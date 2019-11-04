def Add(arrayOfCharacters, number):
    return [arrayOfCharacters[i] + number for i in range(len(arrayOfCharacters))]

def Sub(arrayOfCharacters, number):
    return [arrayOfCharacters[i] - number for i in range(len(arrayOfCharacters))]

with open("input.txt", "r") as f:
    encrypted = f.read()
    encrypted = [ord(i) for i in encrypted]

encrypted = Sub(encrypted, 2401)
encrypted = Add(encrypted, 1001)
encrypted = Add(encrypted, 1337)

encrypted = [str(j) for j in encrypted]
open("output.txt", "w").write('|'.join(encrypted))