def greet(name,nationality):
    print("Name is",name)
    print("From ",nationality)

greet(nationality="India",name="John")



#KWARGS PROFILE
def employee(**kwargs):
    print(kwargs)
    print("Name is", kwargs["name"])
    for key,value in kwargs.items():
        print("For key is", key, "and value is", value)

employee(name="Alice", age=30, position="Engineer", country="USA")
employee(name="Bob", age=25, position="Designer", country="Canada", experience=5)


def do_drink(**kwargs):
    drinks=kwargs["drink"]
    prices=kwargs["price"]

    for index,value in enumerate(drinks):
        print("For index",index)
        print("The Drink",value)
        print("The price",prices[index])


do_drink(drink=["KenyaCane","Best"],
          price=[100,200])





def mixed(*args, **kwargs):
    print("Kwargs", kwargs)
    print("Args", args)
mixed("cool","drinks", name="Alice", age=30, country="USA")



def square_all(*args):
    ans=[]
    for n in args:
        ans.append(n*n)
    print(ans)
    return ans

square_all(2,4,6,1)