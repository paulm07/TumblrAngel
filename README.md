# TumblrAngel

### Description ###

This application attempts to identify users on Tumblr that might be a danger to themselves or others based on their recent post history.

It attempts to intervene by actively sending a private message to users who fall within this category. It is our understanding that Tumblr already tries to do this by diverting a user who is searching for certain tags or terms to a help page with useful contact information for counseling. This is a passive approach.

Our application takes on a more active approach. It constantly monitors blogs for contextual clues based on the contents of the most recent posts, attempting to extrapolate whether a user is in danger or not.

If the application detects a user is in danger it will send the user a positive message filled with reinforcement and with the same contact information provided by the page already supplied by Tumblr when searching for negative terms.

### Usage ###

Included is a test file with several blogs that are rated either positive or neutral called test.py. Also included is a test file which immediately triggers the messaging system to show off the messaging system's capabilities. The commands below showcase the usage.

$ python test.py

$ python bad_test.py

