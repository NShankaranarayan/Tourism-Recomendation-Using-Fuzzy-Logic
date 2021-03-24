import math

def distfuzzify(y,i):
    nd=0.0
    md=0.0
    fd=0.0
    x=0.0
    # 50, 100, 150, 200, 250
#NEAR DISTANCE
    if(y<50):
        x=1.0
        nd=x
    elif(50<=y) and (y<=100):
        x = (100-y)/(100-50)
        nd=x
    elif(y>=100):
        x = 0.0
        nd = x
# MID DISTANCE
    if (150<=y) and (y<=250):
        x = 2-math.exp(-((300-y)-150)/150)
        md=x
    elif (50<=y) and (y <= 150):
        x = 2-math.exp(-(y-150)/150)
        md=x
    elif (y <= 50) or (y>=200):
        x = 0
        md=x
# FAR DISTANCE
    if (y >= 250):
        x = 1
        fd=x
    elif (200<=y) and (y <= 250):
        x = (250-y)/(250-200)
        fd=x
    elif (y <= 200):
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
        x = 2-math.exp(-((65-y)-32.5)/33)
        mp=x
    elif (10.0<=y) and (y <= 32.5):
        x = 2-math.exp(-(y-32.5)/33)
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
    ht=0.0
    x=0.0
#FAST TIME
    if(y<=60):
        x=1.0
        ft=x
    elif(60<=y) and (y<=120):
        x = (60-y)/(120-60)
        ft=x
    elif(y>=120):
        x = 0
        ft = x
# MID TIME
    if (180<=y) and (y<=360):
        x = 2-math.exp(-((360-y)-180)/180)
        mt=x
    elif (60<=y) and (y <= 180):
        x = 2-math.exp(-(y-180)/180)
        mt=x
    elif (y <= 60) or (y>=360):
        x = 0
        mt=x
# HIGH TIME
    if (y >= 360):
        x = 1
        ht=x
    elif (300<=y) and (y <= 360):
        x = (360-y)/(360-300)
        ht=x
    elif (y <= 300):
        x = 0
        ht=x
    return (ft, mt, ht)
