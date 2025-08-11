from datetime import datetime

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")
       

class Human():

    species="H.sapiens"
    genus="Homo"
    count=0
    
    def __init__(self,gender,name):
        print("The initializer was called")
        self._gender=gender
        self._name=name
        if self._gender=="Male":
            self._ribs=24
            self._curse="Suffer"
        else :
          self._ribs=23
          self._curse="Pain"
        #Human.count=Human.count+1
        #Human=self.__class__
        self.__class__.count=self.__class__.count+1
    
    @property
    def name(self):
        now = datetime.now()
        print("Current date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} got name from adam")
        return self._name
    
    @name.setter
    def name(self,new_name):
        if not isinstance(new_name,str):
            print("Failed to update name")
            return
        now = datetime.now()
        print("Current date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} Name changed from {self._name} to {new_name}")
        self._name=new_name
        return new_name

    def print_self(self):
        print("----------------------")
        print("name",self._name)
        print("gender",self._gender)
        print("ribs",self._ribs)
        print("curse",self._curse)
        print("---------------------")

    @classmethod
    def get_general_info(cls):
     print("Species", cls.species)
     print("Species",cls.genus)
     print("Species",cls.count)


# adam=Human(name="adam",gender="Male") #object from a class
adam=Human(name="adam",gender="Male")
eve=Human(name="eve",gender="Female")

#adam.print_self2(obj=adam)
#eve.print_self2(obj=eve)

#eve.get_general_info()

Human.get_general_info()
#adam:<HUMAN>-<name and gender -> adam 
#eve<HUMAN> -> name and gender -> eve
# print(adam.__class__)

# print("adam species",adam.species)
# print("eve species",eve.species)
# print("class property",Human.species)

#print("Total humans",Human.count)