import sys
import json


def parseDictionnry( sentiment_file ):
	afinnfile = sentiment_file.readlines()
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = score  # Convert the score to an integerself.
   	return scores

def score_tweet ( scores,text ):
	score = 0.0
	newTerms = []
	text = text.encode('utf-8')
	words = text.split()
	#go through each word in text and add the score to score
	for word in words:
		# print word
		if word in scores:
			score = score+int(scores[word])
		else:
			newTerms.append(word)
	
	for	term in newTerms:
		print term+" "+str(score/len(words))		



def score_all_the_tweets(tweet_file,sentiment_dictionary):
	tweet_file = tweet_file.readlines()
	for tweet in tweet_file:
		tweet=json.loads(tweet)
		if "text" in tweet.keys():
			print score_tweet(sentiment_dictionary,tweet["text"])


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_dictionary=parseDictionnry(sent_file)
    score_all_the_tweets(tweet_file,sentiment_dictionary)


if __name__ == '__main__':
    main()
