import requests

def  main():
    response = requests.get("http://www.google.com")
    print ("google.com Status Code: ",response.status_code)

    response = requests.get("https://sso-business2.tele2.nl/")
    print ("arnvi.com Status Code: ",response.status_code)

    response = requests.get("https://mijn.tele2zakelijk.nl")
    print("https://mijn.tele2zakelijk.nl Status Code: ", response.status_code)

if __name__ == "__main__":
    main()
