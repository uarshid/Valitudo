import sqlite3
from MedicalTests import MedicalTests # IN this line I am importing the MedicalTests class, from the MedicalTests.py file
from MedicalTests import PatientMedicalHistory

connection = sqlite3.connect(':memory:')

con = connection.cursor()

con.execute("""CREATE TABLE medicalTests (
            doc_id integer FORIEGN KEY ,
            patient_id integer FORIEGN KEY,
            date text NOT NULL,
            description text NOT NULL
)""")

#change name of family illness column o family condition
con.execute("""CREATE TABLE patientMedicalHistory (
              patient_id integer FORIEGN KEY,
              active_illness text NOT NULL,
              family_illness text NOT NULL,
              immunizations text NOT NULL,
              allergies text NOT NULL
 )""")

#this function inserts the attributes of a medical test object, The parameter is an object and I insert the relevant attribtues
def insert_medicalTest(med_tests,):
    # the with is a context manager so you dont have to keep commiting
    with connection:
        con.execute("INSERT INTO medicalTests VALUES (:doc_id, :patient_id, :date, :description)", (med_tests.docId,med_tests.patientId, med_tests.date, med_tests.description))


def getallMedicalTests():
    with connection:
        con.execute("SELECT * from medicalTests")
        return con.fetchall()

#function to get the medical tests by patient_id
def getAllMedicalTestsbyPatientID(med_tests):
    with connection:
        con.execute("SELECT * from medicalTests WHERE patient_Id =:patient_Id", {'patient_Id': med_tests.patientId})
        return con.fetchall()

#this function deletes a medical test tuple, given the id, the parameter is the patient_id
def deleteMedicalTestbyPatientID(patient):
    with connection:
        con.execute("DELETE from medicalTests WHERE patient_Id =:patient_Id", {'patient_Id': patient.id})



def insertpatientMedicalHistory(patient_his,patient):
    with connection:
        con.execute("INSERT INTO patientMedicalHistory VALUES (:patient_id, :active_illness, :family_illness, :immunizations ,:allergies) ",
        (patient, patient_his.active_illness, patient_his.family_illness, patient_his.immunizations, patient_his.allergies))

def getallMedicalHistories():
    with connection:
        con.execute("SELECT * from patientMedicalHistory")
        return con.fetchall()

def updatePatientIllnessInPatientMedicalHistory(active_illness,patient):
        with connection:
            con.execute('UPDATE patientMedicalHistory SET active_illness = ? WHERE patient_id = ?',(active_illness,patient))
       
    
def updateFamilyIllnessInPatientMedicalHistory(family_illness,patient):
    with connection:
        con.execute('UPDATE patientMedicalHistory SET family_illness = ? WHERE patient_id = ?', (family_illness, patient))

def deleteMedicalHistorybyID(patient):
    with connection:
        con.execute('DELETE FROM patientMedicalHistory WHERE patient_id = ?', (patient,))



#def delte


#functuons for updating allegies, immunizations, more



test_record = MedicalTests(3453,37243,'3/23/2021','Patient Blood Test')

patient_history = PatientMedicalHistory("hello","diabetes and heart disease,","flu and Covid","Deez")

insert_medicalTest(test_record)

insertpatientMedicalHistory(patient_history, 37242322323)

updatePatientIllnessInPatientMedicalHistory('hemorage',37242322323)

updateFamilyIllnessInPatientMedicalHistory('diabeties heart diseases',37242322323)

deleteMedicalHistorybyID(37242322323)

deleteMedicalTestbyPatientID
print(getallMedicalHistories())

#delete funct

#print(test_record)

#print(getallMedicalTests())

#print(getAllMedicalTestsbyPatientID(test_record))

connection.close()
