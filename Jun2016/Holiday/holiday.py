while True:
    try:
        string = raw_input().split()
        people = int(string[0])
        money = int(string[1])
        cases = int(string[2])
        weeks = int(string[3])
        # One more than the max possible cost
        totalCost = 2000001
        room = False
        enoughMoney = False
        hostelFound = False
        for i in range(cases):  
            cost = int(raw_input())
            if people*cost <= money:
                enoughMoney = True
            availability = raw_input().split()
            for j in range(weeks):
                if int(availability[j]) >= people:
                    room = True
            if enoughMoney and room:
                hostelFound = True
            if  enoughMoney and room and people*cost < totalCost:
                totalCost = people*cost
            room = False
            enoughMoney = False 
        if hostelFound:
            print totalCost
        else:
            print 'stay home'

    except:
        break
