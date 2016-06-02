while True:
    try:
        string = raw_input()
        spaceIndex = string.index(' ')
        print (int(string[0:spaceIndex]) * int(string[spaceIndex:]))-1
    except:
        break   

