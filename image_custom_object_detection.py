'''
	name: Bo Dem Xe May
'''

from imageai.Detection import ObjectDetection
import os
from time import time

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

our_time = time()

custom = detector.CustomObjects(motorcycle=True)

detections = detector.detectCustomObjectsFromImage( 
	custom_objects=custom
	, input_image=os.path.join(execution_path , "image3.jpg")
	, output_image_path=os.path.join(execution_path , "image3new-custom.jpg")
	, minimum_percentage_probability=30
)

src = [item['name'] for item in detections]

resultDict = dict([ (i, src.count(i)) for i in set(src) ] )

print("===================")
print(
	"Tim thay: {motorcycle} xe may".format(
	motorcycle=resultDict['motorcycle']))
print("===================")
