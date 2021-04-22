These are notes for how Lane implements the dataset from her own machine.

The files and descriptions in this folder (einsteinAPI_Docs) are as follows:
bullMastiff.txt -> results of classifying perturbed bullMastiff images
horseChestnut.txt -> results of classifying perturbed horseChestnut images
strawberry.txt -> results of classifying perturbed strawberry images
tests.txt -> results of classifying random images
metamind_datasets_outputs.txt -> info on the used dataset
metrics_output.txt -> metrics of the two successful models
meta_probability.xlsx -> bullMastiff, horseChestnut, and strawberry results in spreadsheet
charts.docx -> bullMastiff, horseChestnut, and strawberry results as bar graphs

Get access token from api.einstein.ai/token
Use account email and account .pem file. There is a .pem file in this branch but it 
expires 4/22/2021. 

The following are model ID's that the API trained from various sets of images found in 
pics/resnet:
Model ID: 
Beaches and Mountains Model:
TW2DN6VIJB2SMRQ7WG5Y2HFEZY

CSCI 691 Test Model:
JQDLQXTHBA77T535BXXDEHN72Q

Mastiff and Strawberry and Conker Test 2:
54GDKEPKNV5HY7VJ2T7H5YR6HU

BIA Images Test Model:
U5XSYUKEM2TULKSABXH26NUB3U

The following commands are how Lane used the API. The commands can be entered into any 
machine's CLI with curl.

CREATE Dataset:
Replace <TOKEN> with access token and "path" with where your zip file is. The current 
path is the API example. 

curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "type=image" -F "path=https://einstein.ai/images/mountainvsbeach.zip" https://api.einstein.ai/v2/vision/datasets/upload/sync

NOTE: To use folder from local drive, it cannot exceed 50 megabytes. Online can be up to 1 gigabyte. 
To reference a local file, you need "data=@FILEPATH" rather than "path=FILEPATH". 

NOTE: Must have at least 40 items to train. Each label must have at least 10 images. 

LIST datasets:
Replace <TOKEN> with access token.
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets

DELETE datasets:
Replace <TOKEN> with access token. Replace <DATASET_ID> with dataset id which can be found with previous command. 
curl -X DELETE -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets/<DATASET_ID>

TRAIN datasets:
Replace <TOKEN> with access token. Replace "name" with a desired model name. Replace <DATASET_ID> with dataset id.
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "name=Beach and Mountain Model" -F "datasetId=<DATASET_ID>" https://api.einstein.ai/v2/vision/train

NOTE: The output of this command gives the user a model id which will be used in the next three commands. 

STATUS of training:
Replace <TOKEN> with access token. Replace <YOUR_MODEL_ID> with model id. 
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/train/<YOUR_MODEL_ID>

METRICS of model:
Replace <TOKEN> with access token. Replace <YOUR_MODEL_ID> with model id. 
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/models/<MODEL_ID>

CLASSIFY an image:
Replace <TOKEN> with access token. Replace "sampleLocation" with url location of image. Replace <YOUR_MODEL_ID> with model id. 
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "sampleLocation=http://einstein.ai/images/546212389.jpg" -F "modelId=<YOUR_MODEL_ID>" https://api.einstein.ai/v2/vision/predict

NOTE: A user can also use a local image. 