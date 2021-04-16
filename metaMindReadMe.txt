These are notes for how Lane implements the dataset imagenette from her own machine.

Get access token from api.einstein.ai/token
Use account email and account .pem file. There is a .pem file in this branch but it 
expires 4/22/2021. 

Token code that expires 4/16/2021 at ~6:00 pm central:
IVAUEN2YK5FE6Q2YIFIVUTKTKU2TEU2VG42VGRSGKBHFINCJKBEESUKSJNHTMUK2II2TMWSDI5KTOVKYGJIUWUCKKI2E6RKBJVNFUN2JIVEFON2ZJBDVCSZVGVGFAMZUJAZUIQ2WKVCFUWBSJRNEQQKPIZFTEV2NI5HES7COIE

Create Dataset:
The following command is not edited:
curl -X POST -H "Authorization: Bearer <TOKEN>" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "type=image" -F "path=https://einstein.ai/images/mountainvsbeach.zip" https://api.einstein.ai/v2/vision/datasets/upload/sync
The following command contains the <TOKEN> and the "path" for the imagenette:
curl -X POST -H "Authorization: Bearer IVAUEN2YK5FE6Q2YIFIVUTKTKU2TEU2VG42VGRSGKBHFINCJKBEESUKSJNHTMUK2II2TMWSDI5KTOVKYGJIUWUCKKI2E6RKBJVNFUN2JIVEFON2ZJBDVCSZVGVGFAMZUJAZUIQ2WKVCFUWBSJRNEQQKPIZFTEV2NI5HES7COIE" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data" -F "type=image" -F "path=C:\Users\vlcol\OneDrive\Desktop\train.zip" https://api.einstein.ai/v2/vision/datasets/upload/sync

NOTE: The path must be a public URL and so a .zip file was uploaded onto the Salesforce files page.
public link that will expire with the account: https://olemiss5.my.salesforce.com/sfc/p/5Y0000025uED/a/5Y0000019OPf/ccGb91dOHQQp6viJR2KxmMfN5k5WcEp556p.zu9OAUI
