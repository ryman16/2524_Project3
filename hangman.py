#! /usr/bin/python

print "Welcome to HANGMAN"
word_list = ['linux', 'fedora', 'engineering', 'unix', 'Thompson', 'Ritchie', 'programming', 'bash', 'script', 'shell'];
import random;
word = word_list[random.randrange(0,10,1)];
correct = ['*' for i in word];
txt = '';

for j in range(len(word)):
	txt += str(correct[j]);

for num in range(1,11):
	print "Try #", num;
	print "Secret word: ", txt;	
	guess = raw_input("Guess: ");
	for k in range(len(word)):
		if guess == word[k]:
			correct[k] = guess;
	txt = '';
	for j in range(len(word)):
		txt += str(correct[j]);	



