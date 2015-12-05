#! /usr/bin/python

print "\n          ~~~Welcome to linux HANGMAN~~~\n"
print "                      --Rules--" 
print "- Secret word is selected at random from a pool of 15"
print "- Possible words are a mixture of unix/linux vocabulary and commands"
print "- Enter one single lower-case letter per guess"
print "- 10 incorrect guesses results in game over"
print "- User will see hint showing word length"
print "- If a correct guess is made, that letter is revealed in hint"

word_list = ['linux', 'fedora', 'kernel', 'unix', 'opensource', 'sudo', 'yum', 'bash', 'script', 'shell', 'root', 'distro', 'ubuntu', 'compiler', 'gnu'];

import random;
word = word_list[random.randrange(0,14,1)];

correct = ['*' for i in word];
txt = '';

for j in range(len(word)):
	txt += str(correct[j]);

tries = 10;
correct_guess = 0;
while tries > 0:
	print "\nIncorrect guesses remaining:", tries;
	print "Secret word: ", txt;	
	guess = raw_input("Guess: ");
	for k in range(len(word)):
		if guess == word[k]:
			correct[k] = guess;
			correct_guess = 1;

	if correct_guess != 1:
		tries = tries - 1;

	txt = '';
	correct_guess = 0;
	for j in range(len(word)):
		txt += str(correct[j]);

	if txt == word:
		tries = -1;
		print "\nCongratulations, you win linux hangman!";

if tries == 0:
	print "\nGAME OVER, you lose."

print "The secret word was:", word;	



