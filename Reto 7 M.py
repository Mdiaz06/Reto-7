class Person:
    def __init__(self,name,age,size,hair_color):
        self.name = name
        self.age = age
        self.size =size
        self.hair_color = hair_color
        
    def walk(self,distancia):
        print (f"Soy {self.name} y he recorrido {distancia} de distancia")
        
    def eat(self,food):
        print (f"Soy {self.name} y he comido {food}")
        
    def speak(self,language):
        print (f"Soy {self.name} y hablo {language}")
    
class Student(Person):
    def study(self,subject):
        print (f"Soy {self.name} y estudio {subject}")

class Teacher(Person):
    def teach(self,subject):
        print (f"Soy {self.name} y enseño {subject}")
    
student1=Student("Isabela Bedoya", 20, 1.67, "Castaño claro")
teacher1=Teacher("Andrés Gómez", 40, 1.70, "Negro")


student1.walk(25)
student1.eat("Salchipapa")
student1.speak("Eapañol")
   
teacher1.teach("Expresión gráfica")
teacher1.walk(10)
teacher1.speak("Español")