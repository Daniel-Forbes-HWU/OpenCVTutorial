"""Stream camera to OpenCV window."""
import cv2 as cv

# Connect to camera
CAMERA_ID = 0
print(f"Connecting to camera id={CAMERA_ID}...")
source = cv.VideoCapture(CAMERA_ID)
print("Connected")

# Create display window
window_name = f"Camera Preview id={CAMERA_ID}, press ESC key to exit"
cv.namedWindow(window_name, cv.WINDOW_NORMAL)

# Stream camera to window until escape key is pressed
while cv.waitKey(1) != 27:  # Escape
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv.imshow(window_name, frame)

# Disconnect from camera
source.release()

# Destroy window
cv.destroyAllWindows()
    