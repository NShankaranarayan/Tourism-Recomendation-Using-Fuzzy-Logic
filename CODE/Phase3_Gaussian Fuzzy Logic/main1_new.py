import fuzzifier2_Tu as fz
import pandas as pd
import input as ip
import numpy as np
from tabulate import tabulate
import pathrec12 as p

#initializing data

price = [0,10.0, 40.0, 10.0, 15.0, 0.0, 15.0, 10.0, 10.0, 5.0]
distance = [0,198,341,138,447,9999,96,36,43,48]
time = [0,240,499,184,600,1300,155,66,89,103]

name=['Guwahati','Kaziranga National Park','Majuli','Manas National Park','Dibrugarh','Dibru Saikhowa National Park','Barpeta','Hajo','Mayong','Pobitora Wildlife Sanctuary']

lp1=[]
mp1=[]
hp1=[]
nd1=[]
md1=[]
fd1=[]
ft1=[]
mt1=[]
ht1=[]
ip_price=0
ip_dist=0
ip_time=0

#fuzzify
def startfuzzification():
    for i in range(len(distance)):
        nd,md,fd= fz.distfuzzify(distance[i], i)
        nd1.append(nd)
        md1.append(md)
        fd1.append(fd)
    for i in range(len(price)):
        nd,md,fd= fz.pricefuzzify(price[i], i)
        lp1.append(nd)
        mp1.append(md)
        hp1.append(fd)
    for i in range(len(time)):
        nd,md,fd= fz.timefuzzify(time[i], i)
        ft1.append(nd)
        mt1.append(md)
        ht1.append(fd)

def print_dataframe():
    print("______________________________________")
    print(tabulate(price_list, headers='keys', tablefmt='psql'))
    print("______________________________________")
    print("______________________________________")
    print(tabulate(dist_list, headers = 'keys', tablefmt = 'psql'))
    print("______________________________________")
    print("______________________________________")
    print(tabulate(time_list, headers = 'keys', tablefmt = 'psql'))
    print("______________________________________")

def create_dataframe():
    global price_list
    price_list = pd.DataFrame(
        {'NAME': name,
         'PRICE': price,
         'LOW': lp1,
         'MID': mp1,
         'HIGH': hp1
        })

    global dist_list
    dist_list = pd.DataFrame(
        {'NAME': name,
         'DISTANCE': distance,
         'LOW': nd1,
         'MID': md1,
         'HIGH': fd1
        })

    global time_list
    time_list = pd.DataFrame(
        {'NAME': name,
         'TIME': time,
         'LOW': ft1,
         'MID': mt1,
         'HIGH': ht1
        })

def recomend():
    global maint
    maint = pd.DataFrame(
        {'NAME': name,
         'PRICE': price_list[ip_price],
         'DIST': dist_list[ip_dist],
         'TIME': time_list[ip_time],
         })
    maint['RESULT'] = pd.Series(maint.PRICE+maint.DIST+maint.TIME, index=maint.index)
    print(tabulate(maint, headers = 'keys', tablefmt = 'psql'))
    global s_rec
    s_rec=maint.sort_values(by=['RESULT'],ascending = False)
    print(tabulate(s_rec, headers = 'keys', tablefmt = 'psql'))
    return s_rec

#mamdani fuzzy
ip_price,ip_dist,ip_time=ip.init() #getinput
startfuzzification() #fuzzifying the data
create_dataframe() #creating dataframe to store data
print_dataframe() #print data frame
Rec=recomend() #use the input to generate list of recomendation
l=[]
for i in Rec['NAME']:
    l.append(i)
print(l)
result=p.Pathrecomend(l[:5])

#shortest path
