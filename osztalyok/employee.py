class Employee:
    def __init__(self):
        self.name = "" #privat
        self.city = ""
        self.age = 0
        
        
#majdnem setter        
    def setName(self,name):
        self.name = name
        
    def setCity(self,city):
        self.city = city 
        
    def setAge(self,age):
        self.age = age 
                
sanyi = Employee()
print("_ " + sanyi.name + " _")

sanyi.name = "Sanya"
print("_ " + sanyi.name + " _")

sanyi.setName("Sándor")
print("_ " + sanyi.name + " _")

