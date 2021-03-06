class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  
        
# original
#class Professor(Lecturer): 
#    def say(self, stuff): 
#        return self.name + ' says: ' + self.lecture(stuff)

# Problem 6-3      
class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)      

# Problem 6-1
#class ArrogantProfessor(Professor): 
#    def lecture(self, stuff): 
#        return 'It is obvious that ' + Person.say(self,stuff)

        
# Problem 6-2
class ArrogantProfessor(Professor): 
    def lecture(self, stuff): 
        return 'It is obvious that ' + Lecturer.lecture(self,stuff)

        

        
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')
print(e.say('the sky is blue'))
print(le.say('the sky is blue'))
print(le.lecture('the sky is blue'))
print(pe.say('the sky is blue'))
print(pe.lecture('the sky is blue'))
print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))