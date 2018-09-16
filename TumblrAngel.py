try:
    import pytumblr
except ImportError:
    sys.exit("""You need pytumblr!
                install it from http://pypi.python.org/pypi/pytumblr
                or run pip install pytumblr.""")
				
try:
    import pytumblr
except ImportError:
    sys.exit("""You need json!
                install it from http://pypi.python.org/pypi/json
                or run pip install json.""")
				
try:
    from nested_lookup import nested_lookup
except ImportError:
    sys.exit("""You need nested_lookup!
                install it from http://pypi.python.org/pypi/nested_lookup
                or run pip install nested_lookup.""")
	
	
from Analyzer import Analyzer
import time, sys



# MAIN TEST

#ashley = Analyzer('ashley-arue')
#ashley.start()

#starttime=time.time()

if len(sys.argv) <= 1:
	print("Error! Invalid number of blogs provided!")
	sys.exit(2)

# Made it this far, need to make blog dictionary
blogs = []

# Keeps all blogs happily in an array
for x in range(1, len(sys.argv)):
	blogs.append(Analyzer(sys.argv[x]))
	
for analyzer in blogs:
	analyzer.start()
	
try:
	while(True):
		continue
except KeyboardInterrupt:
	sys.exit(1)

# FINISH MAIN TEST
