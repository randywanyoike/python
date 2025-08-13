class User():
    def __init__(self,name,email,phone,password,user,discount=0):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.discount=discount
        self.user=user
        self.is_locked=False


    def say_my_name(self):
        print(f"My name is {self.name}")

    def print_details(self):
        print("---------------")
        print("User",self.user)
        print("Name", self.name)
        print("Email", self.email)
        print("Phone", self.phone)
        print("Discount", self.discount)
        print("---------------")
    def login(self):

        if self.is_locked:
            print("Account is locked. Please contact support.")
            return 
        
        for i in range(1,3):
            password=input(f"Enter your password: Attempt{i}")
            if self.password==password:
                print("Login successful")
                return 
        self.is_locked=True
        print("Account locked due to multiple failed attempts. Please contact support.")

        
class Employee(User):
    def __init__(self, name, email, phone, password,salary):
        super().__init__(name=name, email=email, phone=phone, password=password,discount=10,user="employee")
        self.salary=salary

class Customer(User):
    def __init__(self,name,email,phone,password):
        super().__init__(name=name, email=email, phone=phone, password=password,discount= 0,user="customer")



emp1=Employee(name="Randy", email="randy@gmail.com", phone="1234567890", password="randy123", salary=500000)

c1=Customer(name="Alice", email="alice@gmail.com", phone="0987654321", password="alice123")

emp1.say_my_name()
c1.say_my_name()

emp1.print_details()
c1.print_details()

emp1.login()
c1.login()
        