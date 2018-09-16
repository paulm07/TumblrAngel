import sched, time, threading
import pytumblr
import TumblrAngelAnalyzer as sentiment
import alert
from nested_lookup import nested_lookup

class Analyzer(object):
	userData = []
	done_analyzing = False
	current_status = "neu"
	blogToWatch = ''
	client = ""
	CHECKING_INTERVAL = 15
	POST_THRESHOLD = 3
	
	def __init__(self, blogToWatch):
		self.userData = []
		self.done_analyzing = False
		self.current_status = "neu"
		self.blogToWatch = blogToWatch
		self.client = pytumblr.TumblrRestClient(
		  '4ZWlBQ09MpXd0sJElHtCrgKfrzkq4cnLsKGYOuFsyRA7n2yvev',
		  'VV65lUa7NPk2vIhYbwTKpNFtCDa74CZj0YkOPY91OBfZB2aXwY',
		  'l8KeEdg8V7jTJeAMtIpQvuXMGYg9YWO2BU3fLNyedRwjvvpxoX',
		  'AdxaT3RrXFyOQdDoYcqk36FCigrM1iFXaFWcECYEXxTC5I3WMQ'
		)
		
	# Returns the current sentiment of the last three posts of a tumblr account
	def getBlogDetails(self):

		data = self.client.posts(self.blogToWatch + '.tumblr.com', limit=self.POST_THRESHOLD, filter='text')

		working_data = []
		#print(data)
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
		
		return " ".join(working_data)
		
	# Gets the status of the
	def updateStatus(self):
		starttime=time.time()
		try:
			while(True):
				self.current_status = sentiment.getSentiment(self.getBlogDetails())
				if self.current_status == 'neg':
					alertUser(self.blogToWatch)
					break
				else:
					time.sleep(CHECKING_INTERVAL - ((time.time() - starttime) % CHECKING_INTERVAL))
		except KeyboardInterrupt:
			quit()
		
	def start(self):
		t = threading.Thread(target=self.updateStatus)
		t.start()
		
