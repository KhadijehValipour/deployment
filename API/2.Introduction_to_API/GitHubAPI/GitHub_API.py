import requests

payload={}
headers={}

def get_followes_following_count(github_username):
    url = f'https://api.github.com/users/{github_username}'
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        followers_count = data['followers']
        following_count = data['following']
        return followers_count , following_count
    else:
        return 0
    
github_username = 'KhadijehValipour'

followers , following = get_followes_following_count(github_username)

print(f"{github_username} has {followers} followers and is following {following}.")




