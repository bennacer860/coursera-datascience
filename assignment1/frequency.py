import sys
import json

def count_all_words(tweet_file):
	word_frequency= {}
	word_list = tweet_file.read().decode("utf8").split()
	# print text
	for w in word_list:
		word_frequency[w] = word_frequency.get(w,0)+1
	
	keys = sorted(word_frequency.keys())
	for word in keys:
		print "%s %f" % (word, word_frequency[word])

def main():
	tweet_file = open(sys.argv[1])
	# tweet_file.read().decode("utf8").split()
	count_all_words(tweet_file)

if __name__ == '__main__':
    main()
