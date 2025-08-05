#def greet(person1,person2,person3):
 #   print("Name is",person1)
  #  print("Name is",person2)
   # print("Name is",person3)


#greet("Randy", "Earth", "Universe")




#def greet(*args):
#    for arg in args:
 #   print("Name is", arg)

#greet("Randy", "Earth", "Universe", "Galaxy", "Multiverse", "Cosmos")
#greet(123,True,False,None,[1,2,3])





def sum(*args):
    ans=0
    for n in args:
        #print(f"{ans}={ans}+{n}")
        print(ans, "=", ans, "+", n)
        ans=ans+n
        
    print("Ans is ",ans)
    return ans

sum(100,50,20,30,150,200,700)