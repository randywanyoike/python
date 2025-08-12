
import time



def calculate_sum(n):

    sum =0 
    for numb in range (1,n+1):
        print(f"sum ={sum} , numb={numb}")
        sum=sum+numb
    print(f"For {n} The sum is {sum}")
    return sum

def anotherfun(n):
    sum =0 
    for numb in range (1,n+1):
        print(f"sum ={sum} , numb={numb}")
        sum=sum+numb
    print(f"For {n} The sum is {sum}")
    return sum


    for numb in range(1,20):
        for k in range(3,40):
            print(numb)
            print(k)


def calculate_sum2(n):

    term1=n+1
    term2=n*term1
    sum=term2/2
    print(f"For {n} The sum is {sum}")
    return sum


start_time=time.time()
calculate_sum(2423)
end_time=time.time()
diff=end_time-start_time
print(f"Speed {diff}")