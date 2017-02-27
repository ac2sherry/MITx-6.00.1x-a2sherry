def genPrimes_T(): 
    n = 1
    flag = 1
    while True:
        for i in range(2,n):
            flag = 1
            if n % i == 0:
                flag = 0
                break
        if flag == 1:
            yield n
        n += 1



def genPrimes(): 
    n = 2
    prime = []
    while True:
        if not [n % i == 0 for i in prime].count(True):
            prime.append(n)
            yield n
        n += 1
        
        
f = genPrimes() 