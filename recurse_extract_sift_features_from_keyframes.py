'''
Author:  Steve North
Author URI:  http://www.cs.nott.ac.uk/~pszsn/
License: AGPLv3 or later
License URI: http://www.gnu.org/licenses/agpl-3.0.en.html
Can: Commercial Use, Modify, Distribute, Place Warranty
Can't: Sublicence, Hold Liable
Must: Include Copyright, Include License, State Changes, Disclose Source

Copyright (c) 2016, The University of Nottingham
'''

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
