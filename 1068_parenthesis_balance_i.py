while True:
    try:
        s = input()
        counter = 0
        for i in s:
            if i == "(":
              counter = counter + 1
            elif i == ")":
              counter = counter - 1
            if counter < 0:
                break
        if(counter == 0):
            print("correct")
        else:
            print("incorrect")
    except (EOFError):
        break