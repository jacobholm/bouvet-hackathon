# Used to concatenate data files generated at mockaroo.com (sql format)

import os

directory = "."
idIterator = 1

with open("ouput.txt", 'w') as outputFile:
    for filename in os.listdir(directory):
        if filename.endswith(".sql"):
            with open(filename, 'r') as inputFile:
                line = inputFile.readline()

                while line:
                    # Find and iterate _id
                    indexStart = line.find("values (") + 8
                    indexEnd = line.find(",", indexStart, indexStart + 5)
                    newLine = "".join((line[:indexStart], str(idIterator), line[indexEnd:]))
                    outputFile.write(newLine)

                    idIterator += 1
                    line = inputFile.readline()