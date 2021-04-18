These are notes for how Lane implements the dataset imagenette from her own machine.

Get access token from api.einstein.ai/token
Use account email and account .pem file. There is a .pem file in this branch but it 
expires 4/22/2021. 

Token code that expires 4/16/2021 at ~9:25 pm central:
JFJDETJWIVFFGWCPIJCVIUBSJFBVEQ2WJM2E6R2ZKZDVAUBSGRBEUWKZKYZESTRTKJCUUWJSJ43EOWCGGYZUUSBXIRBVAT2IJQZFSVSSJBKFETCVKM3TEMRVKBDDIWKMJJLVIWCQGNHEWWSHKJITKVSHJBGTMVKKIFKVS7COIE

Model ID where name is Beaches and Mountains Model:
TW2DN6VIJB2SMRQ7WG5Y2HFEZY

Create Dataset:
The following command is not edited:
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "type=image" -F "path=https://einstein.ai/images/mountainvsbeach.zip" https://api.einstein.ai/v2/vision/datasets/upload/sync

The following command contains the <TOKEN> and the "path" for the images:
curl -X POST -H "Authorization: Bearer JFJDETJWIVFFGWCPIJCVIUBSJFBVEQ2WJM2E6R2ZKZDVAUBSGRBEUWKZKYZESTRTKJCUUWJSJ43EOWCGGYZUUSBXIRBVAT2IJQZFSVSSJBKFETCVKM3TEMRVKBDDIWKMJJLVIWCQGNHEWWSHKJITKVSHJBGTMVKKIFKVS7COIE" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "data=@C:\Users\vlcol\OneDrive\Desktop\meta.zip" -F "type=image" https://api.einstein.ai/v2/vision/datasets/upload/sync

//NOTE: The path must be a public URL and so a .zip file was uploaded onto the Salesforce files page.
//public link that will expire with the account: https://olemiss5.my.salesforce.com/sfc/p/5Y0000025uED/a/5Y0000019OPf/ccGb91dOHQQp6viJR2KxmMfN5k5WcEp556p.zu9OAUI
//link to the .zip file in Lane's OneDrive: https://1drv.ms/u/s!AsV2bQ2d5pmEivw-k2CJQ3sc74B_rg?e=8ayNOn 

The above // is not true. To use foldr from local drive, it cannot exceed 50 megabytes. Online can be up to 1 gigabyte,
however the file thus far has been "invalid" with the two aproaches from the // section. To reference a local file,
you need "data=@FILEPATH" rather than "path=FILEPATH". 

The following command lists the datasets:
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets

The following command lists the datasets with the token used for copy and paste:
curl -X GET -H "Authorization: Bearer JFJDETJWIVFFGWCPIJCVIUBSJFBVEQ2WJM2E6R2ZKZDVAUBSGRBEUWKZKYZESTRTKJCUUWJSJ43EOWCGGYZUUSBXIRBVAT2IJQZFSVSSJBKFETCVKM3TEMRVKBDDIWKMJJLVIWCQGNHEWWSHKJITKVSHJBGTMVKKIFKVS7COIE" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets

DELETE datasets:
curl -X DELETE -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets/<DATASET_ID>

curl -X DELETE -H "Authorization: Bearer JFJDETJWIVFFGWCPIJCVIUBSJFBVEQ2WJM2E6R2ZKZDVAUBSGRBEUWKZKYZESTRTKJCUUWJSJ43EOWCGGYZUUSBXIRBVAT2IJQZFSVSSJBKFETCVKM3TEMRVKBDDIWKMJJLVIWCQGNHEWWSHKJITKVSHJBGTMVKKIFKVS7COIE" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets/1265485

TRAIN datasets:
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "name=Beach and Mountain Model" -F "datasetId=<DATASET_ID>" https://api.einstein.ai/v2/vision/train

curl -X POST -H "Authorization: Bearer JFJDETJWIVFFGWCPIJCVIUBSJFBVEQ2WJM2E6R2ZKZDVAUBSGRBEUWKZKYZESTRTKJCUUWJSJ43EOWCGGYZUUSBXIRBVAT2IJQZFSVSSJBKFETCVKM3TEMRVKBDDIWKMJJLVIWCQGNHEWWSHKJITKVSHJBGTMVKKIFKVS7COIE" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "name=Bull Mastiff and Horse Cestnut and Strawberry Model" -F "datasetId=1265484" https://api.einstein.ai/v2/vision/train

STATUS of training:
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/train/<YOUR_MODEL_ID>

curl -X GET -H "Authorization: Bearer JFJDETJWIVFFGWCPIJCVIUBSJFBVEQ2WJM2E6R2ZKZDVAUBSGRBEUWKZKYZESTRTKJCUUWJSJ43EOWCGGYZUUSBXIRBVAT2IJQZFSVSSJBKFETCVKM3TEMRVKBDDIWKMJJLVIWCQGNHEWWSHKJITKVSHJBGTMVKKIFKVS7COIE" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/train/TW2DN6VIJB2SMRQ7WG5Y2HFEZY

METRICS of model:
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/models/<MODEL_ID>

curl -X GET -H "Authorization: Bearer JFJDETJWIVFFGWCPIJCVIUBSJFBVEQ2WJM2E6R2ZKZDVAUBSGRBEUWKZKYZESTRTKJCUUWJSJ43EOWCGGYZUUSBXIRBVAT2IJQZFSVSSJBKFETCVKM3TEMRVKBDDIWKMJJLVIWCQGNHEWWSHKJITKVSHJBGTMVKKIFKVS7COIE" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/models/TW2DN6VIJB2SMRQ7WG5Y2HFEZY

CLASSIFY an image:
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "sampleLocation=http://einstein.ai/images/546212389.jpg" -F "modelId=<YOUR_MODEL_ID>" https://api.einstein.ai/v2/vision/predict

curl -X POST -H "Authorization: Bearer GI2EGWJSJNIESNRTGJCDOT2SINFUMVBWLBGFOVKTGVNEKVCBJ42VSV2DKJCEENCDGZBVGUKPJ5JUYNSLLFKFEUZUJZBVSSKLLJNEIRRUK5DVEQSVKRCTOVSFIJHVGNKNII2E2WCBIFGECRKMJZIUWUCUIFGVITCTJJKUC7COIE" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "sampleContent=@C:\Users\vlcol\OneDrive\Desktop\AML-Commercial-Model-Robustness\pics\pgd\1_tensor(949)_.png" -F "modelId=TW2DN6VIJB2SMRQ7WG5Y2HFEZY" https://api.einstein.ai/v2/vision/predict
