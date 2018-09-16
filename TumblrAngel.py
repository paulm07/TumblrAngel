import pytumblr
import json
from nested_lookup import nested_lookup

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  '4ZWlBQ09MpXd0sJElHtCrgKfrzkq4cnLsKGYOuFsyRA7n2yvev',
  'VV65lUa7NPk2vIhYbwTKpNFtCDa74CZj0YkOPY91OBfZB2aXwY',
  'l8KeEdg8V7jTJeAMtIpQvuXMGYg9YWO2BU3fLNyedRwjvvpxoX',
  'AdxaT3RrXFyOQdDoYcqk36FCigrM1iFXaFWcECYEXxTC5I3WMQ'
)

# Make the request
#print(client.info())

#client.follow('ashley-arue.tumblr.com') # follow a blog

'''
#Create a chat post
chat = """TumblrAngel: @ashley-arue Are you feeling okay?
TumblrAngel: Based on your last post you might not be.
TumblrAngel: If you're feeling any sort of ways please don't be afraid to reach out to someone.
TumblrAngel: Suicide Hotline: 1-888-XXXXX
TumblrAngel: 7cups.com
"""
print(client.create_chat('legendarykittyprince', title="Are You Okay?", state='private', conversation=chat, tags=["Positivity", "ReachingOut"]))
'''

data = client.posts('whatdiditcost-everything.tumblr.com', limit=20, filter='text')

print(nested_lookup('tags', data['posts']))
	
#print(json.dumps(data['posts'], indent=4, sort_keys=True))
