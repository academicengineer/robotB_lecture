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
    stdin, stdout, stderr = ssh.exec_command('ls & /usr/bin/python hello.py')

    # コマンド実行後に標準入力が必要な場合
    # stdin.write('password\n')
    # stdin.flush()

    # 実行結果を表示
    for o in stdout:
        print('[std]', o, end='')
    for e in stderr:
        print('[err]', e, end='')