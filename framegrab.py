import cv2
import os
from tqdm import tqdm

#function to grab frames per second and save it into the same folder as the images. 
def framegrab(video_dir):
    #set progress bar
    progress=tqdm(desc='Grabbing frames')
    progress.set_postfix(file=video_dir)

    # Open the video file
    video = cv2.VideoCapture(video_dir)
    video_n = os.path.splitext(video_dir)[0]

    # Get the frames per second (fps)
    fps = round(video.get(cv2.CAP_PROP_FPS))

    # Set the frame count
    frame_count = 0
    i = 1

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
            cv2.imwrite(f'{video_n}_{i:04d}.jpg', frame)
            # uncomment the line below if you want to remove the frames being created. 
            # os.remove(f'{video_n}_{i:04d}.jpg')
            i += 1
        # Increment the frame count
        frame_count += 1
        progress.update()

    # Release the video file
    video.release()
