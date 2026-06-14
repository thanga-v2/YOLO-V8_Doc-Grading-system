import cv2

# 0 = default webcam (built-in)
# 1 = external webcam
cap = cv2.VideoCapture(0)

# Check if opened
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Camera opened!")
print("Width:",  cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("FPS:",    cap.get(cv2.CAP_PROP_FPS))

cap.release()