# Used to concatenate data files generated at mockaroo.com (firebase format)

import os

directory = "."
idIterator = 1

with open("ouput.txt", 'w') as outputFile:
    outputFile.write("{\n")

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(filename, 'r') as inputFile:
                line = inputFile.readline()

                while line:
                    if line == "{\n" or line == "}":
                        line = inputFile.readline()
                        continue

                    # Find and iterate _id
                    indexStart = line.find('"id":') + 5
                    indexEnd = line.find(",", indexStart, indexStart + 5)
                    newLine = "".join((line[:indexStart], str(idIterator), line[indexEnd:]))

                    if idIterator % 1000 == 0:
                        newLine = newLine[0:len(newLine)-1] + ",\n"

                    outputFile.write(newLine)

                    idIterator += 1
                    line = inputFile.readline()
    
    outputFile.write("}")