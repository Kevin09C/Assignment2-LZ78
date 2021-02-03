import os


def encode(FileIn, FileOut):
    inFile = open(FileIn, 'r')
    encoded = open(FileOut, 'w')
    text = inFile.read()
    dict = {text[0]: '1'}
    encoded.write('0' + text[0])
    text = text[1:]
    combination = ''
    code = 2
    for char in text:
        combination += char
        if combination not in dict:
            dict[combination] = str(code)
            if len(combination) == 1:
                encoded.write('0' + combination)
            else:
                encoded.write(dict[combination[0:-1]] + combination[-1])
            code += 1
            combination = ''
    inFile.close()
    encoded.close()
    return True


def decode(FileIn, FileOut):
    codedFile = open(FileIn, 'r')
    decodedFile = open(FileOut, 'w')
    text = codedFile.read()
    dict = {'0': '', '1': text[1]}
    decodedFile.write(dict['1'])
    text = text[2:]
    comb = ''
    code = 2
    for char in text:
        if char in '1234567890':
            comb += char
        else:
            dict[str(code)] = dict[comb] + char
            decodedFile.write(dict[comb] + char)
            comb = ''
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

encode('input.txt', 'results\\encoded.txt')
decode('results\\encoded.txt', 'results\\decoded.txt')
compare('input.txt', 'results\\decoded.txt')
print(calculateCompressionRatio('input.txt','results\\encoded.txt'))