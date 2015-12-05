#! /usr/bin/python

#ECE2524 Project 3
#written by Ryan Walter, 12/5/15

#print welcome message and game rules
print "\n          ~~~Welcome to linux HANGMAN~~~\n"
print "                      --Rules--" 
print "- Secret word is selected at random from a pool of 15"
print "- Possible words are a mixture of unix/linux vocabulary and commands"
print "- Enter one single lower-case letter per guess"
print "- 10 incorrect guesses results in game over"
print "- User will see hint showing word length"
print "- If a correct guess is made, that letter is revealed in hint"

#list of possible words
word_list = ['linux', 'fedora', 'kernel', 'unix', 'opensource', 'sudo', 'yum', 'bash', 'script', 'shell', 'root', 'distro', 'ubuntu', 'compiler', 'gnu'];

#select random word from list
import random;
word = word_list[random.randrange(0,14,1)];

#create hint
hint = ['*' for i in word];
#string variable used for printing hint
txt = '';

#append hint to blank string
for j in range(len(word)):
	txt += str(hint[j]);

#incorrect guesses remaining
tries = 10;
#indicates correct guess
correct_guess = 0;

#main loop
while tries > 0:
	print "\nIncorrect guesses remaining:", tries;
	print "Secret word: ", txt;
	#user inputs guess	
	guess = raw_input("Guess: ");
	#loop through word to check for match
	for k in range(len(word)):
		if guess == word[k]:
			#correct guess was made, update hint
			hint[k] = guess;
			correct_guess = 1;

	#if wrong guess, decrement tries remaining
	if correct_guess != 1:
		tries = tries - 1;

	#reset correct for next iteration
	correct_guess = 0;
	#copy hint to string
	txt = '';
	for j in range(len(word)):
		txt += str(hint[j]);

	#if string and word match, game is won
	if txt == word:
		tries = -1;
		print "\nCongratulations, you win linux hangman!";

#out of tries, game over
if tries == 0:
	print "\nGAME OVER, you lose."

#display secret word at end of game
print "The secret word was:", word;	



