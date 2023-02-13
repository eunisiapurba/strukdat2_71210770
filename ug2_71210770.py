import timeit

#fungsi dari iteratif
def blg_prima1(n): 
    x = 1 
    y = 1 
    # print(a,end=" ")
    for y in range(1,n):
        # print(b,end=" ")
        if ((y+1) % 5 == 0):
            print(end="")
        z = y
        y = y+x
        x = z
    
for y in range(1,101):
    start = timeit.default_timer()
    blg_prima1(y)  
    end = timeit.default_timer()
    print("n=",y,"iteratif ->", end-start,"second")
print()

#fungsi rekursif
def blg_prima2(n):
    if n <= 1:
        return n
    else:
        return (blg_prima2(n-1)+blg_prima2(n-2))

for y in range(1,101):
    start = timeit.default_timer()
    blg_prima2(y)  
    end = timeit.default_timer()
    print("n=",y,"rekursif ->", end-start,"second")