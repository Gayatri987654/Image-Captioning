import cv2

# Open the default camera (usually the webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture frame-by-frame
ret, frame = cap.read()

# Display the captured frame
cv2.imshow('Captured Image', frame)

# Save the captured frame to a file
cv2.imwrite('captured_image.jpg', frame)

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
