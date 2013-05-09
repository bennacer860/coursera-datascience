import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def parseDictionnry( sentiment_file ):
	afinnfile = sentiment_file.readlines()
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = score  # Convert the score to an integerself.
   	return scores

def score_tweet ( scores,text ):
	score = 0
	#go through each word in text and add the score to score
	for word in text.split():
		# print word
		if word in scores:
			score = score+int(scores[word])
	return score		

def score_all_the_tweets(tweet_file,sentiment_dictionary):
	tweet_file = tweet_file.readlines()
	for tweet in tweet_file:
		tweet=json.loads(tweet)
		if "text" in tweet.keys():
			print score_tweet(sentiment_dictionary,tweet["text"])


def main():
    sent_file = open(sys.argv[1])
    sentiment_dictionary=parseDictionnry(sent_file)
    # print "score tentative"
    tweet_file = open(sys.argv[2])
    score_all_the_tweets(tweet_file,sentiment_dictionary)
    # hw()
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
