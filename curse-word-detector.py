import urllib.request

def read_text():
	quotes = open("movie_quotes.txt")
	contents_of_file = quotes.read()
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	query = urllib.parse.urlencode({'q': text_to_check})
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + query)
	output = connection.read()
	connection.close()
	if "true" in str(output):
		print("Curse world Alert!!")
	elif "false" in str(output):
		print("This document has no curse words.")
	else:
		print("Could not scan the document properly.")

read_text()
