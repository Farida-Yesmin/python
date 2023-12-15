''' Write a program to print your information.'''

class personal_information:
    
    def __init__(self, name, age, address, email):
        self.name = next                #instance variable
        self.age = age
        self.address = address
        self.email= email
        
    def details(self):
        print("Name: {}\nAge: {} Year\nAddress: {}".format(self.name, self.age, self.address))

    def mail(self):
        return("Email:{}".format(self.email))
    
obj = personal_information('Orhan', 1, 'Bangladesh', "orhan@gmail.com")
obj.details()
x = obj.mail()
print(x)
