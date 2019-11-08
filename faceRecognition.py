import cv2
import os
import numpy as np


def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img, cv2.COLOR_BGRGRAY)
    face_haar_cascade=cv2.CascadeClassifier('')