import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
import facebook
import vk


# Facebook API

'''
graph = facebook.GraphAPI(access_token="", version="2.11")

friends = graph.get_all_connections(id='me', connection_name='friends')
print(friends)
for friend in friends:
     print(friend)
'''

'''
myToken = 'EAACEdEose0cBAJvE9he5LQiZAg4ZAwni0fbib5NWneSGag85c4Vm6U3k5uLAGwsjC7ZB2xehWGjzedk7ZBSfg1LB9xZAdPZCxQ4y9hvPNBH9kj2xDDuGPhU2kLqCtx34uCZANKcaZAdxWPMJWcnjYSgeydzj8HA3NGZAOav5mLZCuZB8iuhVYh1JqUueJJ5Y54KgGwZD'
url1 = 'https://graph.facebook.com/v2.11/100009063552861'
head = {'Authorization': 'token {}'.format(myToken)}
print(head)
response = requests.get(url1, headers=head)

print(response.headers)
print(response)
'''

'''
graph = facebook.GraphAPI(access_token="EAACEdEose0cBAJwT0VgdSakVE6ykQYZAl3BIuVw2pse5TJWVDNuPCwERKp2t6c5YjB58yGANmGoLAWUuGZBaU3P8OLsM9ZAVL9eKtwTyuj83NiAXhNH8mNDFP7ZAsVnkDRmtryCyCqoAG6qiih0TJXetp0PC44LIwTKec0onRlQKvK8OyZAvNm286TpTKZB931Wk74b8rWs2RHLkzWXhZBP", version="2.8")
friends = graph.get_object("/me/friends")
print(friends)
for friend in friends['data']:
    print("{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id']))
'''

# VK API

session = vk.Session()
api = vk.API(session)
res1 = api.users.get(user_ids=1695846)
print(res1)
res2 = api.friends.get(user_id=1695846)
print(res2)

for elem in res2:
    print(api.users.get(user_ids=elem, fields="bdate"))
