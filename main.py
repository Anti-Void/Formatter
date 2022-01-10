from Formatter import *
from File import *

##creates a list to store the output of the formatter
formattedCode = []

print("Welcome to the Binary/DNA Code formatter?")
print("type new for a new file or load to load in an existing file")
dec = input()

##Creates a new file from scratch
if(dec.lower() == "new"):

    ##Allows the user to choose between numbering text or formatting binary or DNA Code
    print("Type number to number a block of text or format to format binary or dna code")
    dec = input()

    ##This block of code gets executed if the user chooses the number option
    if(dec.lower() == "number"):
        code = []

        ##Get the name of the file from the user
        print("What would you like the code file to be called?")
        fileName = input()

        ##Get the number of lines the user wants to number
        print("How many lines of text does the block of text have?")
        numLines = input()

        ##Adds each line into an array of strings in order to number the text line by line
        for x in range(int(numLines)):
            print("Type Line " + str(x + 1) + " Of the text file or paste an entire block at once")
            code1 = input()
            code.append(code1[0:len(code1)])

        ##Create the formatter object to number the block of text
        textFormatter = Formatter(code, formattedCode, 0, 0)

        ##Function that adds the numbers to the beginning of each line of text
        formattedCode = textFormatter.numberTxt(numLines)

        ##Create the file object to save the data to
        file = File(fileName, code, formattedCode)

        ##Save the formatted code to a txt file
        status = file.textSaveToFile()

    ##This block of code get's executed if the user chooses the format option
    if(dec.lower() == "format"):

        ##Get the name of the file from the user
        print("What would you like the code file to be called?")
        fileName = input()

        ##Retrieve the data to be formatted from the user
        print("Type Binary or DNA code to format it")
        print("Note: Paste the code on one line and not multiple lines")
        code = input()

        ##Create the file object that the data will be stored in
        file = File(fileName, code, 0)

        ##Determine if the data is either binary or DNA code
        codeType = file.analyzeFile()

        ##If it's DNA code then execute this block of code
        if(codeType == "dna"):

            ##Create the formatter object
            dnaFormatter = Formatter(code, formattedCode, 0, 80)

            ##Format and then store the code inside a variable
            formattedCode = dnaFormatter.formatCode(80)

            ##Print the formatted code in the console
            for x in formattedCode:
                print(x)
            ##Create the file object to store the formatted data
            file = File(fileName, code, formattedCode)

            ##Save the data to the file and then return if it's successful or not
            status = file.dnaSaveToFile()


        ##If the code is binary then execute this block of code
        if(codeType == "binary"):

            ##Create the formatter object
            binaryFormatter = Formatter(code, formattedCode, 0, 8)

            ##Format the binary code and store it inside a variable
            formattedCode = binaryFormatter.formatCode(9)

            ##Print the formatted code in the console
            for x in formattedCode:
                print(x)

            ##Store the formatted code in the file and return if it was successful or not
            file = File(fileName, code, formattedCode)
            status = file.binarySaveToFile()

    ##Prints the state of the saveToFile function in the console
    print(status)

    ##Load in an existing txt file and add to it (Unfinised)
if (dec.lower() == "load"):
    print("Sorry this feature isn't finished yet")

        ##print("Type the name of the file you would like to modify")
        ##fileName = input()
        ##file = File(fileName)
        ##print("Type either Binary or DNA to add the desired code")
        ##code = file.createFile()

        ##if (code == int):
            ##print("hi")


