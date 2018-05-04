import copy

def get_Lambda(level,price):
    if(level==1):
        price = price-1.322
        if(price >= 0 and price<=0.2):
            top_to_low = 0
        elif(price>0.2 and  price<1.4):
            top_to_low = 0.25*(price-0.2)
        elif(price>=1.4):
            top_to_low = 0.3
        else:
            return "infinity"
        
        if(price<=0.2 and price >= 2):
            top_to_flat = 0
        elif(price>0.2 and price<0.8):
            top_to_flat = (price-0.2)*1
        elif(price>=0.8):
            top_to_flat = 0.6
        else:
            return "infinity"

        return (top_to_flat,top_to_low)

    elif(level==2):
        price = price-0.832
        if(price<=0.1 and price>=0):
            flat_to_low = 0.0
        elif(price>0.1 and price<0.6):
            flat_to_low = 0.8*(price-0.1)
        elif(price>=0.6):
            flat_to_low = 0.8
        else:
            return "infinity"
        
        return float(flat_to_low)

    elif(level==3):
        if(price-0.369<0):
            return "infinity"
        
        return 'no'

def get_Buying_level():
    l = [0.369,0.369,0.369,0.369,0.369,0.369,0.832,0.832,0.832,1.322,1.322,1.322,1.322,1.322,1.322,0.832,0.832,0.832,1.322,1.322,1.322,0.832,0.832,0.369]
    return l

def get_Given_Level(result):
    level = []
    l = copy.deepcopy(result)
    l.sort()
    #print(l)
    upper = (l[15] + l[16]) / 2
    lower = (l[7] + l[8]) / 2
    #print(upper,lower)
    for i in range(24):
        if (result[i]>upper):
            level.append(1)
        elif(result[i]<=upper and result[i]>lower):
            level.append(2)
        elif(result[i]<=lower):
            level.append(3)

    return level

def get_Orginal(level):
    Original = []
    pupil_high = 330/8
    pupil_mid = 454/8
    pupil_low = 212/8
    for i in range(24):
        if(level[i]==1):
            Original.append(pupil_high)
        elif(level[i]==2):
            Original.append(pupil_mid)
        elif(level[i]==3):
            Original.append(pupil_low)

    return Original

def fitness(result):
    '''
    :param result: An array that include 24 hours of prices
    :return: total cost

    highest : 3.2
    lowest : lowest buying cost
    '''
    #print(result)

    quantity = []
    function = 0
    pupil_high = 330
    pupil_med = 454
    pupil_low = 212

    high_bound = 3.2
    #low_bound changes while change

    original_price = []
    #stores the buying price according to each of the hours level


    # 1: top
    # 2: flat
    # 3: low
    constant_W = 15
    # 13.6 = const
    level = get_Given_Level(result)
    level_2 = get_Buying_level()
    #print (level)

    top_to_low = 0
    top_to_flat = 0
    flat_to_low = 0

    for i in range(24):
        a = get_Lambda(level[i],result[i])
        if(a == "no"):
            continue
        elif(type(a)==tuple):
            top_to_low += a[0]
            top_to_flat += a[1]
        elif(type(a)==float):
            flat_to_low += a
        elif(a =="infinity"):
            function = 1000000000

    top = level.count(1)
    flat = level.count(2)
    low = level.count(3)

    #print(top,flat,low)
    flat_to_low /= flat
    top_to_low /= top
    top_to_flat /= flat

    #print("flat_to_low: {0}   top_to_flat: {1}  top_to_low: {2}".format(flat_to_low, top_to_flat, top_to_low))

    Original = get_Orginal(level)
    for i in range(24):
        if(level[i]==1):
            quantity.append(Original[i]- (top_to_flat*pupil_high)/top - (top_to_low*pupil_high)/top)
        elif(level[i]==2):
            quantity.append(Original[i] + (top_to_flat * pupil_high) / flat - (flat_to_low * pupil_med) / flat)
        elif (level[i] == 3):
            quantity.append(Original[i] + (top_to_low * pupil_high) / low + (flat_to_low * pupil_med) / low)

    #print("level:")
    #print(level)
    for i in range(24):
        function += quantity[i]*level_2[i]*constant_W
        
##    print(quantity)
    return 1/function


def getDemand(result):
    '''
    :param result: An array that include 24 hours of prices
    :return: total cost

    highest : 3.2
    lowest : lowest buying cost
    '''
    #print(result)

    quantity = []
    function = 0
    pupil_high = 330
    pupil_med = 454
    pupil_low = 212

    high_bound = 3.2
    #low_bound changes while change

    original_price = []
    #stores the buying price according to each of the hours level


    # 1: top
    # 2: flat
    # 3: low
    constant_W = 15
    # 13.6 = const
    level = get_Given_Level(result)
    level_2 = get_Buying_level()
    #print (level)

    top_to_low = 0
    top_to_flat = 0
    flat_to_low = 0

    for i in range(24):
        a = get_Lambda(level[i],result[i])
        if(a == "no"):
            continue
        elif(type(a)==tuple):
            top_to_low += a[0]
            top_to_flat += a[1]
        elif(type(a)==float):
            flat_to_low += a
        elif(a =="infinity"):
            function = 1000000000

    top = level.count(1)
    flat = level.count(2)
    low = level.count(3)

    #print(top,flat,low)
    flat_to_low /= flat
    top_to_low /= top
    top_to_flat /= flat

    #print("flat_to_low: {0}   top_to_flat: {1}  top_to_low: {2}".format(flat_to_low, top_to_flat, top_to_low))

    Original = get_Orginal(level)
    for i in range(24):
        if(level[i]==1):
            quantity.append(Original[i]- (top_to_flat*pupil_high)/top - (top_to_low*pupil_high)/top)
        elif(level[i]==2):
            quantity.append(Original[i] + (top_to_flat * pupil_high) / flat - (flat_to_low * pupil_med) / flat)
        elif (level[i] == 3):
            quantity.append(Original[i] + (top_to_low * pupil_high) / low + (flat_to_low * pupil_med) / low)

    #print("level:")
    #print(level)
    for i in range(24):
        function += quantity[i]*level_2[i]*constant_W
        
##    print(quantity)
##    print(Original)
    
getDemand([1.593326360932395, 1.395333048693535, 1.5196803480583185, 1.5580291411691218, 1.1383573167070427, 1.6565362798532401, 1.3688948781662404, 2.263969048153723, 2.142583582222681, 2.792604971220557, 2.68761907565876, 2.7529449005312796, 2.7992797286872158, 2.7780030319875384, 2.779322321591551, 1.966650559437774, 1.8104827821820153, 2.262203968234748, 2.796447197421088, 2.788795471121769, 2.124489321152705, 2.137099067197299, 1.8113070585195161, 1.5591370840221854])
