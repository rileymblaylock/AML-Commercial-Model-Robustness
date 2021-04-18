These are notes for how Lane implements the dataset from her own machine.

Get access token from api.einstein.ai/token
Use account email and account .pem file. There is a .pem file in this branch but it 
expires 4/22/2021. 

Token code that expires 4/16/2021 at ~9:25 pm central:
KBCU4U2ZJ43UURZWIJAU6T2BLBGUIMSGKI3EKNCUKI2DIQ2YGZKUCU2GG5HFMQSBGRDEYQKLGNFVIQ2TGZEVCRSDGZCFONCUKZKEIR2EIM3DMS2ZGJBVMNSJJVEVQWCJJE2DMRKZKE2VGWKSIYZDOSCVIJGFMUCILBDEC7COIE

Model ID: 
Beaches and Mountains Model:
TW2DN6VIJB2SMRQ7WG5Y2HFEZY

CSCI 691 Test Model:
JQDLQXTHBA77T535BXXDEHN72Q

CREATE Dataset:
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "type=image" -F "path=https://einstein.ai/images/mountainvsbeach.zip" https://api.einstein.ai/v2/vision/datasets/upload/sync

curl -X POST -H "Authorization: Bearer KBCU4U2ZJ43UURZWIJAU6T2BLBGUIMSGKI3EKNCUKI2DIQ2YGZKUCU2GG5HFMQSBGRDEYQKLGNFVIQ2TGZEVCRSDGZCFONCUKZKEIR2EIM3DMS2ZGJBVMNSJJVEVQWCJJE2DMRKZKE2VGWKSIYZDOSCVIJGFMUCILBDEC7COIE" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "data=@C:\Users\vlcol\OneDrive\Desktop\bia.zip" -F "type=image" https://api.einstein.ai/v2/vision/datasets/upload/sync | json

NOTE: To use foldr from local drive, it cannot exceed 50 megabytes. Online can be up to 1 gigabyte. 
To reference a local file, you need "data=@FILEPATH" rather than "path=FILEPATH". 

NOTE: Must have at least 40 items to train. 

LIST datasets:
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets

curl -X GET -H "Authorization: Bearer KBCU4U2ZJ43UURZWIJAU6T2BLBGUIMSGKI3EKNCUKI2DIQ2YGZKUCU2GG5HFMQSBGRDEYQKLGNFVIQ2TGZEVCRSDGZCFONCUKZKEIR2EIM3DMS2ZGJBVMNSJJVEVQWCJJE2DMRKZKE2VGWKSIYZDOSCVIJGFMUCILBDEC7COIE" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets | json

DELETE datasets:
curl -X DELETE -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets/<DATASET_ID>

curl -X DELETE -H "Authorization: Bearer KBCU4U2ZJ43UURZWIJAU6T2BLBGUIMSGKI3EKNCUKI2DIQ2YGZKUCU2GG5HFMQSBGRDEYQKLGNFVIQ2TGZEVCRSDGZCFONCUKZKEIR2EIM3DMS2ZGJBVMNSJJVEVQWCJJE2DMRKZKE2VGWKSIYZDOSCVIJGFMUCILBDEC7COIE" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/datasets/1265574 | json

TRAIN datasets:
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "name=Beach and Mountain Model" -F "datasetId=<DATASET_ID>" https://api.einstein.ai/v2/vision/train

curl -X POST -H "Authorization: Bearer KBCU4U2ZJ43UURZWIJAU6T2BLBGUIMSGKI3EKNCUKI2DIQ2YGZKUCU2GG5HFMQSBGRDEYQKLGNFVIQ2TGZEVCRSDGZCFONCUKZKEIR2EIM3DMS2ZGJBVMNSJJVEVQWCJJE2DMRKZKE2VGWKSIYZDOSCVIJGFMUCILBDEC7COIE" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "name=CSCI 691 Test Model" -F "datasetId=1265577" https://api.einstein.ai/v2/vision/train | json

STATUS of training:
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/train/<YOUR_MODEL_ID>

curl -X GET -H "Authorization: Bearer KBCU4U2ZJ43UURZWIJAU6T2BLBGUIMSGKI3EKNCUKI2DIQ2YGZKUCU2GG5HFMQSBGRDEYQKLGNFVIQ2TGZEVCRSDGZCFONCUKZKEIR2EIM3DMS2ZGJBVMNSJJVEVQWCJJE2DMRKZKE2VGWKSIYZDOSCVIJGFMUCILBDEC7COIE" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/train/JQDLQXTHBA77T535BXXDEHN72Q | json

METRICS of model:
curl -X GET -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/models/<MODEL_ID>

curl -X GET -H "Authorization: Bearer KBCU4U2ZJ43UURZWIJAU6T2BLBGUIMSGKI3EKNCUKI2DIQ2YGZKUCU2GG5HFMQSBGRDEYQKLGNFVIQ2TGZEVCRSDGZCFONCUKZKEIR2EIM3DMS2ZGJBVMNSJJVEVQWCJJE2DMRKZKE2VGWKSIYZDOSCVIJGFMUCILBDEC7COIE" -H "Cache-Control: no-cache" https://api.einstein.ai/v2/vision/models/TW2DN6VIJB2SMRQ7WG5Y2HFEZY | json

CLASSIFY an image:
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "sampleLocation=http://einstein.ai/images/546212389.jpg" -F "modelId=<YOUR_MODEL_ID>" https://api.einstein.ai/v2/vision/predict

curl -X POST -H "Authorization: Bearer KBCU4U2ZJ43UURZWIJAU6T2BLBGUIMSGKI3EKNCUKI2DIQ2YGZKUCU2GG5HFMQSBGRDEYQKLGNFVIQ2TGZEVCRSDGZCFONCUKZKEIR2EIM3DMS2ZGJBVMNSJJVEVQWCJJE2DMRKZKE2VGWKSIYZDOSCVIJGFMUCILBDEC7COIE" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "sampleContent=@C:\Users\vlcol\OneDrive\Desktop\AML-Commercial-Model-Robustness\pics\resnet\bia\bullMastiff_0.1.png" -F "modelId=TW2DN6VIJB2SMRQ7WG5Y2HFEZY" https://api.einstein.ai/v2/vision/predict | json
