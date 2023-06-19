def bubbleSort(estrutura):
    for i in range(0, len(estrutura)):
        for j in range(0, i):
            if estrutura[i]< estrutura[j]:
                temp = estrutura[i]
                estrutura[i] = estrutura[j]
                estrutura[j] = temp
est = [2,3,5,8,4,6,1,7]
print(est)
bubbleSort(est)
print(est)