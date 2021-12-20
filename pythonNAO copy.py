#
# 状態推定なし
#

# paramikoモジュールをpipでインストールするとimportできます
import paramiko
import time
from selenium import webdriver

# IPはNAOのボタンをクリックして確認して変更してください。
ip = '192.168.11.18'
lecture = 'lec2'
slide_num = 4

# ChromeDriverのパス設定
# Chromeのバージョンによってドライバが変わるので注意
driver = webdriver.Chrome('C:\\Users\\member\\Desktop\\slideBrowser\\chromedriver.exe')

# NAOのWebサーバをブラウザで起動
driver.get("http://"+ip+"/apps/lec2_slide1.html")

#ここにPythonで実行したいプログラム名を記載
# python_code = 'hello.py'

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
time.sleep(10)

#for i in range (1,slide_num+1):
#    #naoPythonSsh("pointing.py")


#    naoPythonSsh(lecture+"_slide"+str(i)+".py")
#    driver.find_element_by_id("skip-btn").click()

#naoPythonSsh("lec2_slide3.py")
#naoPythonSsh("estimate4.py")

naoPythonSsh("lec2_slide1.py")
driver.find_element_by_id("skip-btn").click()
naoPythonSsh("lec2_slide2-1.py")
driver.find_element_by_id("skip-btn").click()
naoPythonSsh("lec2_slide3.py")
driver.find_element_by_id("skip-btn").click()
naoPythonSsh("lec2_slide4.py")
driver.find_element_by_id("skip-btn").click()
naoPythonSsh("lec2_slide5.py")
driver.find_element_by_id("skip-btn").click()

#naoPythonSsh("setOutputVolume30.py")
#naoPythonSsh("lec2_slide2-1.py")
#naoPythonSsh("setOutputVolume60.py")
#naoPythonSsh("lec2_slide2-2.py")
#naoPythonSsh("altexttospeech_setparameter.py")
#driver.find_element_by_id("skip-btn").click()
#naoPythonSsh("setOutputVolume30.py")
#naoPythonSsh("altexttospeech_setparameter.py")
#naoPythonSsh("lec2_slide3.py")
#driver.find_element_by_id("skip-btn").click()
#naoPythonSsh("setOutputVolume60.py")
#naoPythonSsh("lec2_slide4.py")

# スライド2枚目以降はfor文で繰り返し
#for i in range(2,slideNum+1):
#    naoPythonSsh("lec2_motion7.py")
#    driver.find_element_by_id("skip-btn").click()
#    #naoPythonSsh("lec2_slide"+str(i)+".py")
#    naoPythonSsh("lec2_slide"+str(i)+".py")
#    naoPythonSsh("lec2_motion8.py")

#time.sleep(5)
#driver.find_element_by_id("skip-btn").click()
#naoPythonSsh("lec2_slide2.py")