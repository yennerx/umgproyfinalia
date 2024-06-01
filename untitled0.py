# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:09:03 2024

@author: Usuario
"""

import cv2

# Dirección IP de la Raspberry Pi y el puerto
url = 'http://192.168.10.218:5000/video_feed'

# Captura de video desde el stream
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
