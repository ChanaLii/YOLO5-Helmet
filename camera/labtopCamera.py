import cv2


def capture_video_frames():
    print("macos camera is running...")
    # Open the camera, o is usually the built-in camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Display the frame in a window
        cv2.imshow('Video', frame)

        # Check for user input to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture_video_frames()
