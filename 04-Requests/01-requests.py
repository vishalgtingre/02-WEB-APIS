import requests

url = 'https://api-prd.kpn.com/oauth/client_credential/accesstoken'
qryparams = {"grant_type": "client_credentials"}
headers = "{'Content-type': 'application/json', 'Accept': 'text/plain'}"
myobj = {
    "client_id": "bXSpPYGHs8jwSLFFC8vmODZRCN9Jr7in",
    "client_secret": "RnGliA5EF5qhptzJ"
}

def  main():
    
   
    #print ("Headers : ", response.headers)
    #print ("Response text : ", response.text)
    response = requests.post(url,params=qryparams,data=myobj)
    

    print("authrequest : ",response.status_code)
    responsejsondata = response.json() 
    #print(responsejsondata)
    print(responsejsondata["access_token"])

    response = requests.get(
        "https://api-prd.kpn.com/network/kpn/internet-speed-check/offer")
    print("KPN Status Code: ", response.status_code)


if __name__ == "__main__":
    main()
