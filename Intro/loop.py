to_loop=True
i=0

while to_loop:
    if i>10:
        to_loop=False
    print("i is",i)
    i=i+1


    k=0
    while k<10:
        print("k is", k)
        k=k+1


for i in range(2,10):
    print("For loop is", i)


for i in range(10,2,-1):
    print("For loop is", i) 


for i in range(0,1000,2):
    print("All even numbers", i)
