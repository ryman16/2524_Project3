#! /usr/bin/python

print "Welcome to HANGMAN"
word_list = ['linux', 'fedora', 'engineering', 'UNIX', 'Thompson', 'Ritchie', 'programming', 'bash', 'script', 'shell'];
import random;
word = word_list[random.randrange(0,10,1)];
print word;


