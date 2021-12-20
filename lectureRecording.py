
#  (720*1280 30fps の IMG_sample.MOVをoutput.mp4に変換)

import argparse
import logging
import time
import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

from tf_pose import common
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

img_outdir = './img'
os.makedirs(img_outdir, exist_ok=True)

# 動画作成
os.system('ffmpeg -i IMG_sample.MOV sample.mp4')
width = 720
height = 1280
fps = 30.0

fourcc = cv2.VideoWriter_fourcc('m','p','4', 'v')
video  = cv2.VideoWriter('tmp_video.mp4', fourcc, fps, (width, height))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation Video')

    outimg_files = []
    count = 0
    w = 544 
    h = 960
    e = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(w, h))

    # 入力動画
    cap = cv2.VideoCapture('sample.mp4')

    # 動画用の音声切出し
    os.system('ffmpeg -i "sample.mp4" -map 0:1 -vn -ac 2 -acodec pcm_s24le -f wav "audio.wav"')

    # 動画用の画像作成
    while True:
        ret, image = cap.read()

        if ret == True:
            # １フレームずつ処理
            count += 1
            if count % 100 == 0:
                print('Image No.：{0}'.format(count))

            humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=4)
            image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

            # 画像出力
            outimg_file = '{}/{:05d}.jpg'.format(img_outdir, count)
            cv2.imwrite(outimg_file, image)
            image = cv2.resize(image, (width,height))
            video.write(image)       

        else:
            break


    video.release()
    os.system('ffmpeg -i tmp_video.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4')
