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

#client.follow('ashley-arue.tumblr.com') # follow a blog

data = client.posts('whatdiditcost-everything.tumblr.com', limit=20, filter='text')

working_data = []

tags = nested_lookup('tags', data['posts'])
bodies = nested_lookup('body', data['posts'])
conversations = nested_lookup('conversation', data['posts'])
dates = nested_lookup('date', data['posts'])

for item in tags:
	for data in item:
		working_data.append(data)
		
for item in bodies:
	working_data.append(item)

for item in conversations:
	working_data.append(item)
	
working_data = list(filter(None, working_data))
	
print(working_data)

#print(json.dumps(data['posts'], indent=4, sort_keys=True))