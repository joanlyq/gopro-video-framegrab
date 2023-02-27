import cv2

# Open the video file
video = cv2.VideoCapture('path/to/video/file.mp4')

# Get the frames per second (fps)
fps = video.get(cv2.CAP_PROP_FPS)

# Set the frame count
frame_count = 0

# Loop through the video
while True:
    # Read the frame
    ret, frame = video.read()

    # If the frame was not read, break out of the loop
    if not ret:
        break

    # Check if it's time to grab a frame
    if frame_count % fps == 0:
        # Save the frame as an image file
        cv2.imwrite(f'frame{frame_count}.jpg', frame)

    # Increment the frame count
    frame_count += 1

# Release the video file
video.release()
