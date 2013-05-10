import sys
import json


#for each token say how many times it has appeared in the file
def count_word_frequency(tweet_file_name):
	tweet_file = open(tweet_file_name)
	total = count_all_words(tweet_file)
	tweet_file.close
	
	tweet_file = open(tweet_file_name)
	word_frequency= {}
	word_list = tweet_file.read().decode("utf8").split()
	# print text
	for w in word_list:
		word_frequency[w] = word_frequency.get(w,0)+1.0
	
	keys = sorted(word_frequency.keys())
	for word in keys:
		print "%s %f" % (word, word_frequency[word]/total)
	tweet_file.close

#compute the frequency of each token


def count_all_words(tweet_file):
	word_list = tweet_file.read().encode("utf8").split()
	# print word_list
	return len(word_list)

def main():
	tweet_file_name = sys.argv[1]
	count_word_frequency(tweet_file_name)



if __name__ == '__main__':
    main()
