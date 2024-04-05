#Reads the data from the file and returns it.
def GetDataFromFile(messageFile):
    file = open(messageFile, "r")
    listOfData = file.readlines()    
    file.close()
    return listOfData

#Example given key is 1 number, but if key is ever > 9 then it will be 2+ letters.
def GetKeyFromDataLine(line):
    key = ""
    for letter in line:
        if letter == " ":
            return key
        key += letter

def ConvertDataListIntoDictionary(listOfData):
    dictOfDataByKey = {}

    for line in listOfData:
        key = GetKeyFromDataLine(line)
        entry = ""

        #Iteration starts after the space, number of chars in key + 1 as 1 represents space.
        for letterPos in range(len(key) + 1, len(line)):
            letter = line[letterPos]

            #\n indiacates end of word as its a new line (new data entry)
            if letter == '\n':
                #Word complete, add it to dictionary
                dictOfDataByKey.update({int(key):entry})
                break
            
            #If not end of word, update entry with current letter
            entry += letter

    return dictOfDataByKey

def GenerateResponseStringFromDictionary(dictOfDataByKey):
    treeDepth = 1
    dataPosition = 1
    responseMessage = ""

    #Normally wouldn't use "while True", however, exit condition is in the loop.
    while True:        
        data = dictOfDataByKey[dataPosition]        
        responseMessage += data

        #Exit condition - Max depths is number of nodes / 3
        if(treeDepth > len(dictOfDataByKey)/3):
            break
        
        responseMessage += " "
        
        #Rightmost node is always 3 * depth
        dataPosition = 3 * treeDepth
        treeDepth += 1
        
    return responseMessage
    
def Decode(messageFile):
    listOfData = GetDataFromFile(messageFile)
    dictOfDataByKey = ConvertDataListIntoDictionary(listOfData)
    return GenerateResponseStringFromDictionary(dictOfDataByKey)

if __name__ == "__main__":
    print(Decode("data.txt"))
    input()
