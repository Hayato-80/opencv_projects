import cv2 as cv

cap = cv.VideoCapture(0,700)
if not cap.isOpened():
    print("Error: Could not open camera.")

while True:
    _, frame = cap.read()
    cv.imshow('Video', frame)
    # frame = cv.medianBlur(frame, 5)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()