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

def fingerFunction(w, h): #the function of the program
    cap = cv2.VideoCapture(0) #webcam
    current = 0
    detector = htm.handDetector(detectionCon=0.75)
    tipIds = [8, 12, 16, 20] #the ids of the tips of fingers (without thumb)
    size = [0, 0, w, h] #size of screen

    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=False)
        lmList = detector.findPosition(img) #gets the list of positions of the landmarks of hands

        if len(lmList) != 0: #When the hand is in frame
            fingers = []
            
            if lmList[5][1] > lmList[17][1]: #right thumb
                if lmList[4][1] > lmList[4-1][1]:
                    fingers.append(1)#raised finger
                else:
                    fingers.append(0)#closed finger
            else: #left thumb
                if lmList[4][1] < lmList[4-1][1]:
                    fingers.append(1) #raised finger
                else:
                    fingers.append(0) #closed finger

            #other 4 fingers
            for id in range(4):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)#raised finger
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1) #counts the amount of fingers raised

            if totalFingers == 1: #Take screenshot and record the text onto text file
                #screenshot
                myScreenshot = pyautogui.screenshot(region=(size[0], size[1], size[2], size[3]))
                myScreenshot.save(f'{current}.png')

                imag = Image.open(f'{current}.png') 
                text = tess.image_to_string(imag) #take all text from image
                
                f = open(f'{current}.txt', 'w') #write text onto text file
                f.write(text)
                f.close

                current += 1
                time.sleep(2)

            elif totalFingers == 2: #Screenshot
                myScreenshot = pyautogui.screenshot(region=(size[0], size[1], size[2], size[3]))
                myScreenshot.save(f'{current}.png')

                current += 1
                time.sleep(2)

            elif totalFingers == 3: #only create text file
                #screenshot
                myScreenshot = pyautogui.screenshot(region=(size[0], size[1], size[2], size[3]))
                myScreenshot.save(f'image.png')

                imag = Image.open("image.png")
                text = tess.image_to_string(imag)  #take text from image
                os.remove("image.png")  #delete image

                f = open(f'{current}.txt', 'w') #write text onto file
                f.write(text)
                f.close

                current += 1
                time.sleep(2)

            elif totalFingers == 4:
                break #end program

        cv2.waitKey(1)
#tutorial help: https://www.youtube.com/watch?v=p5Z_GGRCI5s
