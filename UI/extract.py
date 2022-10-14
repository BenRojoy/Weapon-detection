# Importing all necessary libraries
import cv2
import os
import shutil
import ast
import sys
import math

from cv2 import threshold

# Read the video from specified path
video = cv2.VideoCapture("static/op.mp4")

if(sys.argv[1]=="wielded"):
    file_name="wielded_frames.txt"
    output_folder="high_severity"
else:
    file_name="unwielded_frames.txt"
    output_folder="medium_severity"

with open('static/output/'+file_name,'r') as f:
   ser = f.read()
detected_frames = set() if ser == str(set()) else ast.literal_eval(ser)

try:

    # creating output folder for saving frames
    if not os.path.exists('static/snapshots/'+output_folder):
        os.makedirs('static/snapshots/'+output_folder)
    folder="static/snapshots/"+output_folder
    if(len(os.listdir(folder))!=0):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    
# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 1
threshold=math.ceil(len(detected_frames)/50) if(len(detected_frames)//50>0) else 1

while(True):

    # reading from frame
    ret, frame = video.read()

    if ret:
        # if video is still left continue creating images
        name = 'static/snapshots/'+output_folder+'/frame' + str(currentframe) + '.jpg'

        # writing the extracted images
        if(currentframe in detected_frames and currentframe % threshold ==0):
            cv2.imwrite(name, frame)

    # increasing counter so that it will
    # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
video.release()
cv2.destroyAllWindows()
