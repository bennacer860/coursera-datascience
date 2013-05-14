import sys
import json



def parseTweetFile(tweet_file):
	tweet_file = open(tweet_file)
	tweets = [ ]
	for tweet in tweet_file.readlines():
		tweet = json.loads(tweet)
		# print tweet["text"].encode("utf-8")
		try:
			tweets.append(tweet["text"].encode("utf-8"))
		except:
		    print "Unexpected error:", sys.exc_info()[0]
	tweet_file.close()	    
	return tweets	    
		


def count_frequency(tweets):
	word_count = {}
	frequency = {}
	total_number_of_terms = 0.0
		
	for tweet in tweets:
		words = tweet.split()
		for word in words:
			#increment the total
			total_number_of_terms += 1.0	
			if word in word_count.keys():
				word_count[word] += 1.0
			else:
				word_count[word] = 1.0	
	
	for key in word_count.keys():
		frequency[key] = word_count[key] / total_number_of_terms 
	return frequency




def main():
	tweet_file = sys.argv[1]
	tweets = parseTweetFile(tweet_file)
	terms = count_frequency(tweets)
	for key in terms:
		print key,terms[key]

if __name__ == '__main__':
    main()
