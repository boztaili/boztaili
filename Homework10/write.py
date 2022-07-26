import cv2

# Opens the Video file
cap = cv2.VideoCapture('bird.mkv')
i = 1
while (cap.isOpened()):
    ret, frame = cap.read()
  #  frame = cv2.flip(frame, 0)
    if ret == False:
        break
    if i % 2 == 0:
        cv2.imwrite( str(i) + '.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindow()