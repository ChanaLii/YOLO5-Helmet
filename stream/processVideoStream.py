import cv2
import os
import glob


def del_tmp_files(dir_path):
    try:
        file_paths = glob.glob(os.path.join(dir_path, '*'))
        for file_path in file_paths:
            os.remove(file_path)
            print(f'File [{file_path}] was delete successfully.')
    except FileNotFoundError:
        print(f'File [{dir_path}] was not found.')
    except PermissionError:
        print(f'Permission denied.Unable delete the file [{dir_path}]')
    except Exception as e:
        print(f'Unknown exception while delete the files: {e}')


def capture_video_frame(frame_count, win_name):
    print("macos camera is running...")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        # check if frame was read successfully
        if not ret:
            break

        # TODO Process the frame, which was to use for YOLO5 model

        # Process the frame, output a pic for seconds
        frame_count += 1
        file_name = f"frame_{frame_count}.jpg"
        saved = cv2.imwrite(f'../data_set/develop_data/{file_name}', frame)
        if saved:
            print(f"frame_{frame_count} save as {file_name}")
        else:
            print(f"Failed to save frame {frame_count}")

        # Display on the window
        cv2.imshow(win_name, frame)

        # Check for user input to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyWindow(win_name)


if __name__ == '__main__':
    # frame
    frame_count = 0
    win_name = 'Video'
    capture_video_frame(frame_count, win_name)

    # the path of delete jpg
    # dir_path = '../data_set/develop_data'
    # del_tmp_files(dir_path)
