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

ashley = Analyzer('ashley-arue')
ashley.start()

starttime=time.time()

try:
	while(True):
		#print(ashley.current_status)
except KeyboardInterrupt:
	sys.exit(1)

# FINISH MAIN TEST
