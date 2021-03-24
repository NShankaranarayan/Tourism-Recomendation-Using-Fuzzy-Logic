def distfuzzify(y,i):
    nd=0.0
    md=0.0
    fd=0.0
    x=0.0
#NEAR DISTANCE
    if(y<17.5):
        x=1.0
        nd=x
    elif(17.5<=y) and (y<=20):
        x = (20-y)/(20-17.5)
        nd=x
    elif(y>=20):
        x = 0.0
        nd = x
# MID DISTANCE
    if (30<=y) and (y<=42.5):
        x = (42.5-y)/(42.5-30)
        md=x
    elif (17.5<=y) and (y <= 30):
        x = (y-17.5)/(30-17.5)
        md=x
    elif (y <= 17.5) or (y>=40):
        x = 0
        md=x
# FAR DISTANCE
    if (y >= 42.5):
        x = 1
        fd=x
    elif (40<=y) and (y <= 42.5):
        x = (42.5-y)/(42.5-40)
        fd=x
    elif (y <= 40):
        x = 0
        fd=x
    return (nd, md, fd)



def pricefuzzify(y,i):
    lp=0.0
    mp=0.0
    hp=0.0
    x=0.0
#LOW PRICE
    if(y<10.0):
        x=1.0
        lp=x
    elif(10.0<=y) and (y<=15.00):
        x = (15.00-y)/(15.0-10.0)
        lp=x
    elif(y>15.0):
        x = 0.0
        lp = x
# MID PRICE
    if (32.5<=y) and (y<=55.0):
        x = (55.0-y)/(55.0-32.5)
        mp=x
    elif (10.0<=y) and (y <= 32.5):
        x = (y-10.0)/(32.5-10.0)
        mp=x
    elif (y <= 10.0) or (y>=55.0):
        x = 0
        mp=x
# FAR PRICE
    if (y >= 55.5):
        x = 1
        hp=x
    elif (50.00<=y) and (y <= 55.00):
        x = (42.5-y)/(42.5-40)
        hp=x
    elif (y <= 50.00):
        x = 0
        hp=x
    return (lp, mp, hp)

#TIME
def timefuzzify(y,i):
    ft=0.0
    mt=0.0
    lt=0.0
    x=0.0
#FAST TIME
    if(y<=20):
        x=1.0
        ft=x
    elif(20<=y) and (y<=30):
        x = (20-y)/(30-20)
        ft=x
    elif(y>=30):
        x = 0
        ft = x
# MID TIME
    if (60<=y) and (y<=100):
        x = (100-y)/(100-60)
        mt=x
    elif (20.0<=y) and (y <= 60):
        x = (y-20.0)/(60-20.0)
        mt=x
    elif (y <= 20.0) or (y>=100.0):
        x = 0
        mt=x
# HIGH TIME
    if (y >= 100):
        x = 1
        ht=x
    elif (90.00<=y) and (y <= 100):
        x = (100-y)/(100-90)
        ht=x
    elif (y <= 90.00):
        x = 0
        ht=x
    return (ft, mt, ht)
