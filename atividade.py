def mult(x,y):
    if y == 1:
        return x
    else:   
        return y + mult(y,x-1)
    
x,y = input().split()
x = int(x)
y = int(y)

print(mult(x,y))
