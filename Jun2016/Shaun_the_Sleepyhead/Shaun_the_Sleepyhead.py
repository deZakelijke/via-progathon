while True:
        data  = raw_input().split()
        distance = int(data[0]) 
        if distance == 0:
            break    
        walkDistance = int(data[1])
        backDistance = int(data[2])
        sleepFactor = int(data[3])
        speedLoss = walkDistance*sleepFactor/100.0
        days = 0
        madeIt = False
        distanceMoved = 0
        while walkDistance > 0:
            distanceMoved += walkDistance
            distanceMoved -= backDistance
            walkDistance -= speedLoss
            if distanceMoved >= distance:
                madeIt = True
                break
            days +=1
            if distanceMoved < 0:
                break


        if madeIt:
            print 'succes on day ', days
        else:
            print 'failure on day ', days
                


            

            
            
