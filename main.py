import sys
from LinkedList import *


# This function check if our data is a Real Number
def isfloat(data):
    try:
        float(data)
    except ValueError:
        return False
    return True


# This function checks if our data is a negative Integer
def checkNegative(data):
    if data.find('-') == 0:
        data = data[1:len(data)]
        return checkInt(data)
    return False


# This function checks if our data is an Integer
def checkInt(data):
    if data.isdigit():
        return True
    else:
        return False


# This function ignores truncating decimal as float
# EXAMPLE:- 1234. will not be classified as a float
def checkReal(data):
    if (data.find('.') > 0) and (data.find('.') is not (len(data) - 1)):
        return True
    else:
        return False


argument = sys.argv[1]
argument = argument.split(';')  # splits the argument into list

inputFileName = argument[0]
k = argument[1]
outputFileName = argument[2]

inputFileName = inputFileName[inputFileName.find('=') + 1:len(inputFileName)]
k = k[k.find('=') + 1:len(k)]
k = int(k)
outputFileName = outputFileName[outputFileName.find('=') + 1:len(outputFileName)]

integerList = None
realNumberList = None

try:
    inputFile = open(inputFileName, "r")

    # Splits every line from input file by spaces
    # Then we deal with this data only if it is an Integer or Real Number
    # Then we add it to its respective list
    for line in inputFile:
        check = ""
        counter = 0
        line = line.strip()

        while counter < len(line):
            if line[counter] is not ' ' and line[counter] is not '\t':
                check += line[counter]
            else:
                if checkInt(check) or isfloat(check) or checkNegative(check):
                    if checkReal(check):
                        realNumberList = push(realNumberList, check)
                    if checkInt(check) or checkNegative(check):
                        integerList = push(integerList, check)

                check = ""

            counter += 1

        if check is not " ":
            if checkInt(check) or isfloat(check) or checkNegative(check):
                if checkReal(check):
                    realNumberList = push(realNumberList, check)
                if checkInt(check) or checkNegative(check):
                    integerList = push(integerList, check)
            check = ""

except IOError:
    print(inputFileName, "is not available")
    exit(0)

outputFile = open(outputFileName, "w")

outputFile.write("integer:")
outputFile.write("\n")
traverse(integerList, integerList, k, outputFile, 0)

outputFile.write("real:")
outputFile.write("\n")
traverse(realNumberList, realNumberList, k, outputFile, 0)

outputFile.close()
