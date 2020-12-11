# importing the requests library 
import requests 

for i in range(1, 9):
    server_url = "http://10.1.0.{}/board".format(i)


    for j in range(1,6):
        data = {'entry':i*10+j}

        r = requests.post(url = server_url, data = data) 

        print("Sent POST request to :%s"%server_url) 
