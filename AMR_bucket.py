import boto3
import io
import csv
import os
import matplotlib.pyplot as plt
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

#Accessing user credentials
with open ('new_user_credentials.csv','r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]


bucket = 'swapsud'
key = '0.0005_tensor(243)_.png'

#Label Detection using amazon s3 bucket
def detect_labels(bucket,key,max_labels=10, min_confidence=70,):
    rekognition = boto3.client("rekognition",aws_access_key_id = access_key_id,aws_secret_access_key = secret_access_key)
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
               "Bucket": bucket,
                "Name": key,
            }
        
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence,
    )
    return response['Labels']

label_name = []
cf_score = []
for label in detect_labels(bucket, key):
    print ("{Name} - {Confidence}%".format(**label))
    label_name.append(label['Name'])
    cf_score.append(label['Confidence'])
    
    
data = dict(zip(label_name,cf_score))
fig,ax = plt.subplots()
rects1 = ax.bar(data.keys(), data.values(), color='b',width = 0.25)
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,'%.3f' % float(height),ha='center', va='bottom')
autolabel(rects1)
plt.xlabel("labels detected")
plt.ylabel("Confidence percentage ")
plt.tight_layout()
plt.savefig('bargraph.pdf')
plt.show()

