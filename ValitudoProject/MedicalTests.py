class MedicalTests:

    def __init__(self,docId,patientId,date,description):
        self.docId = docId
        self.patientId = patientId
        self.date = date
        self.description = description

    def __str__(self):
        return "On {}, the Patient with id {} ".format(self.date,self.patientId)


class PatientMedicalHistory:

    def __init__(self,active_illness,family_illness,immunizations,allergies):
        self.active_illness = active_illness
        self.family_illness = family_illness
        self.immunizations = immunizations
        self.allergies = allergies
        
        
    
    def printMedicalHistory(self):
        pass

