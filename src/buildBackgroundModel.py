import cv2
from sys import argv
import glob
import numpy as np
import matplotlib.pyplot as plt 


# reads in all images and applies smoothing 
# 2 matrix outputs
#	1) avg for each pixel
#	2) std for each pixel

def smoothImage(framedir):
	# Read in all images from directory
	# Populate a list with gray-scale, smoothed cv2 objects

	piclist = []
	for i in glob.glob(framedir+'*.jpg'):
		src = cv2.imread(i,0)
		piclist.append(cv2.GaussianBlur(src,(5,5),0))

	piclist = np.array(piclist)

	# Avg
	avg = np.average(piclist, axis=0)

	# Std
	std = np.std(piclist, axis=0)

	return([avg, std])




if __name__ == '__main__':
	
	output = smoothImage(argv[1])
	plt.imshow(output[0], cmap='gray')
	plt.show()