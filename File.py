class File:

    def __init__(self, fileName, code, formattedCode):
        self.fileName = fileName
        self.code = code
        self.formattedCode = formattedCode

    def characterCount(self):
        return "Amount of Characters in Code: " + str(len(self.code))

    def createFile(self):
        print("What would you like the code file to be called?")
        self.fileName = input()
        return self.fileName

    def analyzeFile(self):
        for x in range(8):
            if("1" in self.code or "0" in self.code):
                return "binary"
            if("A" in self.code or "C" in self.code):
                return "dna"

    def dnaSaveToFile(self):

        affirmationList = open(self.fileName, 'w+')
        for x in range(len(self.formattedCode)):
            print(self.formattedCode[x])
            affirmationList.write(self.formattedCode[x] + "\n")
        affirmationList.close()
        return "Success"

    def binarySaveToFile(self):
        newLine = 0
        Affirmation_List = open(self.fileName, 'w+')
        for x in range(len(self.formattedCode)):
            if x <= 8 + newLine:
                print(self.formattedCode[x], end=" ")
                Affirmation_List.write(self.formattedCode[x] + " ")
            if x > 8 + newLine:
                print("")
                Affirmation_List.write("\n")
                newLine += 10
        Affirmation_List.close()
        return "success"

    def textSaveToFile(self):

        Affirmation_List = open(self.fileName, 'w+')
        for x in range(len(self.formattedCode)):
            Affirmation_List.write(self.formattedCode[x] + "\n")
        Affirmation_List.close()
        return "success"