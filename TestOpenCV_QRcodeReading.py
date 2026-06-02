import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize OpenCV QR code detector from cv2 library
detector = cv2.QRCodeDetector()

print("Looking for QR codes, Press 'x' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Detect and decode QR code
    # data: decoded stuff
    # bbox: bounding box by connecting vertices
    # rectified_image: a transformed, straight version of the QR code
    data, bounds, _ = detector.detectAndDecode(frame) #bbox in the frame,

    # Check if a QR code was detected
    if data:
        print(f"Decoded Data: {data}")
        
        # Draw a bounding box around the QR code if vertices are found
        if bounds is not None:
            for i in range(len(bounds)):
                pt1 = tuple(bounds[i][0].astype(int))
                pt2 = tuple(bounds[(i + 1) % len(bounds)][0].astype(int))
                cv2.line(frame, pt1, pt2, (0, 255, 0), 3)
            
            # Display the decoded text on the frame
            cv2.putText(frame, data, (int(bounds[0][0][0]), int(bounds[0][0][1]) - 10),
                        cv2.FONT_HERSHEY_PLAIN, 0.5, (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('QR Code Scanner', frame)

    # If 'x' pressed get outa there
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()