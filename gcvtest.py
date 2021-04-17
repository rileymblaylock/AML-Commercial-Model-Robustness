import os
path = os.getcwd()
from google.cloud import vision
import io

#set paths
path = path + '\\pics'
DFpath = path + '\\df'
fgsmpath = path + '\\fgsm'
fpgdpath = path + '\\fgpd'

def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    for pic in path:
        with io.open(pic, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')

        for label in labels:
            print(label.description)

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))

detect_labels(path)