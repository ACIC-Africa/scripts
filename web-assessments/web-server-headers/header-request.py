# import requests module 
import requests 
  
# Making a get request 
response = requests.get('https://www.github.com', verify=False) 
  
# print response 
print(response) 
  
# print headers of response 
print(response.headers) 
