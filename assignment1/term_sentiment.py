import sys
import json
import re


def parseDictionnry( sentiment_file ):
	afinnfile = sentiment_file.readlines()
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = score  # Convert the score to an integerself.
   	return scores

def parseTweetFile(tweet_file):
	tweets = [ ]
	for tweet in tweet_file.readlines():
		tweet = json.loads(tweet)
		# print tweet["text"].encode("utf-8")
		try:
			tweets.append(tweet["text"].encode("utf-8"))
		except:
		    print "Unexpected error:", sys.exc_info()[0]
	return tweets	    
		


def score_all_the_terms(tweets,sentiment_dictionary):
	#store the words and their scores in a dict
	word_scores = {}
	#get the dictionary keys
	keys = sentiment_dictionary.keys()
	
	for tweet in tweets:
		score = 0.0
		words = tweet.split()
		num_of_words = len(words)
		for word in words:
			#if the word is in our sentiment dict
			if word in keys:
				score += float(sentiment_dictionary[word])

		for word in words:
			#if the word is not calculate a score for the new word =score of the tweet / the number of the words in that tweet		
			if word not in keys:
				word_scores[word] =  score/num_of_words
	return word_scores




def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	sentiment_dictionary=parseDictionnry(sent_file)
	tweets = parseTweetFile(tweet_file)
	terms = score_all_the_terms(tweets,sentiment_dictionary)
	for key in terms:
		print key,terms[key]

if __name__ == '__main__':
    main()
