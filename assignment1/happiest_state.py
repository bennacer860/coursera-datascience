import sys
import json

def create_sentiment_dict(sentiment_file):
    """ (file) -> (dict)
    Reads the AFINN-111.txt file and creates a sentiment dictionary
    """
    scores = {}
    with open(sentiment_file) as afinnfile:
        for line in afinnfile:
            term, score  = line.split("\t")  # The file is tab-delimited.
            scores[term] = int(score) # Store each term with its integer value
        afinnfile.close()
    return scores

def create_tweet_and_location_list(twitter_stream_file):
    """ (file) -> (list of list) inner lists are: [location, tweet_text]
    Reads a Twitter stream file and returns a list that
    contains the location and text parts of each tweet
    """
    tweet_and_location_list = [] #tall
    with open(twitter_stream_file) as tweetfile:
        for line in tweetfile:
            text = ""
            location = ""
            tweet = json.loads(line) #Convert each tweet from JSON to Dict
            if "user" in tweet.keys():
                location = tweet["user"]["location"] #Get the location, if any
            if "text" in tweet.keys():
                text = tweet["text"] #Get the text of tweet, if any
            tweet_and_location_list.append([location, text])
    return tweet_and_location_list

def find_happiest_state(sentiment_dict, tall):
    """ (list, list) -> (list)
    Given a sentiment dict and a list of tweets, this method computes
    the sentiment value of each tweet
    """
    happiness_score = {}
    for data in tall:
        state = data[0]
        happiness_score[state] = 0.0 #initialize all states with base 0

    for data in tall:
        state = data[0]
        tweet = data[1]
        total_score = 0.0
        words = tweet.split()
        for word in words:
            if word.encode('utf-8') in sentiment_dict.keys():
                total_score += float(sentiment_dict[word])
        happiness_score[state] += total_score

    for key in happiness_score.keys():
        happies_state = ""
        start = 0.0
        if happiness_score[key] > start:
            happiest_state = key
    return happiest_state
    

def main():
    sf = sys.argv[1] #Sentiment File
    tf = sys.argv[2] #Twitter File
    sent_dict = create_sentiment_dict(sf)
    tw_and_loc_lst = create_tweet_and_location_list(tf)
    hs = find_happiest_state(sent_dict, tw_and_loc_lst)
    print hs.encode('utf-8')

if __name__ == '__main__':
    main()