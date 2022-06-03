import requests

def syncAuthorize(login, passwd):
    session = requests.Session()

    link = "https://api.joyreactor.cc/graphql"

    variables = {"query":"mutation Login($login: String!, $password: String!){login(name:$login,password:$password) {me {token}}}",
                    "variables":{"login":login,"password":passwd}}

    header = {"accept": "*/*",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
                "origin":"http://joyreactor.cc",
                "referer": "http://joyreactor.cc/"}

    response = session.post(url=link, json=variables, headers=header)

    if response.status_code == 200:
        if type(response.json().get('data')) == type(None):
            return [None, response.status_code]        
        else:    
            return [response.json().get('data').get('login').get('me').get('token'), response.status_code]
    else:
        return [None, response.status_code]      

