"""
import time
from selenium import webdriver
import chromedriver_binary

# ChromeDriverのパス設定
driver = webdriver.Chrome('C:\\Users\\member\\Desktop\\slideBrowser\\chromedriver.exe')

#extension_path ="C:\\Users\\member\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\iodihamcpbpeioajjeobimgagajmlibd\\0.43_0"
#options = webdriver.ChromeOptions()
#options.add_argument(
#    f'load-extension={extension_path}')
 
#driver = webdriver.Chrome(options=options)
#driver.get('chrome-extension://iodihamcpbpeioajjeobimgagajmlibd/html/nassh.html')

# Chromeを起動するためのオプションに拡張機能を追加する
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("C:\\Users\\member\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\iodihamcpbpeioajjeobimgagajmlibd\\0.43_0\\043_0.crx")

driver = webdriver.Chrome(options=chrome_options)
driver.get('chrome-extension://iodihamcpbpeioajjeobimgagajmlibd/html/nassh.html')
"""

# サーバー上で実行するコマンドを設定(ここで嵌る)
#CMD = 'cd /data/home/nao/.local/PackageManager/apps \
#ls \
#python almotion_moveinit.py'

import paramiko

with paramiko.SSHClient() as ssh:
    # 初回ログイン時に「Are you sure you want to continue connecting (yes/no)?」と
    # きかれても問題なく接続できるように。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # ssh接続
    ssh.connect('192.168.11.18', port=22, username='nao', password='kashi-lab')

    # コマンド実行
    # stdin, stdout, stderr = ssh.exec_command('"export LD_LIBRARY_PATH=/opt/aldebaran/lib:/opt/aldebaran/lib/naoqi:/opt/ros/indigo/lib" && "export PYTHONPATH=${PYTHONPATH}:/opt/aldebaran/lib/python2.7/site-packages" && pwd && "/usr/bin/python hello.py" && python hello.py')
    stdin, stdout, stderr = ssh.exec_command("export LD_LIBRARY_PATH=/opt/aldebaran/lib:/opt/aldebaran/lib/naoqi:/opt/ros/indigo/lib && export PYTHONPATH=${PYTHONPATH}:/opt/aldebaran/lib/python2.7/site-packages && python hello.py")
    # コマンド実行後に標準入力が必要な場合
    # stdin.write('password\n')
    # stdin.flush()

    # 実行結果を表示
    for o in stdout:
        print('[std]', o, end='')
    for e in stderr:
        print('[err]', e, end='')


"""
import paramiko
 
def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())vim 
    client.connect(ip, username=user, password=passwd, port=22)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return
 
ssh_command('192.168.11.18', 'nao', 'kashi-lab', 'ls && pythopython hello.py')
"""
