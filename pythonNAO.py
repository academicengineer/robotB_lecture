# NAOでPythonを実行するプログラム 島崎作成
# 変更するのはipとpython_codeのみです。適宜関数化するなどしてご利用ください。

# インポート
import cv2          # OpenCV
import subprocess   # コマンドプロンプトの操作に利用
import os           # コマンドプロンプトの操作に利用
import shutil       # ファイルの移動に利用
import dlib         # 機械学習系ライブラリ
import imutils      # OpenCVの補助
from imutils import face_utils
import json
import pandas as pd
from pandas.io.json import json_normalize
import pprint
import csv
import numpy as np
import scipy
import pandas as pd
import paramiko
import time
from selenium import webdriver

# IPはNAOのボタンをクリックして確認して変更してください。
ip = '192.168.11.18'
lecture = 'lec2'
slide_num = 4

# 使用するWebカメラの選択
webcam_id=0

# ChromeDriverのパス設定
# Chromeのバージョンによってドライバが変わるので注意
driver = webdriver.Chrome('C:\\Users\\member\\Desktop\\slideBrowser\\chromedriver.exe')

# NAOにsshでPythonを実行するプログラム
def naoPythonSsh(python_code):
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # ssh接続 IPはNAOのボタンをクリックして確認して変更してください。
        ssh.connect(ip, port=22, username='nao', password='kashi-lab')

        # Pythonの実行
        stdin, stdout, stderr = ssh.exec_command("export LD_LIBRARY_PATH=/opt/aldebaran/lib:/opt/aldebaran/lib/naoqi:/opt/ros/indigo/lib && export PYTHONPATH=${PYTHONPATH}:/opt/aldebaran/lib/python2.7/site-packages && python "+python_code)
    
        # Python実行結果を表示
        # stdoutは標準出力の正常結果，stderrは標準出力のエラーが出力
        for o in stdout:
            print('[std]', o, end='')
        for e in stderr:
            print('[err]', e, end='')

# 状態推定を行うプログラム
def estimate(slide_num):
    for i in range (1,slide_num+1):

        # ブラウザを開く
        url = "http://"+ip+"/apps/"+lecture+"_slide1.html"
        driver.get(url)

        # Openposeの実行

        # ノートPCのディレクトリの移動
        os.chdir("C://openpose")

        # Openposeで姿勢推定するための学習者の画像をWebカメラで撮影
        print("Webカメラで姿勢を撮影します"+str(i)+"回目:")
        capture = cv2.VideoCapture(webcam_id)
        poseret, poseframe = capture.read()
        poseid = "learnerPose0"+ str(i)
        # image = "learnerPose"+ str(i)+ ".jpg"
        #poseid = "learnerPose"+ "00"
        poseimage =  poseid + ".jpg"
        cv2.imwrite(poseimage, poseframe)
        shutil.move(poseimage,"examples//media")
        # shutil.move(poseimage,"poseimage")
        print(poseimage+"を撮影しました")

        # Openposeにより姿勢推定を実行し，jsonファイルを出力
        print("視線推定を開始します"+str(i)+"回目:")
        cmd = "bin\OpenPoseDemo.exe --image_dir examples\media\ --write_json ."
        # cmd = "bin\OpenPoseDemo.exe --image_dir examples\media\ --face --hand  --write_json ."
        print(poseimage)
        poseres = subprocess.call(cmd, shell=True)
        jsonfile = poseid + "_keypoints.json"
        shutil.move(jsonfile,"json")
        print(jsonfile+"を作成しました")

        # json から必要な評価指標のみ抽出した csv　ファイルを作成する
        os.chdir("C://openpose//json")

        #poseid = "learnerPose0"+ str(i)
        #jsonfile = str((poseid + "_keypoints.json"))
        #print(jsonfile)
    
        # JSONファイルを開き，読み込む
        json_open = open(jsonfile, 'r')
        json_load = json.load(json_open)

        # JSONファイルの加工
        data = np.array(json_load['people'][0]['pose_keypoints_2d']).reshape(-1,3)
        df_label = pd.DataFrame(data, columns=['X座標','Y座標','信頼度P'], index=['Nose','Neck','R_Sholder','R_Elbow','R_Wrist','L_Sholder','L_Elbow','L_Wrist','Hip','R_Hip','R_nee','R_Ankle','L_Hip','L_Knee','L_Ankle','R_Eye','L_Eye','R_Ear','L_Ear','L_foot1','L_foot2','L_foot3','R_foot1','R_foot2','R_foot3'])

        # columnsを表示させる時は上記のコメントアウトを外し，下記をコメントアウト
        df = pd.DataFrame(data, index=['Nose','Neck','R_Sholder','R_Elbow','R_Wrist','L_Sholder','L_Elbow','L_Wrist','Hip','R_Hip','R_nee','R_Ankle','L_Hip','L_Knee','L_Ankle','R_Eye','L_Eye','R_Ear','L_Ear','L_foot1','L_foot2','L_foot3','R_foot1','R_foot2','R_foot3'])

        # 削除する姿勢座標を選択
        drop_index = ['R_Elbow','R_Wrist','L_Elbow','L_Wrist','Hip','R_Hip','R_nee','R_Ankle','L_Hip','L_Knee','L_Ankle','L_foot1','L_foot2','L_foot3','R_foot1','R_foot2','R_foot3']
    
        # 削除
        df = df.drop(drop_index, axis=0)

        # CSVに掃き出し
        csvfile_label = "learnerPoseOutput0"+str(i)+"label.csv"
        csvfile = "learnerPoseOutput0"+str(i)+".csv"
        #print(csvfile)

        # df.to_csv(csvfile, encoding='utf-8')

        # indexを表示させる時は上記のコメントアウトを外し，下記をコメントアウト
        df_label.to_csv(csvfile_label, encoding='utf-8')
        df.to_csv(csvfile, encoding='utf-8', index=False)
        print(csvfile_label+"と"+csvfile+"を作成しました")

        # CSVの座標とif文で比較し，学習者の状態を推定

        # 予め用意したCSVファイルを読み込み
        #csvdata_state1 = pd.read_csv("learnerStateCSV01.csv", header=None)
        #csvdata_state2 = pd.read_csv("learnerStateCSV02.csv", header=None)
        #csvdata_state3 = pd.read_csv("learnerStateCSV03.csv", header=None)
        #csvdata_state4 = pd.read_csv("learnerStateCSV04.csv", header=None)

        # スライド毎の学習者の姿勢座標を読み込み
        #csvdata_input = pd.read_csv(csvfile, header=None)

        #state1_array     = np.array
        #state2_array     = np.array
        #state3_array     = np.array
        #state4_array     = np.array
        #input_array      = np.array

        #state1_array     = csvdata_state1.values
        #state2_array     = csvdata_state2.values
        #state3_array     = csvdata_state3.values
        #state4_array     = csvdata_state4.values
        #input_array      = csvdata_input.values

        # 行列の引き算
        #result1 = state1_array - input_array
        #result2 = state2_array - input_array
        #result3 = state3_array - input_array
        #result4 = state4_array - input_array

        # 結果の行列をCSVファイルに書き出し
        #with open("result1_data.csv", "w") as r1:
        #    csv_w1 = csv.writer(r1, lineterminator='\n')
        #    csv_w1.writerows(result1)
    
        #with open("result2_data.csv", "w") as r2:
        #    csv_w2 = csv.writer(r2, lineterminator='\n')
        #    csv_w2.writerows(result2)

        #with open("result3_data.csv", "w") as r3:
        #    csv_w3 = csv.writer(r3, lineterminator='\n')
        #    csv_w3.writerows(result3)

        #with open("result4_data.csv", "w") as r4:
        #    csv_w4 = csv.writer(r4, lineterminator='\n')
        #    csv_w4.writerows(result4)
        
        # 鼻，首，右肩，左肩，右目，左目，右耳，左耳の特徴量をcsvファイルから取得
        csvfile_label = "learnerPoseOutput0"+str(i)+"label.csv"

        # Pandasで加工
        df = pd.read_csv("C:\\openpose\\json\\"+csvfile_label,encoding="utf-8_sig")

        # Openposeの信頼度を抽出
        R_Eye = df.iloc[15]['信頼度P']
        L_Eye = df.iloc[16]['信頼度P']
        R_Wri = df.iloc[4]['信頼度P']
        L_Wri = df.iloc[7]['信頼度P']

        # NAOに話させるプログラムの実行
        naoPythonSsh(lecture+"_slide"+str(i)+".py")

        # 受講状態１：聞いていないの判定 
        # 右耳か左耳のいずれかの信頼度が0　または 右耳と左耳の両方の信頼度が0.25以下の場合，
        # 講義意図１：興味を持たせる（注意喚起もしくは注意維持）を実行する
        # NAOの目を光らせる，NAOがパラ言語（ピッチ・音量・速度，間・抑揚）を用いて聞いてくださいとしゃべる
        # if df.query("label=='R_Ear'&'信頼度P<0.25'"):
        if (R_Eye or L_Eye) == 0 or (R_Eye or L_Eye) < 0.25 :
            naoPythonSsh("estimate1.py")
            #driver.find_element_by_id("skip-btn").click()
            print("受講状態１：聞いていないの判定")

        # 受講状態４：詳細を理解しているの判定
        # 右耳か左耳のいずれかの信頼度が85以上，かつ，右手首もしくは左手首の信頼度を取得できている場合，
        # 講義意図３：講義内容の詳細を理解させる（重要箇所の理解促進もしくは関係の理解促進）を実行する
        # NAOがジェスチャーや，パラ言語（ピッチ・音量・速度，間・抑揚）を用いて，スライド間の接続表現を意識してしゃべる，
        elif (R_Eye or L_Eye) > 0.85 and (R_Wri or L_Wri) > 0 :
            naoPythonSsh("estimate4.py")
            #driver.find_element_by_id("skip-btn").click()
            print("受講状態４：詳細を理解しているの判定")
        
        # 受講状態３：重要箇所に気づくの判定
        # 右耳か左耳のいずれかの信頼度が85以上の場合，
        # 講義意図３：講義内容の詳細を理解させる（重要箇所の理解促進もしくは関係の理解促進）を実行する
        # NAOがジェスチャーや，パラ言語（ピッチ・音量・速度，間・抑揚）を用いてしゃべる，
        elif  (R_Eye or L_Eye) > 0.85 :
            naoPythonSsh("estimate3.py")
            #driver.find_element_by_id("skip-btn").click()
            print("受講状態３：重要箇所に気づくの判定")
    
        # 受講状態２：耳を傾けているの判定 上記以外すべての場合，
        # 講義意図２：重要箇所への集中・理解を促す（注意維持・注意誘導もしくは重要箇所の理解促進）を実行する
        # NAOが学習者の視線を意識し，がジェスチャーや，パラ言語（ピッチ・音量・速度，間・抑揚）を用いてしゃべる，
        else:
            naoPythonSsh("estimate2.py")
            #driver.find_element_by_id("skip-btn").click()
            print("受講状態２：耳を傾けているの判定")
        
        driver.find_element_by_id("skip-btn").click()

# 状態推定を行うロボット講義は，関数estimateを利用
estimate(slide_num)

# 状態推定を行わないロボット講義は，関数naoPythonSshをfor文を持ちて回す