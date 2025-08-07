class Human():

     def __init__(self,gender,name):
        print("The initializer wass called")
        
     def learn_self(self,gender,name):
        self.gender=gender
        self.name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"

     def print_self(self):
        print("--------------")
        print("name:",self.name)
        print("gender",self.gender)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("--------------")
    
adam=Human(name="adam",gender="Male") #object from a classprint("name",adam.name)
adam.print_self

eve=Human(name="eve",gender="Female") #object from a class
eve.print_self
#print("name",eve.name)
#print("gender",eve.gender)
#print("ribs",eve.ribs)
#print("curse",eve.curse)

        