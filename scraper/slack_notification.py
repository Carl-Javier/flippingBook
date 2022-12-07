import requests 
# link to files.upload method 
url = "https://slack.com/api/files.upload" 
# this is where you add your query string. Please chage token value 
querystring = {"token":"oyER1mn7Zd9qFzg8Xr3Mf9aA"} 
# this is where you define who do you want to send it to. Change channels to your target one 
payload = { "channel":"#test"} 
file_upload = { 
"file":("flipbookDatascopy.csv", 
open("./scraper/file/flipbookDatascopy.csv", 'rb'), 'csv') 
} 
headers = { "Content-Type": "multipart/form-data", } 
response = requests.post(url, data=payload, params=querystring, files=file_upload)