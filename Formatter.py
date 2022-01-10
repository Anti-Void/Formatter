class Formatter:

    def __init__(self, code, formattedCode, codeCharStart, codeCharEnd):
        self.formattedCode = formattedCode
        self.code = code
        self.codeCharStart = codeCharStart
        self.codeCharEnd = codeCharEnd

    def formatCode(self, newCharPos):

        for x in range(len(str(self.code))):
            if x > 0 or x == self.codeCharStart:
                self.formattedCode.append(self.code[self.codeCharStart:self.codeCharEnd])
                self.codeCharStart = self.codeCharStart + newCharPos
                self.codeCharEnd =  self.codeCharEnd  + newCharPos
        return self.formattedCode

    def numberTxt(self, numLines):

        ##Sorts through the block of txt and numbers each line
        for x in range(int(numLines)):
            self.formattedCode.append("(" + str(x + 1) + ")" + self.code[x])
        return self.formattedCode