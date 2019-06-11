'''
	name: Bo dem phuong tien: xe may, xe bus, car, truck
'''

import os
import csv
from time import time
from collections import Counter
from imageai.Detection import ObjectDetection


# bien moi truong & thu muc data
imagePath = '/home/nema/Downloads/limit/git_projt/ImageAI/tesst/'
arr = [ x for x in os.listdir(imagePath) if x.endswith(".jpg") ]

# chon model && load
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()

for eachImage in arr:
	print(eachImage)
	
	with open('aTest.csv', 'a') as csvfile:
		our_time = time()
		detections = detector.detectObjectsFromImage(
			input_image= "{dir}{path}".format(
				dir=imagePath, path=eachImage)
			, output_image_path= "result/{name}-result.jpg".format(
				name=eachImage)
			, minimum_percentage_probability= 30
		)
		print("IT TOOK : ", time() - our_time)
		
		# beautify
		src = [
			item['name'] for item in detections 
			if item['name'] in ['motorcycle', 'car' ,'bus','truck'] 
		]
		
		# dem tong tung loai phuong tien
		resultDict = dict([ (i, src.count(i)) for i in set(src) ] )
		
		# chuan bi ghi vao tep
		resultDict['file'] = eachImage
		print(resultDict)

		fieldNames = ['file', 'motorcycle', 'car', 'bus', 'truck']
		writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
		writer.writerow(resultDict) 

	csvfile.close()	

print("Writing complete")

