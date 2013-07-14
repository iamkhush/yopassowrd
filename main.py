# Module for generating simple and complex password

import string
import config
import random
from itertools import chain


def main():
	'''
	Main module for generating password.
	'''
	if config.passtype == 'complex':
		key = 'max'			
		password = generate_pass(key)
		return "".join(random.sample(password, config.totallen['max']))
	key = 'min'
	password = generate_pass(key)
	return "".join(password[:config.totallen[key]])


def generate_pass(key):
	'''Generates chained list of strings, taking configurtion settings from config.py.

	Args:
		key: string Either min or max.

	Returns:
		List of strings.
	'''
	return list(
		chain(
				(random.choice(string.uppercase) for _ in range(config.upperlen[key])),
				(random.choice(string.lowercase) for _ in range(config.lowerlen[key])),
				(random.choice(string.digits) for _ in range(config.digitslen[key])),
				(random.choice(string.punctuation) for _ in range(config.punclen[key])),
				(random.choice(string.letters) for _ in range(config.totallen['max']-config.punclen[key])),
		)
	)

print main()
