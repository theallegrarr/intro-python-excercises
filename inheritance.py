# Inheritance is the capability of one class to derive 
# or inherit the properties from some another class
class Human: 
  def __init__(self, name, age): 
    self.name = name 
    self.age = age
  def getName(self): 
    return self.name
  def getAge(self):
    return self.age
  def isAlive(self): 
    return False
   
class LivingPerson(Person, name, age):
  def __init__(self, name, age):
    super().__init__(name, age)
  def isAlive(self):
      return f"{self.name} is alive"