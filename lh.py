import networkx as nx
import random 
import matplotlib.pyplot as plt

size =10
iterations = 1000000
G=nx.complete_graph(size)

def checkIfBalanced(G, a, b, c):
    countPos = 0
    if G[a][b]["weight"]:
        countPos += 1
    if G[a][c]["weight"]:
        countPos += 1
    if G[b][c]["weight"]:
        countPos += 1
    if countPos == 1 or countPos == 3:
        return True
    return False

def countBalanced(G):
    total = 0
    bal = 0
    for i in range(0,size):
        for j in range(i+1,size):
            for k in range(j+1,size):
                if checkIfBalanced(G,i,j,k):
                    bal += 1
                total += 1 
    return bal,total

avg = [0] * iterations

for k in range (1,100):
    # true = + 
    # false = - 
    # set up graph
    for (a,b) in G.edges:
        ran = random.randint(0,1)
        if ran == 1:
            G[a][b]["weight"] = True
        else:
            G[a][b]["weight"] = False
    # print(countBalanced(G))

    finishFlag = False 
    prevBalCount = countBalanced(G)[0]
    for i in range (0,iterations):
        randNodes = random.sample(range(0,size),3)
        count = 0
        if not checkIfBalanced(G, randNodes[0],randNodes[1],randNodes[2]):
            randEdge = random.sample(range(0,3),2)
            n1 = randNodes[randEdge[0]]
            n2 = randNodes[randEdge[1]]
            G[n1][n2]["weight"] = not (G[n1][n2]["weight"]) 
            count = countBalanced(G)[0]
        else:
            count = prevBalCount
        prevBalCount= count
        avgCount = count / 120
        avg[i] = (avg[i] + ( (avgCount - avg[i])/ k))
        if (count == 120):
            if k == 1:
                for num in range(0, len(avg)):
                    if avg[num] == 0:
                        avg[num] = 1
            break

        
        print("Interation: "+ str(k)+ "/100    Cycle: "+ str(i)+"/1000000", end="\r", flush=True)

    

# print(avg)  
# plt.xscale('log')
# plt.xticks([1,10,100,1000,10000,100000,1000000])
plt.semilogx(avg)
plt.savefig('avg.png')