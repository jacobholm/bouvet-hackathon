def Add(arrayOfCharacters, number):
    return [arrayOfCharacters[i] + number for i in range(len(arrayOfCharacters))]

def Sub(arrayOfCharacters, number):
    return [arrayOfCharacters[i] - number for i in range(len(arrayOfCharacters))]

with open("input.txt", "r") as f:
    document = f.read()
    document = document.split('|')
    document = [int(x.strip()) for x in document] 

document = Sub(document, 1337)
document = Sub(document, 1001)
document = Add(document, 2401)

result = ""
for c in document:
	result += str(chr(c))

open("output.txt", "w").write(result)