# importing the requests library 
import requests 

for i in range(1, 9):
    server_url = "http://10.1.0.{}/board/5/".format(i)


    data = {'entry':100*i,
            'delete':0 }

    r = requests.post(url = server_url, data = data) 

    print("Sent POST request to :%s"%server_url) 
