import argparse
import time
import random

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Typing test', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--words', type=int, default=10, help="Amount of words")
	args = parser.parse_args()

	with open ("wordlist.txt", "r") as myfile:
                wordlist = myfile.read().splitlines()

	wordlist = [word for word in wordlist if word.isalpha()]

	words = random.choices(wordlist, k=args.words)
	print(' '.join(words))

	delay = 0.5
	print("Typing test starts in ", end='', flush=True)
	time.sleep(delay)
	print("3 ", end='', flush=True)
	time.sleep(delay)
	print("2 ", end='', flush=True)
	time.sleep(delay)
	print("1 ", end='', flush=True)
	time.sleep(delay)
	print("Start!", flush=True)
	
	start_time = time.time()
	input_text = input("")
	end_time = time.time()

	input_text = input_text.split(' ')
	
	correct = 0

	for i, word in enumerate(words):
		if i >= len(input_text):
			break
		if word == input_text[i]:
			correct += 1
	
	print(f'{correct/args.words:.2f} accuracy in {end_time - start_time:.4f} seconds at {60*correct/(end_time - start_time):.2f} wpm')

