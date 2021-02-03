import os

def encodeInv(FileIn, FileOut):
    inFile = open(FileIn, 'r')
    text = inFile.read()
    dictonry = {text[len(text)-1]: '1'}
    encoded = open(FileOut, 'w')
    encoded.write('0' + text[len(text)-1])
    text = text[0:len(text)-1]
    x = ""
    code = 2
    for i in range (len(text)-1, -1, -1):
        x += text[i]
        if x not in dictonry:
            dictonry[x] = str(code)
            if len(x) == 1:
                encoded.write('0' + x)
            else:
                encoded.write(dictonry[x[0:-1]] + x[-1])
            code += 1
            x = ''
    inFile.close()
    encoded.close()
    return True


def decodeInv(FileIn, FileOut):
    codedFile = open(FileIn, 'r')
    decodedFile = open(FileOut, 'w')
    text = codedFile.read()
    dictonry = {'0': '', '1': text[1]}
    decodedFile.write(dictonry['1'])
    text = text[2:]
    x = ''
    code = 2
    for e in text:
        if e in '1234567890':
            x += e
        else:
            dictonry[str(code)] = dictonry[x] + e
            decodedFile.write(dictonry[x] + e)
            x = ''
            code += 1
    codedFile.close()
    decodedFile.close()


def compare(input1, input2):
  originalFile = open(input1, 'r')
  decodedFile = open(input2, 'r')
  originalText = originalFile.read()
  decodedText = decodedFile.read()
  if(originalText == decodedText):
    print("The files are identical, the compression was lossless")
  else:
    print("Files are not identical, the compression was lossy")
  originalFile.close()
  decodedFile.close()

def calculateCompressionRatio(inputFile, encodedFile):
    inputFileSize = os.stat(inputFile).st_size
    encodedFileSize = os.stat(encodedFile).st_size
    return float(encodedFileSize/inputFileSize)

def reverseText():
    f = open("inverseResults\\temp.txt", "r")
    s = f.read()
    f.close()
    f = open("inverseResults\\decodedInv.txt", "w")
    f.write(s[::-1])
    f.close()

encodeInv('input.txt', 'inverseResults\\encodedInv.txt')
decodeInv('inverseResults\\encodedInv.txt', 'inverseResults\\temp.txt')
reverseText()
compare('input.txt', 'inverseResults\\decodedInv.txt')
print(calculateCompressionRatio('input.txt','inverseResults\\encodedInv.txt'))



