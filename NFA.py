m = 3
n = 3
#stateMatrix[fromState][toState] = [withValues]
a = [[None for x in range(m)] for y in range(n)]
a[0][0] = [0,1]
a[0][1] = [1]
a[0][2] = [99]
a[1][0] = [99]
a[1][1] = [99]
a[1][2] = [1]
a[2][0] = [99]
a[2][1] = [99]
a[2][2] = [1,0]
i = 0
b=[]
c=[]
stariIntermediare = []
def accepta(Reguli,stInitial,stFinal,sir):
    c = [stInitial]
    for token in sir:
        for v in range(len(c)):
            primul = c[v]
            for i in range(n):
                if Reguli[primul][i].__contains__(token):
                    b.append(i)
        c = b[:]
        stariIntermediare.append(c)
        del b[:]
        #print c
    if c.__contains__(stFinal):
        return True
    else:
        return False
sir = [0,0,1,1,0]
print accepta(a,0,2,sir)
print stariIntermediare
