import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, prev_frame = cap.read()
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

kernel = np.ones((5,5), np.uint8)
while True:
    ret, frame = cap.read()
    if not ret:
        print('Video ended.')
        break

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (21, 21), 0)

    fgmask = fgbg.apply(frame)

    dilation = cv2.dilate(fgmask, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(image=dilation, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
    
        (x, y, w , h) = cv2.boundingRect(contour)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.drawContours(image=frame, contours=contours, contourIdx=-1, color=(0,0,255), thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow("Motion Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
