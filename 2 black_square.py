import cv2

cap = cv2.VideoCapture(0)
'''
list_example = [0, 1, 2, 3, 4, 5]
print(list_example[1:3])
exit()
'''
while True:
    ret, frame = cap.read()
    print(frame.shape)
    height, width, _ = frame.shape
    frame[height - 100:, width - 100:] = [0, 0, 0]
    frame[:100, width - 100:] = [0, 0, 0]
    frame[:100, :100] = [0, 0, 0]
    frame[height - 100:, :100] = [0, 0, 0]
    frame[height//2 - 50:height//2 + 50, width//2 - 50:width//2 + 50] = [0, 0, 0]
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1000)
    print(key)
    if key == ord(' '):
        break



cv2.destroyAllWindows()
cap.release()