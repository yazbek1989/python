# sucesion de fibonacci hasta el numero
def fibonacci(limite):
    a,b = 0,1
    fibon = [0]
    for i in range(limite): 
        if b > limite: return fibon
        else: 
            fibon.append(b)
            a,b = b,a+b
    return fibon

print(f"{fibonacci(34)}")
