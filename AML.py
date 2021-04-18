import csv
import boto3
import os
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

#Accessing user credentials
with open ('new_user_credentials.csv','r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

#photo = "imageadv.png"
#with open (photo, 'rb') as source_image:
 #   source_bites = source_image.read()


#Label Detection using local file
def detect_labels(image, max_labels=10, min_confidence=70):
    rekognition = boto3.client("rekognition",aws_access_key_id = access_key_id,aws_secret_access_key = secret_access_key)
    response = rekognition.detect_labels(
        Image = {'Bytes': source_bites},
        MaxLabels=max_labels,
        MinConfidence=min_confidence,
    )
    return response['Labels']


#Print out the label and confidence scores
#for label in detect_labels(photo):
    #print "{Name} - {Confidence}%".format(**label)
 #   print(label["Name"],"\t\t", label["Confidence"])

#Image to be tested and bucket in which it is kept
BUCKET = "swapsud"
PHOTO = "fish.jpg"


#Label Detection using bucket
def detect_labels(bucket, photo, max_labels=10, min_confidence=70):
    rekognition = boto3.client("rekognition",aws_access_key_id = access_key_id,aws_secret_access_key = secret_access_key)
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
               "Bucket": bucket,
                "Name": photo,
            }
        
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence,
    )
    print('Detected labels for ' + photo) 
    print()   
    for label in response['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("Instances:")
        for instance in label['Instances']:
            print ("  Bounding box")
            print ("    Top: " + str(instance['BoundingBox']['Top']))
            print ("    Left: " + str(instance['BoundingBox']['Left']))
            print ("    Width: " +  str(instance['BoundingBox']['Width']))
            print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        print ("Parents:")
        for parent in label['Parents']:
            print ("   " + parent['Name'])
        print ("----------")
        print ()
    return len(response['Labels'])


detect_labels(BUCKET, PHOTO)
