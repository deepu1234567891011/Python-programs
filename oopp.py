class patient:
    def __init__(self,name,age,gender,illness,contact_info):
        self.name=name
        self.age=age
        self.gender=gender
        self.illness=illness
        self.contact_info=contact_info
    def display_details(self):#instance method
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"gender:{self.gender}")
        print(f"illness:{self.illness}")
        print(f"contanct:{self.contact_info}")
    @staticmethod
    def show():
        print("Welcome to the patiet class")
class doctor:
    def __init__(self,doctid,doctname,doctage,doctspecilization):
        self.doctid=doctid
        self.doctname=doctname
        self.doctage=doctage
        self.doctspecilization=doctspecilization
    def show(self):#instance method
        print(f"doctid:{self.doctid}")
        print(f"doctname:{self.doctname}")
        print(f"doctage:{self.doctage}")
        print(f"doctorspecilization:{self.doctspecilization}")
    @staticmethod
    def shows():
        print("Welcome to the doctor class")
#object creation
patient.show()#static method called through class name
Patient=patient("srideepika",21,"female","fever",12345678910)
doctor.shows()#static method called through class name
Doctor=doctor(123,"deepu",24,"dental")
Patient.display_details()#instance method call through object name
Doctor.show()#instance method call through object name



    
    