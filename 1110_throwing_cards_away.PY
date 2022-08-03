while True:
    n = int(input())
    
    if n == 0:
        break
    
    isThrowAray = True
    numbersList = list(range(1,n + 1))
    isThrowArayList = []
    
    throwArayString = ""
    
    while len(isThrowArayList) < n - 1:
        if isThrowAray:
            numberQueue = numbersList.pop(0)
            isThrowArayList.append(numberQueue)
            throwArayString += str(numberQueue)
            throwArayString += ", "
            isThrowAray = False
        else:
            numberQueue = numbersList.pop(0)
            numbersList.append(numberQueue)
            isThrowAray = True
    
    throwArayString = throwArayString[:-2]
    
    print('Discarded cards: ' +throwArayString)
    print('Remaining card:', +numbersList[0])
