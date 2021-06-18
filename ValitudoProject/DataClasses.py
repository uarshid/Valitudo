
class Patient:
    def __init__(self,PatientId,firstName,lastName,DateOfBirth,age,gender,address):
        self.PatientId = PatientId
        self.firstName = firstName
        self.lastName = lastName
        self.DateOfBirth = DateOfBirth
        self.age = age
        self.gender = gender
        self.address = address

class Doctor:
    def __init__(self,DoctorId,firstName,lastName,officeNum,age,gender,address,specialty):
        self.DoctorId = DoctorId
        self.firstName = firstName
        self.lastName = lastName
        self.officeNum = officeNum
        self.age = age
        self.gender = gender
        self.address = address
        self.specialty = specialty
        
class Pharmacist:

    def __init__(self,PharmacistId,firstName,lastName,age,gender,pharmacyAddress):
        self.PharmacistId = PharmacistId
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.pharmacyAddress = pharmacyAddress


class MedicalTests:

 def __init__(self,date,time,description):
    self.date = date
    self.time = time
    self.description = description

 def __str__(self):
     return "On {}, the Patient with id {} ".format(self.date,self.patientId)

class Appointments:
    
    def __init__(self,date,time,AppointmentPurpose):
        self.date = date
        self.time = time
        self.AppointmentPurpose = AppointmentPurpose

class Medicine:

    def __init__(self,MedicationName,dataPrescribed):
        self.MedicationName = MedicationName
        self.datePrescribed = dataPrescribed
        
# class PatientMedicalHistory:

#     def __init__(self,active_illness,family_illness,immunizations,allergies):
#         self.active_illness = active_illness
#         self.family_illness = family_illness
#         self.immunizations = immunizations
#         self.allergies = allergies
        
#     def printMedicalHistory(self):
#         pass


