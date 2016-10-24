from PIL import Image
from pylab import *
from vlfeat_interface import *

keyframe_root_path = "./keyframes"

'''
Expected path to both input video keyframes and output SIFT feature files is: 
./keyframes/behaviour_class_label/individual_video_directory/keyframes/
'''

for behaviour_class_label in os.listdir(keyframe_root_path):
    print "\n"
    path = keyframe_root_path + "/" + behaviour_class_label
    print "behaviour_class_label: " + behaviour_class_label + "\n"
	
    for individual_video_directory in os.listdir(path):
        #print behaviour_class +": "+ individual_video_directory
        videoPath = path + "/" + individual_video_directory + "/keyframes/"
        print "video: " + individual_video_directory
		
        for keyframe in os.listdir(videoPath):
          if ".sift" in keyframe:
            # skip directory called 'keyframes'...it's not a video!
            continue
          process_image(videoPath + keyframe,videoPath + keyframe + '.sift')
        print "\n"
