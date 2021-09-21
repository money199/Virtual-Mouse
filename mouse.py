import cv2
import numpy as np
import HandTrackingModule as htm
import autopy
import time

######################################
wCam, hCam = 640, 480
frameR = 100  # frame reduction
smoothening = 10

######################
pTime = 0
pLocX, pLocY = 0, 0
cLocX, cLocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()  # return the size of the screen

while True:
    sucess, img = cap.read()

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)


    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]


        fingers = detector.fingersUp()

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        if fingers[1] == 1 and fingers[2] == 0:
            cv2.circle( img , (x1, y1), 15, (255, 0, 0), cv2.FILLED )
            autopy.mouse.click()


        if fingers[1] == 1 and fingers[2] == 1:

            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length <= 40:
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))  # (convert from width of cam to width of screeen
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                cLocX = pLocX + (x3 - pLocX) / smoothening
                cLocY = pLocY + (y3 - pLocY) / smoothening
                autopy.mouse.move(wScr - cLocX, cLocY)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)

                pLocX, pLocY = cLocX, cLocY




    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)

    # 12th :display

    cv2.imshow("img", img)
    cv2.waitKey(1)
