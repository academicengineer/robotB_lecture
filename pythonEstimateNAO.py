# NAOでPythonを実行するプログラム 島崎作成
# 変更するのはipとpython_codeのみです。適宜関数化するなどしてご利用ください。

# paramikoモジュールをpipでインストールするとimportできます
import paramiko
import time
from selenium import webdriver
import csv
import numpy as np
import scipy
import pandas as pd

# IPはNAOのボタンをクリックして確認して変更してください。
ip = '192.168.11.18'

# 講義スライドの枚数
slideNum = 3

# ChromeDriverのパス設定
# Chromeのバージョンによってドライバが変わるので注意
driver = webdriver.Chrome('C:\\Users\\member\\Desktop\\slideBrowser\\chromedriver.exe')

# 作成されたOpenposeの特徴量を計算し，受講状態を推定する関数
def estimate(slideNum):
    for i in range (1,slideNum+1):

        # NAOのWebサーバをブラウザで起動
        url = "http://"+ip+"/apps/lec2_slide1.html"
        driver.get(url)
        btn = "slide0"+str(i)+"-btn"
        
        # 鼻，首，右肩，左肩，右目，左目，右耳，左耳の特徴量をcsvファイルから取得
        csvfile_label = "learnerPoseOutput0"+str(i)+"label.csv"
        # with open("C:\\openpose\\json\\"+csvfile_label) as f:
        #with open("C:\\openpose\\json\\"+csvfile_label,encoding="utf-8_sig") as f:
        #keypoint = csv.reader(f)
        #l = [row for row in keypoint]
        #print(l)
        df = pd.read_csv("C:\\openpose\\json\\"+csvfile_label,encoding="utf-8_sig")
        # print(df)
        # print(df.query('信頼度P > 0.8'))
        # print(df.query("label=='R_Ear'&'信頼度P<0.25'"))
        
        R_Eye = df.iloc[15]['信頼度P']
        L_Eye = df.iloc[16]['信頼度P']
        R_Wri = df.iloc[4]['信頼度P']
        L_Wri = df.iloc[7]['信頼度P']
      
        # 受講状態１：聞いていないの判定 
        # 右耳か左耳のいずれかの信頼度が0　または 右耳と左耳の両方の信頼度が0.25以下の場合，
        # 講義意図１：興味を持たせる（注意喚起もしくは注意維持）を実行する
        # NAOの目を光らせる，NAOがパラ言語（ピッチ・音量・速度，間・抑揚）を用いて聞いてくださいとしゃべる
        # if df.query("label=='R_Ear'&'信頼度P<0.25'"):
        if (R_Eye or L_Eye) == 0 or (R_Eye or L_Eye) < 0.25 :
            driver.find_element_by_id("repeat-btn").click()
            driver.find_element_by_id(btn).click()
            print("受講状態１：聞いていないの判定")

        # 受講状態４：詳細を理解しているの判定
        # 右耳か左耳のいずれかの信頼度が85以上，かつ，右手首もしくは左手首の信頼度を取得できている場合，
        # 講義意図３：講義内容の詳細を理解させる（重要箇所の理解促進もしくは関係の理解促進）を実行する
        # NAOがジェスチャーや，パラ言語（ピッチ・音量・速度，間・抑揚）を用いて，スライド間の接続表現を意識してしゃべる，
        elif (R_Eye or L_Eye) > 0.85 and (R_Wri or L_Wri) > 0:
            driver.find_element_by_id("skip-btn").click()
            driver.find_element_by_tag_name("a").click()
            print("受講状態４：詳細を理解しているの判定")

        # 受講状態３：重要箇所に気づくの判定
        # 右耳か左耳のいずれかの信頼度が85以上の場合，
        # 講義意図３：講義内容の詳細を理解させる（重要箇所の理解促進もしくは関係の理解促進）を実行する
        # NAOがジェスチャーや，パラ言語（ピッチ・音量・速度，間・抑揚）を用いてしゃべる，
        elif  (R_Eye or L_Eye) > 0.85 :
            driver.find_element_by_id("pose-btn").click()
            print("受講状態３：重要箇所に気づくの判定")
    
        # 受講状態２：耳を傾けているの判定 上記以外すべての場合，
        # 講義意図２：重要箇所への集中・理解を促す（注意維持・注意誘導もしくは重要箇所の理解促進）を実行する
        # NAOが学習者の視線を意識し，がジェスチャーや，パラ言語（ピッチ・音量・速度，間・抑揚）を用いてしゃべる，
        else:
            driver.find_element_by_id(btn).click()
            print("受講状態２：耳を傾けているの判定")
        
    time.sleep(10)

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

# スライド1枚目
time.sleep(15)
estimate(5)

naoPythonSsh("lec2_slide1.py")
driver.find_element_by_id("skip-btn").click()
naoPythonSsh("setOutputVolume30.py")
naoPythonSsh("lec2_slide2-1.py")
naoPythonSsh("setOutputVolume60.py")
naoPythonSsh("alleds_rasta.py")
naoPythonSsh("lec2_slide2-2.py")
driver.find_element_by_id("skip-btn").click()
naoPythonSsh("setOutputVolume90.py")
naoPythonSsh("altexttospeech_setparameter.py")
driver.find_element_by_id("skip-btn").click()
naoPythonSsh("alleds_rasta.py")
naoPythonSsh("setOutputVolume60.py")
naoPythonSsh("altexttospeech_setparameter_default.py")

# スライド2枚目以降はfor文で繰り返し
#for i in range(2,slideNum+1):
#    naoPythonSsh("lec2_motion7.py")
#    driver.find_element_by_id("skip-btn").click()
    #naoPythonSsh("lec2_slide"+str(i)+".py")
#    naoPythonSsh("lec2_slide"+str(i)+".py")
#    naoPythonSsh("lec2_motion8.py")

#time.sleep(5)
#driver.find_element_by_id("skip-btn").click()
#naoPythonSsh("lec2_slide2.py")