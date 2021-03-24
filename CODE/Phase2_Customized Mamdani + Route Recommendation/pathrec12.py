import sys

x = 9999 #infiniity
d={"Guwahati":0,"Kaziranga National Park":1,"Majuli":2,"Manas National Park":3,"Dibrugarh":4,"Dibru Saikhowa National Park":5,"Barpeta":6,"Hajo":7,"Mayong":8,"Pobitora Wildlife sanctuary":9}
#dummy path  --> Try to use google map api to get this value ~shank
G = [[0,198,341,138,447,x,96,36,43,48],
     [198,0,166,270,274,x,273,194,124,125],
     [341,166,0,443,157,x,445,381,301,356],
     [138,270,443,0,576,x,51,91,172,176],
     [447,274,157,576,0,x,537,477,397,399],
     [x,x,x,x,x,0,x,x,x,x],
     [96,273,445,51,537,x,0,60,130,135],
     [36,194,381,172,397,x,60,0,70,74],
     [43,124,301,172,397,x,130,70,0,5],
     [48,125,356,176,399,x,135,74,5,0]]

def printGraph(G):
    for row in G:
        print(row)


def FloydWarshall(p, nr,show=0):
    global k
    assert len(G) == len(G[0])
    #M = G
    n = len(p[0])
    for k in range(n):
        if show:
            print('k=%d' % (k-1))
            printGraph(p)
            print('-'*10)
        for i in range(nr):
            for j in range(n):
                p[i][j] = min([p[i][j], p[i][k]+p[k][j]])
    print("APSP (k=%d):" % k)
    printGraph(p)
    return p
ind =[]
def Pathrecomend(ln):
    for k in range(len(ln)):
        ind.append(d[ln[k]])
    print(ind)
   # l=[]
    #for k in ind:
     #   for j in range(0, 10):
      #      l.append(G[k][j])
    p = [[0 for x in range(len(ind))] for y in range(len(ind))]
    print(p)
    k = 0
    for i in range(len(ind)):
        for j in range(len(ind)):
            p[i][j] = G[ind[i]][ind[j]]
            k = k + 1
    print(p)

    FloydWarshall(p,len(ind),1)
    print("----------------------------------------------------------")
    output=[0]
    i=0
    k=0
    n=len(p[0])
    print(ind[0],end="---->")
    visited=[0 for i in range(n)]
    for i in range(n-1):
        l = p[k]
        visited[k]=1
        mi=9999
        for j in range(len(l)):
            if l[j]!= 0 and visited[j]==0:
                 if mi>l[j]:
                     mi=l[j]
        k=l.index(mi)
        output.append(k)
        print(ind[k],end="---->")
    print("\n")
    key_list = list(d.keys())
    val_list = list(d.values())
    for z in range(len(output)):
         position = val_list.index(ind[output[z]])
         print(key_list[position],end="---->")
    print("\n")

#for k in range(n):

