#Libraries for hand tracking
import cv2
import time
import os
import HandTrackingModule as htm

# Importing Libraries for ocr
import pyautogui
import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def fingerFunction(w, h):
    cap = cv2.VideoCapture(0)
    current = 0
    detector = htm.handDetector(detectionCon=0.75)
    tipIds = [8, 12, 16, 20]
    size = [0, 0, w, h]

    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=False)
        lmList = detector.findPosition(img)

        if len(lmList) != 0:
            fingers = []

            if lmList[5][1] > lmList[17][1]: #right thumb
                if lmList[4][1] > lmList[4-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else: #left thumb
                if lmList[4][1] < lmList[4-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            #other 4 fingers
            for id in range(4):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            if totalFingers == 1: #Take screenshot and record the text onto text file
                myScreenshot = pyautogui.screenshot(region=(size[0], size[1], size[2], size[3]))
                myScreenshot.save(f'{current}.png')

                imag = Image.open(f'{current}.png')  # OPEN IMAGE
                text = tess.image_to_string(imag)  # make the text equal to image text
                print(text)
                f = open(f'{current}.txt', 'w')
                f.write(text)
                f.close

                current += 1
                time.sleep(2)

            elif totalFingers == 2:
                myScreenshot = pyautogui.screenshot(region=(size[0], size[1], size[2], size[3]))
                myScreenshot.save(f'{current}.png')

                current += 1
                time.sleep(2)

            elif totalFingers == 3:
                myScreenshot = pyautogui.screenshot(region=(size[0], size[1], size[2], size[3]))
                myScreenshot.save(f'image.png')

                imag = Image.open("image.png")  # OPEN IMAGE
                text = tess.image_to_string(imag)  # make the text equal to image text
                os.remove("image.png")  # REMOVES SS

                f = open(f'{current}.txt', 'w')
                f.write(text)
                f.close

                current += 1
                time.sleep(2)

            elif totalFingers == 4:
                break

        cv2.waitKey(1)
fingerFunction(1920,1080)