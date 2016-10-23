from PIL import Image
from pylab import *
from vlfeat_interface import *

#process_image('box.pgm','tmp.sift')
process_image('test.jpg','tmp.sift')
l,d = read_features_from_file('tmp.sift')

im = array(Image.open('test.jpg'))
figure()
plot_features(im,l,True)

show()