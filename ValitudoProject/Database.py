import sqlite3
import uuid
import tkinter
from DataClasses import MedicalTests 
#from DataClasses import PatientMedicalHistory
from DataClasses import Patient
from DataClasses import Doctor
from DataClasses import Pharmacist
from DataClasses import *
import pandas as pd 
import os



class Database:
    
    def __init__(self):
        
        self.connection = sqlite3.connect("Valitudo.db")
        self.connection.execute("PRAGMA foreign_keys = 1")
        con = self.connection.cursor()
    #connection = sqlite3.connect(':memory:')

        con.execute("""CREATE TABLE if not exists Patient(
              id integer PRIMARY KEY UNIQUE,
              firstName text NOT NULL,
               lastName text NOT NULL,
               DateOfBirth text NOT NULL,
               age integer NOT NULL,
               gender text NOT NULL,
               address text NOT NULL,
               doctor_id integer,
               pharmacist_id integer,
               FOREIGN KEY (doctor_id) REFERENCES Doctor(id)
        )""")

#Add attribute to patient that is docID
        con.execute("""CREATE TABLE if not exists Doctor (
              id integer PRIMARY KEY UNIQUE,
              firstName text NOT NULL,
               lastName text NOT NULL,
               officeNum integer NOT NULL UNIQUE,
               age integer NOT NULL,
               gender text NOT NULL,
               address text NOT NULL,
               specialty text NOT NULL
        )""")

        con.execute("""CREATE TABLE if not exists Pharmacist (
              id integer PRIMARY KEY UNIQUE,
              firstName text NOT NULL,
               lastName text NOT NULL,
               age integer NOT NULL,
               gender text NOT NULL,
               pharmacyAddress text NOT NULL
        )""")
 
        con.execute("""CREATE TABLE if not exists medicalTests (
            doc_id integer,
            patient_id integer,
            date text NOT NULL,
            time text NOT NULL,
            description text NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patient(id),
            FOREIGN KEY (doc_id) REFERENCES Doctor(id)
            )""")
    

        con.execute("""CREATE TABLE if not exists HereditaryIllness(
                    patient_id integer,
                    illness text NOT NULL,
                    FOREIGN KEY (patient_id) REFERENCES patient(id)
          )""")

        con.execute("""CREATE TABLE if not exists ActiveIllness (
                    patient_id integer,
                    illness text NOT NULL,
                    FOREIGN KEY (patient_id) REFERENCES patient(id)
            )""")

        con.execute("""CREATE TABLE if not exists allergies (
                    patient_id integer,
                    allergy text NOT NULL,
                    FOREIGN KEY (patient_id) REFERENCES patient(id)

            )""")
        
        con.execute("""CREATE TABLE if not exists Appointments (
                patient_id integer,
                doc_id INTEGER,
                date text NOT NULL,
                time text NOT NULL,
                AppointmentPurpose text NOT NULL,
                FOREIGN KEY (doc_id) REFERENCES Doctor(id)
                FOREIGN KEY (patient_id) REFERENCES Patient(id)
            )""")
    
        con.execute("""CREATE TABLE if not exists PrescribedMedicine (
                patient_id integer NOT NULL,
                doc_id integer,
                medicationName text NOT NULL,
                datePrescribed text NOT NULL,
                FOREIGN KEY (patient_id) REFERENCES Patient(id),
                FOREIGN KEY (doc_id) REFERENCES Doctor(id)       
        )""")

       ##Patient Class
    def insertNewPatient(self,patient,doctor,pharmacist):
        con = self.connection.cursor()
        with self.connection:
            con.execute("INSERT INTO Patient VALUES (?,?,?,?,?,?,?,?,?)",(patient.PatientId,patient.firstName,patient.lastName,patient.DateOfBirth,patient.age,patient.gender,patient.address,doctor.DoctorId,pharmacist.PharmacistId))

    def insertNewPatientWithOnlyOtherIDs(self,patient,docId,pharmacistId):
         con = self.connection.cursor()
         with self.connection:
            con.execute("INSERT INTO Patient VALUES (?,?,?,?,?,?,?,?,?)",(patient.PatientId,patient.firstName,patient.lastName,patient.DateOfBirth,patient.age,patient.gender,patient.address,docId,pharmacistId))
    def findPatientbyID(self,patient):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from Patient WHERE id = ?",(patient.PatientId,))
            return con.fetchall()

    def findPatientOnlyID(self,idNum):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from Patient WHERE id = ?",(idNum,))
            return con.fetchall()

    def findAssignedPatientbyDocID(self,docID):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from Patient WHERE doctor_id = ?",(docID,))
            return con.fetchall()
        
    def updatePatientAddress(self,patient,newAddress):
        con = self.connection.cursor()
        with self.connection:
                con.execute("UPDATE Patient SET address = ? WHERE id = ?",(newAddress,patient.PatientId))

    def updatePatientAddressByID(self,newAddress,PatientId):
         con = self.connection.cursor()
         with self.connection:
              con.execute("UPDATE Patient SET address = ? WHERE id = ?",(newAddress,PatientId))

    def updatePatientAgeByID(self,newAge,PatientId):
        con = self.connection.cursor()
        with self.connection:
                con.execute("UPDATE Patient SET age = ? WHERE id = ?",(newAge,PatientId))
    
    def deletePatient(self,patient):
        con = self.connection.cursor()
        with self.connection:
                con.execute("DELETE FROM Patient WHERE id = ?",(patient.PatientId,))

    def getAllPatients(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * FROM Patient ")
            return con.fetchall()

    def printAllPatients(self):
        con = self.connection.cursor()
        with self.connection:
             print(pd.read_sql_query("SELECT * FROM Patient",self.connection))
             

    ##Doctor class queries
    def insertDoctor(self,doctor):
        con = self.connection.cursor()
        with self.connection:
            con.execute("INSERT INTO Doctor VALUES (?,?,?,?,?,?,?,?)",(doctor.DoctorId,doctor.firstName,doctor.lastName,doctor.officeNum,doctor.age,doctor.gender,doctor.address,doctor.specialty))

    def findDoctorbyID(self,doctor):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from Doctor WHERE id = ?",(doctor.DoctorId,))
            return con.fetchall()

    def findDoctorWithSpecificID(self,docid):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from Doctor WHERE id = ?",(docid,))
            return con.fetchall()
    
    def updateDoctorOfficeNum(self,doctor,newOfficeNum):
        con = self.connection.cursor()
        with self.connection:
                con.execute("UPDATE Doctor SET officeNum = ? WHERE id = ?",(newOfficeNum,doctor.DoctorId))

    def updateDoctorAge(self,doctor,newAge):
        con = self.connection.cursor()
        with self.connection:
                con.execute("UPDATE Doctor SET age = ? WHERE id = ?",(newAge,doctor.DoctorId))

    def getAllDoctors(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * FROM Doctor ")
            return con.fetchall()

    def deleteDoctorbyID(self,doctor):
        con = self.connection.cursor()
        with self.connection:
            con.execute("DELETE FROM Doctor WHERE id = ?",(doctor.DoctorId,))
            return con.fetchall()
   
    def printAllDoctors(self):
         con = self.connection.cursor()
         with self.connection:
             print(pd.read_sql_query("SELECT * FROM Doctor",self.connection))
             

    ##Pharmacist
    def insertPharmacist(self,pharmacist):
        con = self.connection.cursor()
        with self.connection:
            con.execute("INSERT INTO Pharmacist VALUES (?,?,?,?,?,?)",(pharmacist.PharmacistId,pharmacist.firstName,pharmacist.lastName,pharmacist.age,pharmacist.gender,pharmacist.pharmacyAddress))

    def findPharmacistByID(self,pharmacist):
         con = self.connection.cursor()
         with self.connection:
            con.execute("SELECT * from Pharmacist WHERE id = ?",(pharmacist.PharmacistId))
            return con.fetchall()

    def updatePharmacyAddressforPharmacist(self,pharmacist,newPharmacyAddress):
            con = self.connection.cursor()
            with self.connection:
                con.execute("UPDATE Pharmacist SET pharmacyAddress = ? WHERE id = ?",(newPharmacyAddress,pharmacist.PharmacistId))

    def getAllPharmacists(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * FROM Pharmacist")
            return con.fetchall()
    
    def deletePharmacistByID(self,pharmacist):
         con = self.connection.cursor()
         with self.connection:
                con.execute("DELETE FROM Pharmacist WHERE id = ?",(pharmacist.PharmacistId,))
    
    def deleteAllPharmacist(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("DELETE FROM Pharmacist")
            return con.fetchall()
    
    def printAllPharmacists(self):
         con = self.connection.cursor()
         with self.connection:
             print(pd.read_sql_query("SELECT * FROM Pharmacist",self.connection))
             
    #appointments
    def insertnewAppointment(self,appointment,patient,doctor):
         con = self.connection.cursor()
         with self.connection:
            con.execute("INSERT INTO Appointments VALUES (?,?,?,?,?)",(patient.PatientId,doctor.DoctorId,appointment.date,appointment.time,appointment.AppointmentPurpose))

    def insertnewAppointWithValues(self,patientID,doctorID,date,time,purpose):
        con = self.connection.cursor()
        with self.connection:
            con.execute("INSERT INTO Appointments VALUES (?,?,?,?,?)",(patientID,doctorID,date,time,purpose))
    
    def chnageAppointment(self,newAppointmentDate,newAppointmentTime,patient):
          con = self.connection.cursor()
          with self.connection:
                con.execute("UPDATE Appointments SET date = ? WHERE patient_id = ?",(newAppointmentDate,patient.PatientId))
                con.execute("UPDATE Appointments SET time = ? WHERE patient_id = ?",(newAppointmentTime,patient.PatientId))
    
    def getPatientAppointments(self,patient):
         con = self.connection.cursor()
         with self.connection:
            con.execute("SELECT * FROM Appointments WHERE patient_id = ?",(patient.PatientId,))
            return con.fetchall()
    
    def getPatientAppointmentsByID(self,patientID):
         con = self.connection.cursor()
         with self.connection:
            con.execute("SELECT * FROM Appointments WHERE patient_id = ?",(patientID,))
            return con.fetchall()

    def getAllAppointments(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * FROM Appointments")
            return con.fetchall()

    def printAllAppointments(self):
       con = self.connection.cursor()
       with self.connection:
             print(pd.read_sql_query("SELECT * FROM Appointments",self.connection))

    def deleteAllAppintments(self):
        con = self.connection.cursor()
        with self.connection:
             con.execute("DELETE FROM Appointments")
             

    def insertRecordIntoMedicalTest(self,medTest,patient,doctor):
    # the with is a context manager so you dont have to keep commiting
         con = self.connection.cursor()
         with self.connection:
            con.execute("INSERT INTO medicalTests Values (?,?,?,?,?)",(doctor.DoctorId,patient.PatientId,medTest.date,medTest.time,medTest.description))

    def updateMedicalTestDateandTime(self,medtest,newDate,newTime,patient):
        con = self.connection.cursor()
        with self.connection:
                con.execute("UPDATE medicalTests SET date = ? WHERE patient_id = ?",(newDate,patient.PatientId))
                con.execute("UPDATE medicalTests SET time = ? WHERE patient_id = ?",(newTime,patient.PatientId))
#get Medical
    def getAllMedicalTestsbyPatientID(self,patient):
         con = self.connection.cursor()
         with self.connection:
            con.execute("SELECT * from medicalTests WHERE patient_Id = ?",(patient.PatientId,))
            return con.fetchall()

    def getAllMedicalTestsbyDoctorID(self,doctor):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from medicalTests WHERE doc_id = ?",(doctor.DoctorId,))
            return con.fetchall()

    def getAllMedicalTests(self):
         con = self.connection.cursor()
         with self.connection:
            con.execute("SELECT * FROM medicalTests")
            return con.fetchall()
    
    def deleteAllMedicalTests(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("DELETE FROM medicalTests")
            return con.fetchall()

    def printAllMedicalTests(self):
         con = self.connection.cursor()
         with self.connection:
             print(pd.read_sql_query("SELECT * FROM medicalTests",self.connection))
    
    #Medicine Query Classes
    def insertPrescribedMedicine(self,medicine,patient,doctor):
       con = self.connection.cursor()
       with self.connection:
            con.execute("INSERT INTO PrescribedMedicine VALUES (?,?,?,?)",(patient.PatientId,doctor.DoctorId,medicine.MedicationName,medicine.datePrescribed))
    
    def insertPrescribedMedicinefromValues(self,patientID,doctorID,MedicationName,dataPrescribed):
         con = self.connection.cursor()
         with self.connection:
            con.execute("INSERT INTO PrescribedMedicine VALUES (?,?,?,?)",(patientID,doctorID,MedicationName,dataPrescribed))
            
    def deletePrescribedMedicineforPatient(self,patient):
         con = self.connection.cursor()
         with self.connection:
                con.execute("DELETE FROM PrescribedMedicine WHERE patient_Id = ?",(patient.PatientId,))

    def  getAllPrescribedMedicine(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * FROM PrescribedMedicine")
            return con.fetchall()

    def getAllMedicinesOfPatient(self,patient):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from PrescribedMedicine WHERE patient_Id = ?",(patient.PatientId,))
            return con.fetchall()

    def getMedicinesofPatientByID(self,patientID):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from PrescribedMedicine WHERE patient_id = ?",(patientID,))
            return con.fetchall()


    def getAllMedicinesofDoctor(self,doctor):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from PrescribedMedicine WHERE doc_id = ?",(doctor.DoctorId,))
            return con.fetchall()

    def printAllMedcines(self):
         con = self.connection.cursor()
         with self.connection:
             print(pd.read_sql_query("SELECT * FROM PrescribedMedicine",self.connection))

    #hereditaryIllness
    def insertHereditaryIllness(self,patient,illness):
        con = self.connection.cursor()
        with self.connection:
            con.execute("INSERT INTO HereditaryIllness VALUES (?,?)",(patient.PatientId,illness))
    
    def deleteHereditaryIllnessofPatient(self,patient):
        con = self.connection.cursor()
        with self.connection:
                con.execute("DELETE FROM HereditaryIllness WHERE patient_id = ?",(patient.PatientId,))

    def getAllHeridatryIllnesses(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * FROM HereditaryIllness")
            return con.fetchall()

    def getAllHeridatryIllnessesofPatient(self,patient):
          con = self.connection.cursor()
          with self.connection:
            con.execute("SELECT * from HereditaryIllness WHERE patient_id = ?",(patient.PatientId,))
            return con.fetchall()

    def getAllPatientsWithSpecIllness(self,illnessName):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT * from HereditaryIllness WHERE illness = ?",(illnessName))
            return con.fetchall()

    def printAllIllnesses(self):
         con = self.connection.cursor()
         with self.connection:
             print(pd.read_sql_query("SELECT * FROM HereditaryIllness",self.connection))

    def getSumOfPatients(self):
         con = self.connection.cursor()
         with self.connection:
            con.execute("SELECT COUNT(*) FROM Patient")
            return con.fetchone()

    def getSumfDoctors(self):
        con = self.connection.cursor()
        with self.connection:
            con.execute("SELECT COUNT(*) FROM Doctor")
            return con.fetchone()

    '''Generate a random 10 digit int to be used for id '''
    def generateRandomId(self):
        val = uuid.uuid4().int
        trim = str(val)[:10]
        intTrim = int(trim)
        return intTrim
  
    def deleteDataBase(self):
        os.remove("./Valitudo.db")

