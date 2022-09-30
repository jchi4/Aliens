import requests
import requests.auth
import pandas as pd
#from credential import USERNAME, PASSWORD

def getReddit():
    CLIENT_ID = 'eyNPIVBIOP64T1QV0ad4WA'
    CLIENT_SECRET = 'CSMcydF5VfBfZ4jjW58GjYJuS4OkPA'

    # Step 1. Getting Authentication Information
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    #post_data = {'grant_type': 'password', 'username': USERNAME, 'password': PASSWORD}
    post_data = {'grant_type': 'password', 'username': 'Fearofdirtybandaids', 'password': '(yd_MX@dQ.t4Fyi'}
    headers = {
        'User-Agent': 'Automation script 1.1 by James'
    }

    # Step 2. Getting Token Access ID
    TOKEN_ACCESS_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'
    response = requests.post(TOKEN_ACCESS_ENDPOINT, data=post_data, headers=headers, auth=client_auth)
    if response.status_code == 200:
        token_id = response.json()['access_token']

    # Step 3. Use Reddit's REST API to perform listings
    OAUTH_ENDPOINT = 'https://oauth.reddit.com'
    params_get = {
        'limit': 31 #getting a total of 30 posts
    }
    headers_get = {
        'User-Agent': 'Automation script 1.1 by James',
        'Authorization': 'Bearer ' + token_id
    }
    response2 = requests.get(OAUTH_ENDPOINT + '/r/aliens/hot/', headers=headers_get, params=params_get)
    data = response2.json()

    # Using pandas for better visibility
    df = pd.DataFrame()

    for post in response2.json()['data']['children']: #for loop to store the posts into a pandas dataframe
        df = df.append({
            'title': post['data']['title'],
            'selftext': post['data']['selftext'],
            'ups': post['data']['ups'],
            'is_video': post['data']['is_video'],
            'url': post['data']['url']
        }, ignore_index=True)
    return(data)

# response3 = requests.get(OAUTH_ENDPOINT + '/r/area51/top/')
# requests.get(OAUTH_ENDPOINT + '/r/area51/best/')


# auth = requests.auth.HTTPBasicAuth(CLIENT, SECRET_KEY)
# #with open('pw.txt', 'r') as f:
#     #pw = f.read()
# data = {
#     'grant_type': 'password',
#     'username': 'Fearofdirtybandaids',
#     'password': '(yd_MX@dQ.t4Fyi'
#     }
# headers = {'User-Agent': 'MyAPI/0.0.1'}
# res = requests.post('https://www.reddit.com/api/v1/access_token, auth=auth, data=data, headers=headers')
# TOKEN = res.json()['access_token']
# headers['Authorization'] = f'bearer {TOKEN}'
#
# #requests.get('https://oauth.reddit.com/api/v1/me', headers={User-Agent': 'MyAPI/0.0.1'})
# requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()