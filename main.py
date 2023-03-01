import os
import argparse
import glob
from tqdm import tqdm
from framegrab import framegrab
import threading

def parse_args():
    parser = argparse.ArgumentParser(description='grab frames from video or folders contain MP4 files')
    parser.add_argument("path", default='', help='the path to the video or folder that contain videos')
    args = parser.parse_args()
    return args.path

if __name__ == '__main__':
    # Parse command line arguments
    path = parse_args()
    if os.path.isfile(path):
        print("One video only")
        framegrab(path)
    elif os.path.isdir(path):
        print("Look for all videos in the folder")
        video_list = [f for f in tqdm(glob.glob(path + "/**/*.mp4", recursive=True))] # you can modify the path that suits your own folder structure better if needed **/T*/
        print("Total {} mp4 videos found".format(len(video_list)))
        threads = []
        for video in tqdm(video_list, desc='Start processing videos'):
            t = threading.Thread(target=framegrab,args=(video,))
            t.start()
            threads.append(t)
        for t in tqdm(threads, desc='finishing processing videos'):
            t.join()
    else:
        print("The input path is not valid, please check again.")

    #grab the directory of individual mp4 videos

    print("\n\nDONE")
    print("\n\n\n\t /\_ /\    ♡\n\t(• - • ̳)\n\t |、ﾞ~ヽ\n\t じしf_; )ノ \n    © Joan Li, 2023")

