from abc import ABC, abstractmethod
class Person(ABC):
   def __init__(self,name,age):
       self.__name=name
       self.__age=age
   #abstract method:
   @abstractmethod
   def get_role(self):
       pass
   #concrete method
   def getbasicinfo(self):
       return f"name is:{self.__name},age is:{self.__age}"


   def getdetails(self): # complete info(basic+role)
       return f"{self.getbasicinfo()},role is:{self.get_role()}"
# Student class:
class Student(Person):
   def __init__(self,name,age,stuid,course):
       super().__init__(name,age)
       self.__stuid=stuid
       self.__course=course


   def get_role(self):
       return "Student"


   def getstudentinfo(self):
       return f"{self.getdetails()},studentid:{self.__stuid},course name:{self.__course}"
#Professor class


class Professor(Person):
   def __init__(self,name,age,proid,dptname):
       super().__init__(name,age)
       self.__proid=proid
       self.__dptname=dptname
   def get_role(self):
       return "Professor"


   def getprofessorinfo(self):
       return f"{self.getdetails()},proid is:{self.__proid},dpt name is:{self.__dptname}"

class Administration (Person):
   def __init__(self,name,age,admid,dptname):
       super().__init__(name,age)
       self.__admid=admid
       self.__dptname=dptname
   def get_role(self):
       return "Administration"


   def getadministrationinfo(self):
       return f"{self.getdetails()},admid is:{self.__admid},dpt name is:{self.__dptname}"


#university class:


class University:
   universityname="Codegnan"
   def __init__(self):
       self.__people=[]


   # adding people to list
   def addpeople(self,person):
       self.__people.append(person)


   #display people who registered
   def displaypeople(self):
       if not self.__people:
           print("not yet registered")
       else:
           for person in self.__people:
               print(person.getdetails())
   @classmethod
   def getuniversityname(cls):
       return f"University name is:{cls.universityname}"


   @staticmethod
   def welcomemessage():
       return f"Welcome to Codegnan university!"


u=University()
print(u.getuniversityname())
print(u.welcomemessage())


# driver class
while True:
   print("press 1 for Student registration")
   print("press 2 for professor registration")
   print("press 3 for administration registration")
   print("press 4 for display registered people")
   print("press 5 for exit")
   ch=int(input("enter your choice:"))
   if ch==1:
       name=input("enter your name:")
       age=int(input("enter your age:"))
       studentid=int(input("enter your id:"))
       course=input("enter your course name")
       s=Student(name,age,studentid,course)
       u.addpeople(s)
       print("Student registered successfully")
   elif ch==2:
       name = input("enter your name:")
       age = int(input("enter your age:"))
       proid = int(input("enter your id:"))
       deptname = input("enter your dpt name")
       p = Professor(name, age,proid,deptname)
       u.addpeople(p)
       print("Professor registered successfully")
   elif ch==3:
      name=input("enter your name:")
      age = int(input("enter your age:"))
      admid = int(input("enter your id:"))
      deptname = input("enter your dpt name")
      a = Administration(name, age,admid,deptname)
      u.addpeople(a)
      print("Administration registered successfully")
   elif ch==4:
       print("registered people info:")
       u.displaypeople()
   elif ch==5:
       print("Thank you for using this application")
       break
   else:
       print("invalid option")

