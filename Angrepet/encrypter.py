import sys
import random

def process():
	key = ""

	with open(sys.argv[1], 'r') as inputFile:
		with open(sys.argv[2], 'w') as outputFile:
			for line in inputFile:
				for char in line:
					charKey = random.choice('abcdefghijklmnopqrstuvwxyz')
					key += charKey

					mappedChar = mapChar(char, charKey)

					if char.isupper():
						mappedChar = mappedChar.upper()
					else:
						mappedChar = mappedChar.lower()

					outputFile.write(mappedChar)

	print ("Key: " + key)

def mapChar(char, charKey):
	lowerASCII = 65
	upperASCII = 90

	charNr = ord(char.upper())
	charKeyNr = ord(charKey.upper())

	if charNr < lowerASCII or charNr > upperASCII:
		return char

	offset = charKeyNr - charNr

	if charKeyNr < charNr:
		offset = (upperASCII - charNr) + (charKeyNr - lowerASCII) + 1

	encryptedChar = lowerASCII + offset

	return chr(encryptedChar)

process()