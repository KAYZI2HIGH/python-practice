class Person:
  def __init__(self, name):
    self.name = name
  def talk(self):
    print(self.name, 'talk')

person = Person('Kayode')
person.talk()