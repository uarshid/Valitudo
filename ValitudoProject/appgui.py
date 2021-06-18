import tkinter as tk
import tkinter.ttk as ttk
from  Database import Database
from DataClasses import *
from tkinter import font
from datetime import date



import tkinter as tk



LARGE_FONT= ("Verdana", 12)

#controller
class ValitudoApps(tk.Tk):

    def __init__(self,*args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        self.doctorID = 0

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


            #the following code puts all the frames in a tuple where they will be raised on top of each other        
        self.frames = {}
        self.pages = (StartPage, DoctorLoginPage, DoctorPage,SearchForPatient,createAppointment,PatientManagement,Choices,AddPatient,DeletePatient,PatientChoices,updatePatient,MyPatients,PrescribedMedicine,PatientView,AdminChoices,AdminAddPatient,AdminAddDoctor,Statistics)
        for F in self.pages:
            frame = F(container, self, self.pages)

            self.frames[F] = frame

            frame.grid(row=0,column=0,sticky='nsew')

        self.show_frame(StartPage)

    #frames are raised to the top
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


    def changeDoctorID(self,newID):
        self.doctorID = newID
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self,parent)

        
        self.patientLogo = tk.Canvas(self,width=800,height=800)
        self.patientLogo.place(anchor='nw', relx='0.06', rely='0.15', x='0', y='0')
        self.doctorLogo = tk.Canvas(self)
        self.doctorLogo.place(anchor='nw', relx='0.56', rely='0.15', x='0', y='0')
        self.adminLogo = tk.Canvas(self)
        self.adminLogo.place(anchor='nw', relx='0.3', rely='0.53', x='0', y='0')
        self.PatientLoginButton = tk.Button(self,command=lambda: controller.show_frame(PatientChoices))
        self.PatientLoginButton.configure(text='Patient Login')
        self.PatientLoginButton.place(anchor='nw', relheight='0.05', relx='0.21', rely='0.46', x='0', y='0')

        self.DoctorLoginButton = tk.Button(self,command=lambda: controller.show_frame(DoctorLoginPage))
        self.DoctorLoginButton.configure(text='Doctor Login')
        self.DoctorLoginButton.place(anchor='nw', relheight='0.05', relx='0.67', rely='0.46', x='0', y='0')
        self.frame2 = tk.Frame(self)
        self.label3 = tk.Label(self.frame2)
        self.label3.configure(background='sky blue', text='Welcome to Valitudo')
        self.label3.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
        self.frame2.configure(background='gold', borderwidth='5', height='200', width='200')
        self.frame2.place(anchor='nw', relheight='0.08', relwidth='0.44', relx='0.27', rely='0.03', x='0', y='0')
        self.button20 = tk.Button(self,command=lambda:controller.show_frame(AdminChoices))
        self.button20.configure(text='Admin')
        self.button20.place(anchor='nw', relheight='0.05', relx='0.43', rely='0.84', x='0', y='0')
       



class DataThings():
    doctorID = 20

class DoctorLoginPage(tk.Frame,DataThings):

    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        #label.(pady =10,padx=10)
        self.controller = controller
        self.database = Database()
        self.controller = controller
        self.label1 = tk.Label(self,text='Please enter your id').pack(pady=20)


        self.login_input = tk.StringVar()
        self.entry1 = tk.Entry(self,textvariable=self.login_input)
        
        controller.changeDoctorID(self.login_input.get())
        DataThings.doctorID = self.login_input.get()
        self.entry1.pack()
        self.errorlabel = tk.Label(self)


        self.button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))

        self.button1.pack(pady=20)

        self.button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(DoctorPage))
      #  self.button2.pack()
        
        self.loginButton = tk.Button(self,text='Log In',command=self.validate)
        self.loginButton.pack()

    def sendID(self,ID):
         returned = self.database.findDoctorWithSpecificID(ID)
         tupleReturned = returned[0]
         docName =  "Welcome Doctor "  + tupleReturned[1] +  " " + tupleReturned[2]
         self.controller.frames[self.controller.pages[2]].DoctorIDValue.set(docName)
         docIDLabel = "Your ID is  \n {}".format(tupleReturned[0])
         self.controller.frames[self.controller.pages[2]].doctorIDNUm.set(ID)
         self.controller.frames[self.controller.pages[2]].doctorIDStatement.set(docIDLabel)

    def validate(self):
        doctorInfo = self.database.findDoctorWithSpecificID((self.login_input.get()))
        if (len(doctorInfo) == 0):
                    self.errorlabel.configure(text="Invalid login please check again, or register in the database")
                    self.errorlabel.pack()
        else:
            self.sendID(self.login_input.get())
            #self.loginButton.configure(command=lambda:self.controller.show_frame(DoctorPage))
            self.login_input.set("")
            self.controller.show_frame(DoctorPage)

      
class DoctorPage(tk.Frame,DataThings):

    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()
        
        self.controller = controller
        self.DoctorIDValue = tk.StringVar()
        self.doctorIDNUm  = tk.StringVar()
        self.doctorIDStatement = tk.StringVar()
        self.headingFrame = tk.Frame(self,bg="#FFBB00",bd=5)
        self.headingFrame.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.13)

        self.headingLabel = tk.Label(self.headingFrame, textvariable=self.DoctorIDValue, bg='sky blue', fg='white', font=('Courier',15))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
       
        self.IDNUMLabel = tk.Label(self,textvariable=self.doctorIDStatement)
        self.IDNUMLabel.place(anchor='nw', relx='0.79', rely='0.08')

        self.label = tk.Label(self, font=LARGE_FONT,textvariable=self.DoctorIDValue)
       

        self.actionFrame = tk.Frame(self,bg="sky blue")
        self.actionFrame.place(relheight='0.7', relwidth='0.82', relx='0.1', rely='0.2')

    
        button1 = tk.Button(self.actionFrame, text="Search for Patient",
                            command=lambda: controller.show_frame(SearchForPatient))
        button1.place(anchor='nw', relheight='0.15', relwidth='0.26', relx='0.17', rely='0.13')


        makeAppointmentButton = tk.Button(self.actionFrame, text="Make Appointment",command=lambda: controller.show_frame(createAppointment))
        makeAppointmentButton.place(anchor='nw', relheight='0.15', relwidth='0.26', relx='0.66', rely='0.13')

        myPatientsButton = tk.Button(self.actionFrame,text=" View My Patients", command=self.getPatients)
        #chnage
        myPatientsButton.place(anchor='nw', relheight='0.15', relwidth='0.26', relx='0.17', rely='0.4')


        AddOrDeletePatientsButton = tk.Button(self.actionFrame,text="Patient Management",command=lambda: controller.show_frame(PatientManagement))
        AddOrDeletePatientsButton.place(anchor='nw', relheight='0.15', relwidth='0.26', relx='0.66', rely='0.4')

        PatientIllnessButton = tk.Button(self.actionFrame,text="Add Patient \n Medical Test")
        PatientIllnessButton.place(anchor='nw', relheight='0.15', relwidth='0.26', relx='0.17', rely='0.68', x='0', y='0')

        PrescribeMedicineButton = tk.Button(self.actionFrame,text="Prescribe Medicine",command=self.sendIDtoMedcine)
        PrescribeMedicineButton.place(anchor='nw', relheight='0.15', relwidth='0.26', relx='0.66', rely='0.68')


        logOutButton = tk.Button(self.actionFrame,text="Log Out",command=lambda: controller.show_frame(DoctorLoginPage))
        logOutButton.place(anchor='nw', relheight='0.09', relwidth='0.21', relx='0.46', rely='0.91')
    
    
    def getPatients(self):
        idasint = int(self.doctorIDNUm.get())
        patientList = self.database.findAssignedPatientbyDocID(idasint)
        #rint(patientList)
        label1 = ""
        label2 = ""
        label3 = ""
        listoflabels = [label1, label2, label3]
        currentLabelPos = 0
        for patient in patientList:
            PatientString = " \n  First name: {} \n Last name: {} \n DOB: {} \n Age: {} \n Gender: {} \n Address: {} \nPharmacist: {} \n".format(patient[1],patient[2],patient[3],patient[4],patient[5],patient[6],patient[8])
            listoflabels[currentLabelPos] = PatientString   
            currentLabelPos = currentLabelPos + 1
        self.controller.frames[self.controller.pages[11]].patient1data.set(listoflabels[0])
        self.controller.frames[self.controller.pages[11]].patient2data.set(listoflabels[1])
        self.controller.frames[self.controller.pages[11]].patient3data.set(listoflabels[2])
        self.controller.show_frame(MyPatients)

    def doPatientFunction(self):
        variable = self.doctorIDNUm.get()
        integer = int(variable)
        self.getPatients(integer)

    def sendIDtoMedcine(self):
        self.controller.frames[self.controller.pages[12]].doctorIDValue.set(self.doctorIDNUm.get())
        self.controller.show_frame(PrescribedMedicine)


class SearchForPatient(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()

        self.headingFrame = tk.Frame(self,bg="#FFBB00",bd=5)
        self.headingFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

        self.headingLabel = tk.Label(self.headingFrame, text="Search For Patient By ID", bg='sky blue', fg='white', font=('Courier',15))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
       

        backButton = tk.Button(self,text="Cancel",command=lambda:controller.show_frame(DoctorPage))
        backButton.place(relx=0.28,rely=0.91, relwidth=0.18,relheight=0.08)
    
        self.searchResultsFrame = tk.Frame(self,bg='sky blue')
        self.searchResultsFrame.place(relheight='0.61', relwidth='0.82', relx='0.1', rely='0.3')
        
      #  tk.Scrol

        self.searchinput = tk.StringVar()
        self.searchFeild = tk.Entry(self.searchResultsFrame,textvariable=self.searchinput)
        self.searchFeild.place(anchor='nw', relheight='0.1', relx='0.26', rely='0.14', x='0', y='0')

        searchButton = tk.Button(self.searchResultsFrame,text="Search",command=self.getPatient)
        searchButton.place(anchor='nw', relx='0.66', rely='0.14',relheight='0.1',relwidth='0.2')

        self.display = tk.Label(self.searchResultsFrame,bg="#FFBB00",bd=5)

    def getPatient(self):
        enteredID = self.searchinput.get()
        returned = self.database.findPatientOnlyID(int(enteredID))
        #put here mesage if searched pateint is not in database
        values = returned[0]
        printString = " \n  First name: {} \n\n Last name: {} \n\n DOB: {} \n\n  Age: {} \n\n Gender: {} \n\n Address: {} \n\n".format(values[1],values[2],values[3],values[4],values[5],values[6])  
        self.display.configure(text=printString)
        self.display.place(anchor='nw', relheight='0.46', relwidth='0.51', relx='0.21', rely='0.34')

#Appointment Creation Frame
class createAppointment(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()

        self.controller = controller
        
        self.frammeHeading = tk.Frame(self,bg="#FFBB00",bd=5)
        self.frammeHeading.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

        headingLabel = tk.Label(self.frammeHeading, text="Make Appointment", bg='sky blue', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        self.detailsFrame = tk.Frame(self,bg='sky blue')
        self.detailsFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)


        lb1 = tk.Label(self.detailsFrame,text="Patient ID : ", bg='sky blue', fg='white')
        lb1.place(relx=0.05,rely=0.1, relheight=0.1)

        self.patientIDValue = tk.StringVar()
        patientIDEntry = tk.Entry(self.detailsFrame,textvariable=self.patientIDValue)
        patientIDEntry.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08) 

        dateLabel = tk.Label(self.detailsFrame,text="Appointment Date(MM/DD/YYYY) : ", bg='sky blue', fg='white')
        dateLabel.place(relx=0.05,rely=0.25, relheight=0.08)

        self.dateEntryValue = tk.StringVar()
        dateEntry = tk.Entry(self.detailsFrame,textvariable=self.dateEntryValue)
        dateEntry.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)

        timeLabel = tk.Label(self.detailsFrame,text="Time: ", bg='sky blue', fg='white')
        timeLabel.place(relx=0.05,rely=0.40, relheight=0.08)
        
        self.timeEntryValue = tk.StringVar()
        timeEntry = tk.Entry(self.detailsFrame,textvariable=self.timeEntryValue)
        timeEntry.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08)

        purposeLabel = tk.Label(self.detailsFrame,text="Purpose:", bg='sky blue', fg='white')
        purposeLabel.place(relx=0.05,rely=0.55, relheight=0.08)
  
        self.purposeEntry = tk.StringVar()
        purposeEntry = tk.Entry(self.detailsFrame,textvariable=self.purposeEntry)        
        purposeEntry.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

        self.SubmitBtn = tk.Button(self,text="Create Appointment",bg='#d1ccc0', fg='black',command=self.makeAppointment)
        self.SubmitBtn.place(relx=0.28,rely=0.91, relwidth=0.18,relheight=0.08)

        self.successFrame = tk.Frame(self,bg='black')


        self.endButton = tk.Button(self,text="Back to Home Page",command=lambda:controller.show_frame(DoctorPage))
        



       # self.successMessage = 

        self.cancelButton = tk.Button(self,text="Quit",bg='#f7f1e3', fg='black', command=lambda:controller.show_frame(DoctorPage))
        self.cancelButton.place(relx=0.53,rely=0.91, relwidth=0.18,relheight=0.08)

        #Here gonna have entry feilds, and then gonna insert into the 
    def makeAppointment(self):
        patientValue = int(self.patientIDValue.get())
        patientData = self.database.findPatientOnlyID(patientValue)
        datalist = patientData[0]
        self.patientNameFromID = "Successfully created appointment with " + datalist[1] + " "  + datalist[2]
        self.sucessLabel = tk.Label(self.successFrame,text=self.patientNameFromID)
        dateValue  =  self.dateEntryValue.get()
        timeValue =  self.timeEntryValue.get()
        purposeValue = self.purposeEntry.get()
        self.database.insertnewAppointWithValues(patientValue,2345,"3/4/2022","4:00 pm","Physical")
        self.detailsFrame.place_forget()
        self.frammeHeading.place_forget()
        self.SubmitBtn.place_forget()
        self.cancelButton.place_forget()
        self.successFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.3)
        self.sucessLabel.place(relx=0.2,rely=0.25,relwidth=0.70,relheight=0.25)
        self.endButton.place(relx=0.28,rely=0.91, relwidth=0.18,relheight=0.08)


class PatientManagement(tk.Frame):
     def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.database = Database()
    #VIew patient screen right
        self.IdLabel = tk.Label(self,text='Please enter patient id')
        self.IdLabel.pack(pady='20', side='top')

        self.login_input = tk.StringVar()

        self.idEntry = tk.Entry(self,textvariable=self.login_input)
        self.idEntry.pack(pady='20',side='top')
        self.logInButton = tk.Button(self,text="Log in",command=self.validate)
        self.logInButton.pack(pady='30',side="top")
        self.goBackButton = tk.Button(self,text="Cancel",command=lambda:controller.show_frame(DoctorPage))
        self.goBackButton.pack(pady='30',side="top")

        self.addPatientButton = tk.Button(self,text="Add New Patient",command=lambda:controller.show_frame(AddPatient))
        self.addPatientButton.pack(side="top")
        

        self.errorlabel = tk.Label(self)

     def sendFirstNameFromIDtoNextFrame(self,ID):
         returnedList = self.database.findPatientOnlyID(ID)
         firstEntry = returnedList[0]
         firstName = firstEntry[1]
         lastName =  firstEntry[2]
         DOB = firstEntry[3]
         age = firstEntry[4]
         gender = firstEntry[5]
         address = firstEntry[6]
         doctorId = firstEntry[7]
         Pharmacist = firstEntry[8]

         self.controller.frames[self.controller.pages[10]].firstname_input.set(firstName)
         self.controller.frames[self.controller.pages[10]].LastNameInput.set(lastName)
         self.controller.frames[self.controller.pages[10]].DOBInput.set(DOB)
         self.controller.frames[self.controller.pages[10]].AgeEntryInput.set(age)
         self.controller.frames[self.controller.pages[10]].GenderEntryInput.set(gender)
         self.controller.frames[self.controller.pages[10]].AddressEntryInput.set(address)
         self.controller.frames[self.controller.pages[10]].DoctorIdInput.set(doctorId)
         self.controller.frames[self.controller.pages[10]].pharmacistIDinput.set(Pharmacist)
         self.controller.frames[self.controller.pages[10]].IDFromLogin.set(ID)


     def validate(self):
        patientInfo = self.database.findPatientOnlyID((self.login_input.get()))
        if (len(patientInfo) == 0):
                    self.errorlabel.configure(text="Invalid login please check again, or register patient in the database")
                    self.errorlabel.pack()
        else:
            self.sendFirstNameFromIDtoNextFrame(self.login_input.get())
            self.login_input.set("")           
            self.controller.show_frame(Choices)

class Choices(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.label1 = tk.Label(self)
        self.label1.configure(text="What would you like to do for this patient?")
        self.label1.pack(pady='20', side='top')

        self.DeletePatientButton = tk.Button(self,command=lambda:controller.show_frame(DeletePatient))
        self.DeletePatientButton.configure(text='Delete Patient')
        self.DeletePatientButton.pack(pady='20', side='top')

        self.UpdatePatientDetails = tk.Button(self,command=lambda:controller.show_frame(updatePatient))
        self.UpdatePatientDetails.configure(text='Update Patient Details')
        self.UpdatePatientDetails.pack(side='top',pady='20')

        self.logOutButton = tk.Button(self,command=lambda:controller.show_frame(PatientManagement))
        self.logOutButton.configure(text='Log Out')
        self.logOutButton.pack(pady='20', side='top')
        
    
class AddPatient(tk.Frame):
     def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()
        self.patientDetailsFrame = tk.Frame(self)
        self.firstname_input = tk.StringVar()

        self.FrirstNameLabel = tk.Label(self.patientDetailsFrame)
        self.FrirstNameLabel.configure(text='First Name',textvariable=self.firstname_input)
        self.FrirstNameLabel.place(anchor='nw', relx='0.22', rely='0.13', x='0', y='0')

        self.FirstNameEntry = tk.Entry(self.patientDetailsFrame)
        self.FirstNameEntry.place(anchor='nw', relx='0.1', rely='0.21', x='0', y='0')

        self.label3 = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.LastNameInput = tk.StringVar()
        self.label3.configure(text='Last Name')
        self.label3.place(anchor='nw', relx='0.74', rely='0.13', x='0', y='0')
        self.LastNameEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.LastNameInput)
        self.LastNameEntry.place(anchor='nw', relx='0.6', rely='0.21', x='0', y='0')
        
        self.DOBInput = tk.StringVar()
        self.label4 = tk.Label(self.patientDetailsFrame)
        self.label4.configure(text='DOB')
        self.label4.place(anchor='nw', relx='0.24', rely='0.3', x='0', y='0')
        self.entry4 = tk.Entry(self.patientDetailsFrame,textvariable=self.DOBInput)
        self.entry4.place(anchor='nw', relx='0.1', rely='0.38', x='0', y='0')
        
        self.AgeEntryInput = tk.StringVar()
        self.AgeLabel = tk.Label(self.patientDetailsFrame)
        self.AgeLabel.configure(text='Age')
        self.AgeLabel.place(anchor='nw', relx='0.74', rely='0.3', x='0', y='0')
        self.AgeEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.AgeEntryInput)
        self.AgeEntry.place(anchor='nw', relx='0.6', rely='0.38', x='0', y='0')
        
        self.GenderEntryInput = tk.StringVar()
        self.GenderLabel = tk.Label(self.patientDetailsFrame)
        self.GenderLabel.configure(text='Gender')
        self.GenderLabel.place(anchor='nw', relx='0.24', rely='0.47', x='0', y='0')
        self.GenderEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.GenderEntryInput)
        self.GenderEntry.place(anchor='nw', relx='0.1', rely='0.54', x='0', y='0')
    
        self.AddressEntryInput = tk.StringVar()
        self.AddressLabel = tk.Label(self.patientDetailsFrame)
        self.AddressLabel.configure(text='Address')
        self.AddressLabel.place(anchor='nw', relx='0.74', rely='0.47', x='0', y='0')
        self.AddressEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.AddressEntryInput)
        self.AddressEntry.place(anchor='nw', relx='0.6', rely='0.54', x='0', y='0')
       
        self.patientDetailsFrame.configure(background='sky blue', height='100', width='200')
        self.patientDetailsFrame.place(anchor='nw', relheight='0.67', relwidth='0.87', relx='0.06', rely='0.22', x='0', y='0')


        self.titleFrame = tk.Frame(self)
        self.label9 = tk.Label(self.titleFrame)
        self.label9.configure(background='sky blue', text='Add Patient')
        self.label9.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
        self.titleFrame.configure(background='gold', borderwidth='5', height='200', width='200')
        self.titleFrame.place(anchor='nw', relheight='0.13', relwidth='0.5', relx='0.26', rely='0.03', x='0', y='0')
        
        self.cancelButton = tk.Button(self,command=lambda:controller.show_frame(PatientManagement))
        self.cancelButton.configure(text='Cancel')
        self.cancelButton.place(anchor='nw', relheight='0.09', relwidth='0.17', relx='0.13', rely='0.9', x='0', y='0')
        
        self.CreatePatientButton = tk.Button(self,command=self.createPatient)
        self.CreatePatientButton.configure(text='Add Patient')
        self.CreatePatientButton.place(anchor='nw', relheight='0.09', relwidth='0.25', relx='0.59', rely='0.9', x='0', y='0')
       
        self.DoctorIdInput = tk.StringVar()
        self.doctorIdEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.DoctorIdInput)
        self.doctorIdEntry.place(anchor='nw', relx='0.1', rely='0.7', x='0', y='0')
        self.DocIDLabel = tk.Label(self.patientDetailsFrame)
        self.DocIDLabel.configure(text='Doctor ID')
        self.DocIDLabel.place(anchor='nw', relx='0.24', rely='0.62', x='0', y='0')

        self.pharmacistIDinput = tk.StringVar()
        self.pharmacistIDEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.pharmacistIDinput)
        self.pharmacistIDEntry.place(anchor='nw', relx='0.6', rely='0.7', x='0', y='0')
        self.PharmacistIDLabel = tk.Label(self.patientDetailsFrame)
        self.PharmacistIDLabel.configure(text='Pharmacist ID')
        self.PharmacistIDLabel.place(anchor='nw', relx='0.72', rely='0.62', x='0', y='0')
        
        self.successFrame = tk.Frame(self)
        
        self.successLabel = tk.Label(self.successFrame)
        self.successLabel.configure(background='sky blue')
        self.successFrame.configure(background='gold', borderwidth='5', height='200', width='200')
        
        self.BackButton = tk.Button(self,command=lambda:controller.show_frame(PatientManagement))
        self.BackButton.configure(text='Back to Home')

    

     def createPatient(self):
         newId = self.database.generateRandomId()
         pharmId = int(self.pharmacistIDinput.get())
         docID = int(self.DoctorIdInput.get())
         newPatient = Patient(newId,self.firstname_input.get(),self.LastNameInput.get(),self.DOBInput.get(),self.AgeEntryInput.get(),self.GenderEntryInput.get(),self.AddressEntryInput.get())
       # self.endButton = tk.Button(self,text="Back to Home Page",command=lambda:controller.show_frame(DoctorPage))
         self.database.insertNewPatientWithOnlyOtherIDs(newPatient,docID,pharmId)
         self.patientDetailsFrame.destroy()
         self.cancelButton.destroy()
         self.CreatePatientButton.destroy()
         textsuccess = "Successfully Created Patient with Id " + str(newId)
         self.successLabel.configure(text=textsuccess)
         self.successLabel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
         self.successFrame.place(anchor='nw', relheight='0.29', relwidth='0.5', relx='0.26', rely='0.26', x='0', y='0')
         self.BackButton.place(anchor='nw', relheight='0.1', relwidth='0.17', relx='0.42', rely='0.6', x='0', y='0')

       # self.successMessage = 

       # self.cancelButton = tk.Button(self,text="Quit",bg='#f7f1e3', fg='black', command=lambda:controller.show_frame(DoctorPage))
       # self.cancelButton.place(relx=0.53,rely=0.91, relwidth=0.18,relheight=0.08)


class DeletePatient(tk.Frame):
   def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()
        self.label1 = tk.Label(self)
        self.label1.configure(text='Enter the id of the patient to  delete')
        self.label1.pack(padx='20', pady='40', side='top')

        self.backButton = tk.Button(self,command=lambda:controller.show_frame(Choices))
        self.backButton.pack(side='top')


        self.patientIdEntry = tk.Entry(self)
        self.IdEntry = tk.StringVar()
        self.patientIdEntry.configure(textvariable=self.IdEntry)
        self.patientIdEntry.pack(side='top')
        self.button2 = tk.Button(self,command=self.deletePatient)
        self.button2.configure(height='2', text='Delete', width='6')
        self.button2.pack(pady='30', side='top')

        


       # self.label2 = tk.Label(self)
       # self.label2.pack(pady='30', side='top')

        
        
   def deletePatient(self):
        pass

class updatePatient(tk.Frame):
        def __init__(self, parent, controller,pages):
            tk.Frame.__init__(self, parent)

            self.IDFromLogin = tk.StringVar()
            self.controller = controller
            self.database = Database()
            self.patientDetailsFrame = tk.Frame(self)
            self.firstname_input = tk.StringVar()

            self.FrirstNameLabel = tk.Label(self.patientDetailsFrame)
            self.FrirstNameLabel.configure(text='First Name')
            self.FrirstNameLabel.place(anchor='nw', relx='0.22', rely='0.13', x='0', y='0')

            self.FirstNameEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.firstname_input)
            self.FirstNameEntry.place(anchor='nw', relx='0.1', rely='0.21', x='0', y='0')

            self.label3 = tk.Label(self.patientDetailsFrame)

            self.LastNameInput = tk.StringVar()
            self.label3.configure(text='Last Name')
            self.label3.place(anchor='nw', relx='0.74', rely='0.13', x='0', y='0')
            self.LastNameEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.LastNameInput)
            self.LastNameEntry.place(anchor='nw', relx='0.6', rely='0.21', x='0', y='0')
            
            self.DOBInput = tk.StringVar()
            self.label4 = tk.Label(self.patientDetailsFrame)
            self.label4.configure(text='DOB')
            self.label4.place(anchor='nw', relx='0.24', rely='0.3', x='0', y='0')
            self.entry4 = tk.Entry(self.patientDetailsFrame,textvariable=self.DOBInput)
            self.entry4.place(anchor='nw', relx='0.1', rely='0.38', x='0', y='0')
            
            self.AgeEntryInput = tk.StringVar()
            self.AgeLabel = tk.Label(self.patientDetailsFrame)
            self.AgeLabel.configure(text='Age')
            self.AgeLabel.place(anchor='nw', relx='0.74', rely='0.3', x='0', y='0')
            self.AgeEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.AgeEntryInput)
            self.AgeEntry.place(anchor='nw', relx='0.6', rely='0.38', x='0', y='0')
            
            self.GenderEntryInput = tk.StringVar()
            self.GenderLabel = tk.Label(self.patientDetailsFrame)
            self.GenderLabel.configure(text='Gender')
            self.GenderLabel.place(anchor='nw', relx='0.24', rely='0.47', x='0', y='0')
            self.GenderEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.GenderEntryInput)
            self.GenderEntry.place(anchor='nw', relx='0.1', rely='0.54', x='0', y='0')
        
            self.AddressEntryInput = tk.StringVar()
            self.AddressLabel = tk.Label(self.patientDetailsFrame)
            self.AddressLabel.configure(text='Address')
            self.AddressLabel.place(anchor='nw', relx='0.74', rely='0.47', x='0', y='0')
            self.AddressEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.AddressEntryInput)
            self.AddressEntry.place(anchor='nw', relx='0.6', rely='0.54', x='0', y='0')
        
            self.patientDetailsFrame.configure(background='sky blue', height='100', width='200')
            self.patientDetailsFrame.place(anchor='nw', relheight='0.67', relwidth='0.87', relx='0.06', rely='0.22', x='0', y='0')


            self.titleFrame = tk.Frame(self)
            self.label9 = tk.Label(self.titleFrame)
            self.label9.configure(background='sky blue', text='Update Patient')
            self.label9.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
            self.titleFrame.configure(background='gold', borderwidth='5', height='200', width='200')
            self.titleFrame.place(anchor='nw', relheight='0.13', relwidth='0.5', relx='0.26', rely='0.03', x='0', y='0')
            
            self.cancelButton = tk.Button(self,command=lambda:controller.show_frame(DoctorPage))
            self.cancelButton.configure(text='Cancel')
            self.cancelButton.place(anchor='nw', relheight='0.09', relwidth='0.17', relx='0.13', rely='0.9', x='0', y='0')
            
            self.updatePatientButton = tk.Button(self,command=self.updatePatient)
            self.updatePatientButton.configure(text='Update Patient')
            self.updatePatientButton.place(anchor='nw', relheight='0.09', relwidth='0.25', relx='0.59', rely='0.9', x='0', y='0')
        
            self.DoctorIdInput = tk.StringVar()
            self.doctorIdEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.DoctorIdInput)
            self.doctorIdEntry.place(anchor='nw', relx='0.1', rely='0.7', x='0', y='0')
            self.DocIDLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
            self.DocIDLabel.configure(text='Doctor ID')
            self.DocIDLabel.place(anchor='nw', relx='0.24', rely='0.62', x='0', y='0')

            self.pharmacistIDinput = tk.StringVar()
            self.pharmacistIDEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.pharmacistIDinput)
            self.pharmacistIDEntry.place(anchor='nw', relx='0.6', rely='0.7', x='0', y='0')
            self.PharmacistIDLabel = tk.Label(self.patientDetailsFrame)
            self.PharmacistIDLabel.configure(text='Pharmacist ID')
            self.PharmacistIDLabel.place(anchor='nw', relx='0.72', rely='0.62', x='0', y='0')
            
            self.successFrame = tk.Frame(self)
            
            self.successLabel = tk.Label(self.successFrame,text="Successfully Updated Patient Details")
            self.successLabel.configure(background='sky blue')
            self.successFrame.configure(background='gold', borderwidth='5', height='200', width='200')
            
            self.goBackButton = tk.Button(self,command=lambda:controller.show_frame(Choices),text="Go Back")
            self.BackButton = tk.Button(self,command=lambda:controller.show_frame(PatientManagement))
            self.BackButton.configure(text='Back to Home')

        def updatePatient(self):
           # here pass things to update well will really update the address and age right?
           self.database.updatePatientAgeByID(self.AgeEntryInput.get(),self.IDFromLogin.get())
           self.database.updatePatientAddressByID(self.AddressEntryInput.get(),self.IDFromLogin.get())
           self.patientDetailsFrame.place_forget()
           self.cancelButton.place_forget()
           self.updatePatientButton.place_forget()
           self.successLabel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
           self.successFrame.place(anchor='nw', relheight='0.29', relwidth='0.5', relx='0.26', rely='0.26', x='0', y='0')
           self.goBackButton.place(anchor='nw', relheight='0.06', relwidth='0.2', relx='0.43',rely='0.8')
    
    #Patient Login Side
#class for doctor to view all patients
class MyPatients(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.frame2 = tk.Frame(self)
        self.label1 = tk.Label(self.frame2,text="Your Patients")
        self.label1.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
        self.frame2.configure(background='gold', borderwidth='5', height='200', width='200')
        self.frame2.place(anchor='nw', relheight='0.18', relwidth='0.59', relx='0.2', rely='0.05', x='0', y='0')
        self.patient1data = tk.StringVar()
        self.firstPatientInfo = tk.Label(self,textvariable=self.patient1data)
        self.firstPatientInfo.place(anchor='nw', relx='0.26', rely='0.38', x='0', y='0')
        
        self.patient2data = tk.StringVar()
        self.secondPatientInfo = tk.Label(self,textvariable=self.patient2data)
        self.secondPatientInfo.place(anchor='nw', relx='0.64', rely='0.38', x='0', y='0')
        self.patient3data = tk.StringVar()
        self.thirdPatientInfo = tk.Label(self,textvariable=self.patient3data)
        self.thirdPatientInfo.place(anchor='nw', relx='0.45', rely='0.62', x='0', y='0')
        self.BackButton = tk.Button(self, command=lambda:controller.show_frame(DoctorPage))
        self.BackButton.configure(text='Go Back')
        self.BackButton.place(anchor='nw', relheight='0.06', relwidth='0.17', relx='0.42', rely='0.9', x='0', y='0')
    
class PrescribedMedicine(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.doctorIDValue = tk.StringVar()
        print(self.doctorIDValue)
        self.database = Database()
        self.headingFrame = tk.Frame(self)
        self.label2 = tk.Label(self.headingFrame)
        self.label2.configure(text='Prescribe Medicine For A Patient')
        self.label2.place(anchor='nw', relheight='1', relwidth='1', relx='0', rely='0', x='0', y='0')
        self.headingFrame.configure(background='gold', borderwidth='5', height='100', width='250')
        self.headingFrame.pack(padx='20', pady='30', side='top')

        self.label3 = tk.Label(self)
        self.label3.configure(text='Patient ID')
        self.label3.pack(side='top')
        self.IDEntryValue = tk.StringVar()

        self.IDEntry = tk.Entry(self,textvariable=self.IDEntryValue)
        self.IDEntry.pack(pady='30', side='top')
        self.PharmacistIDLabel = tk.Label(self)
        self.PharmacistIDLabel.configure(text='Pharmacist ID')
        self.PharmacistIDLabel.pack(side='top')

        self.medicationText = tk.Text(self)
        self.medicationText.configure(height='10', width='50',highlightbackground='sky blue', highlightcolor='sky blue', insertborderwidth='10')
        self.medicationText.pack(padx='20', side='top')
        self.DOneButton = tk.Button(self,command=self.enterMedicine)
        self.DOneButton.configure(text='Done')
        self.DOneButton.pack(pady='20', side='top')
        self.DoneLabel = tk.Label(self)
        self.DoneLabel.pack(pady='20', side='top')
        self.GoBackButton = tk.Button(self,command=lambda:controller.show_frame(DoctorPage))
        self.GoBackButton.configure(text='Go Back')
        self.GoBackButton.pack(side='top')
    
    def enterMedicine(self):
        currentdate = date.today()
        fullDate = currentdate.strftime("%B %d, %Y")
        self.database.insertPrescribedMedicinefromValues(self.IDEntryValue.get(),self.doctorIDValue.get(),self.medicationText.get("1.0","end"),fullDate)
        textCompleted = "Prescribed Medicine for Patient With ID {} on ".format(self.IDEntry.get()) + fullDate
        self.DoneLabel.configure(text=textCompleted)

class PatientChoices(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.database = Database()
        self.IdRequestLabel = tk.Label(self)
        self.IdRequestLabel.configure(text='Please enter your patient id')
        self.IdRequestLabel.pack(pady='30', side='top')
        self.ID_Entry = tk.StringVar()
        self.entry1 = tk.Entry(self,textvariable=self.ID_Entry)
        self.entry1.pack(pady='20', side='top')
        
        self.LoginButton = tk.Button(self)
        self.LoginButton.configure(text='Log In',command=self.validate)
        self.LoginButton.pack(padx='30', pady='30', side='top')
        self.errorlabel = tk.Label(self)
        self.errorlabel.pack(side='top')

        self.cancelButton = tk.Button(self,command=lambda:controller.show_frame(StartPage))
        self.cancelButton.configure(text='Cancel')
        self.cancelButton.pack(side='top')

    
    def sendID(self,ID):
        IDString = "Your ID is \n" + ID
        self.controller.frames[self.controller.pages[13]].IDValue.set(IDString)
        returnedlist = self.database.findPatientOnlyID(ID)
        value = returnedlist[0] #tuple returned
        returnedDoctor = self.database.findDoctorWithSpecificID(value[7])
        doctorDetails = returnedDoctor[0]
        DoctorInfoString ="Your Doctor \n First Name: {} \n LastName: {}  \n OfficeNum: {} \n Specialty: {} \n ".format(doctorDetails[1],doctorDetails[2],doctorDetails[3],doctorDetails[7])
        self.controller.frames[self.controller.pages[13]].DoctorLabelValue.set(DoctorInfoString)
        #Getting appointment
        appointmentList = self.database.getPatientAppointmentsByID(ID)
        appointed = appointmentList[0]
        AppointmentString = "Your Appointment \n  Date: {} \n Time: {} \n Purpose: {}".format(appointed[2],appointed[3],appointed[4])
        self.controller.frames[self.controller.pages[13]].AppointmentLabelValue.set(AppointmentString)
        #getting medicine
        medicineList = self.database.getMedicinesofPatientByID(ID)
        medicine = medicineList[0]
        medicineString = "Your Medication \n Medication Name: {} \n Date Prescribed: {}".format(medicine[2],medicine[3])
        self.controller.frames[self.controller.pages[13]].PrescribedMedicineValue.set(medicineString)
        
        
    
    def validate(self):
        patientInfo = self.database.findPatientOnlyID((self.ID_Entry.get()))
        patientAppointment = self.database.getPatientAppointmentsByID(self.ID_Entry.get())
        patientMedicine = self.database.getMedicinesofPatientByID(self.ID_Entry.get())
        if (len(patientInfo) == 0 or len(patientAppointment) == 0 or len(patientMedicine) == 0):
                    self.errorlabel.configure(text="Invalid login please check again or register in the database \n or create an appointment and presribe medicine for the patient")
                    self.errorlabel.pack()
        else:
            self.sendID(self.ID_Entry.get())
            #self.loginButton.configure(command=lambda:self.controller.show_frame(DoctorPage))
            self.ID_Entry.set("")
            self.controller.show_frame(PatientView) 

class PatientView(tk.Frame):
    def __init__(self, parent, controller, pages):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.DoctorLabelValue = tk.StringVar()                                               
        self.DoctorInfoLabel = tk.Label(self,textvariable=self.DoctorLabelValue)
        self.DoctorInfoLabel.place(anchor='nw', relx='0.11', rely='0.26', x='0', y='0')

        self.AppointmentLabelValue = tk.StringVar()
        self.AppointmentInfoLabel = tk.Label(self,textvariable=self.AppointmentLabelValue)
        self.AppointmentInfoLabel.place(anchor='nw', relx='0.79', rely='0.26', x='0', y='0')
        
        self.PrescribedMedicineValue = tk.StringVar()
        self.PrecribedMedicineInfo = tk.Label(self,textvariable=self.PrescribedMedicineValue)
        self.PrecribedMedicineInfo.place(anchor='nw', relx='0.78', rely='0.53', x='0', y='0')
        self.LogoutButton = tk.Button(self,command=lambda:controller.show_frame(StartPage))
        self.LogoutButton.configure(text='Log Out')
        self.LogoutButton.place(anchor='nw', relheight='0.06', relwidth='0.2', relx='0.43', rely='0.9', x='0', y='0')
        
        self.IDValue = tk.StringVar()
        self.IdNumInfo = tk.Label(self,textvariable=self.IDValue)
        self.IdNumInfo.place(anchor='nw', relx='0.79', rely='0.06', x='0', y='0')
        
        self.MedicalTestInfo = tk.Label(self)
        self.MedicalTestInfo.place(anchor='nw', relx='0.11', rely='0.53', x='0', y='0')
        self.HeadingFrame = tk.Frame(self)
        self.HeadingLabel = tk.Label(self.HeadingFrame)
        self.HeadingLabel.configure(background='sky blue', text='Your Info')
        self.HeadingLabel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
        self.HeadingFrame.configure(background='gold', borderwidth='5', height='200', width='200')
        self.HeadingFrame.place(anchor='nw', relheight='0.17', relwidth='0.32', relx='0.31', rely='0.03', x='0', y='0')

class AdminChoices(tk.Frame):
     def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)   

        self.database = Database()
        self.controller = controller
        self.titleLabel = tk.Label(self)
        self.titleLabel.configure(text='Options')
        self.titleLabel.pack(pady='30', side='top')
        self.AddAPatient = tk.Button(self,command=lambda:controller.show_frame(AdminAddPatient))
        self.AddAPatient.configure(text='Add a Patient')
        self.AddAPatient.pack(padx='30', pady='30', side='top')
        self.AddADoctor = tk.Button(self,command=lambda:controller.show_frame(AdminAddDoctor))
        self.AddADoctor.configure(text='Add a Doctor')
        self.AddADoctor.pack(side='top')
        self.StatsButton = tk.Button(self,command=self.DataStats)
        self.StatsButton.configure(text='View Database Stats')
        self.StatsButton.pack(pady='30', side='top')
        self.BackButton = tk.Button(self,command=lambda:controller.show_frame(StartPage))
        self.BackButton.configure(text='Go Back')
        self.BackButton.pack(pady='20', side='top')

     def DataStats(self):
         PatientsTup = self.database.getSumOfPatients()
         sumnumber = PatientsTup[0]
         SumString = "Total Number of Patients:" + str(sumnumber)
         self.controller.frames[self.controller.pages[17]].PatientValueNum.set(SumString)
         DoctorTup = self.database.getSumfDoctors()
         sumDocNum = DoctorTup[0]
         DocString = "Total Number of Doctors:" + str(sumDocNum)
         self.controller.frames[self.controller.pages[17]].DoctorValueNum.set(DocString)
         self.controller.show_frame(Statistics)
class Statistics(tk.Frame):
    pass
class AdminAddPatient(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()
        self.patientDetailsFrame = tk.Frame(self)
        self.firstname_input = tk.StringVar()

        self.FrirstNameLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.FrirstNameLabel.configure(text='First Name')
        self.FrirstNameLabel.place(anchor='nw', relx='0.22', rely='0.13', x='0', y='0')
        self.FirstNameEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.firstname_input)
        self.FirstNameEntry.place(anchor='nw', relx='0.1', rely='0.21', x='0', y='0')

        self.label3 = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.LastNameInput = tk.StringVar()
        self.label3.configure(text='Last Name')
        self.label3.place(anchor='nw', relx='0.74', rely='0.13', x='0', y='0')
        self.LastNameEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.LastNameInput)
        self.LastNameEntry.place(anchor='nw', relx='0.6', rely='0.21', x='0', y='0')
        
        self.DOBInput = tk.StringVar()
        self.label4 = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.label4.configure(text='DOB')
        self.label4.place(anchor='nw', relx='0.24', rely='0.3', x='0', y='0')
        self.entry4 = tk.Entry(self.patientDetailsFrame,textvariable=self.DOBInput)
        self.entry4.place(anchor='nw', relx='0.1', rely='0.38', x='0', y='0')
        
        self.AgeEntryInput = tk.StringVar()
        self.AgeLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.AgeLabel.configure(text='Age')
        self.AgeLabel.place(anchor='nw', relx='0.74', rely='0.3', x='0', y='0')
        self.AgeEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.AgeEntryInput)
        self.AgeEntry.place(anchor='nw', relx='0.6', rely='0.38', x='0', y='0')
        
        self.GenderEntryInput = tk.StringVar()
        self.GenderLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.GenderLabel.configure(text='Gender')
        self.GenderLabel.place(anchor='nw', relx='0.24', rely='0.47', x='0', y='0')
        self.GenderEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.GenderEntryInput)
        self.GenderEntry.place(anchor='nw', relx='0.1', rely='0.54', x='0', y='0')
    
        self.AddressEntryInput = tk.StringVar()
        self.AddressLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.AddressLabel.configure(text='Address')
        self.AddressLabel.place(anchor='nw', relx='0.74', rely='0.47', x='0', y='0')
        self.AddressEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.AddressEntryInput)
        self.AddressEntry.place(anchor='nw', relx='0.6', rely='0.54', x='0', y='0')
       
        self.patientDetailsFrame.configure(background='sky blue', height='100', width='200')
        self.patientDetailsFrame.place(anchor='nw', relheight='0.67', relwidth='0.87', relx='0.06', rely='0.22', x='0', y='0')


        self.titleFrame = tk.Frame(self)
        self.label9 = tk.Label(self.titleFrame)
        self.label9.configure(background='sky blue', text='Add Patient')
        self.label9.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
        self.titleFrame.configure(background='gold', borderwidth='5', height='200', width='200')
        self.titleFrame.place(anchor='nw', relheight='0.13', relwidth='0.5', relx='0.26', rely='0.03', x='0', y='0')
        
        self.cancelButton = tk.Button(self,command=lambda:controller.show_frame(PatientManagement))
        self.cancelButton.configure(text='Cancel')
        self.cancelButton.place(anchor='nw', relheight='0.09', relwidth='0.17', relx='0.13', rely='0.9', x='0', y='0')
        
        self.CreatePatientButton = tk.Button(self,command=self.createPatient)
        self.CreatePatientButton.configure(text='Add Patient')
        self.CreatePatientButton.place(anchor='nw', relheight='0.09', relwidth='0.25', relx='0.59', rely='0.9', x='0', y='0')
       
        self.DoctorIdInput = tk.StringVar()
        self.doctorIdEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.DoctorIdInput)
        self.doctorIdEntry.place(anchor='nw', relx='0.1', rely='0.7', x='0', y='0')
        self.DocIDLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.DocIDLabel.configure(text='Doctor ID')
        self.DocIDLabel.place(anchor='nw', relx='0.24', rely='0.62', x='0', y='0')

        self.pharmacistIDinput = tk.StringVar()
        self.pharmacistIDEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.pharmacistIDinput)
        self.pharmacistIDEntry.place(anchor='nw', relx='0.6', rely='0.7', x='0', y='0')
        self.PharmacistIDLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.PharmacistIDLabel.configure(text='Pharmacist ID')
        self.PharmacistIDLabel.place(anchor='nw', relx='0.72', rely='0.62', x='0', y='0')
        
        self.successFrame = tk.Frame(self)
        
        self.successLabel = tk.Label(self.successFrame)
        self.successLabel.configure(background='sky blue')
        self.successFrame.configure(background='gold', borderwidth='5', height='200', width='200')
        
        self.BackButton = tk.Button(self,command=lambda:controller.show_frame(AdminChoices))
        self.BackButton.configure(text='Back to Home')

    

    def createPatient(self):
         newId = self.database.generateRandomId()
         pharmId = int(self.pharmacistIDinput.get())
         docID = int(self.DoctorIdInput.get())
         newPatient = Patient(newId,self.firstname_input.get(),self.LastNameInput.get(),self.DOBInput.get(),self.AgeEntryInput.get(),self.GenderEntryInput.get(),self.AddressEntryInput.get())
       # self.endButton = tk.Button(self,text="Back to Home Page",command=lambda:controller.show_frame(DoctorPage))
         self.database.insertNewPatientWithOnlyOtherIDs(newPatient,docID,pharmId)
         self.patientDetailsFrame.destroy()
         self.cancelButton.destroy()
         self.CreatePatientButton.destroy()
         textsuccess = "Successfully Created Patient with Id " + str(newId)
         self.successLabel.configure(text=textsuccess)
         self.successLabel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
         self.successFrame.place(anchor='nw', relheight='0.29', relwidth='0.5', relx='0.26', rely='0.26', x='0', y='0')
         self.BackButton.place(anchor='nw', relheight='0.1', relwidth='0.17', relx='0.42', rely='0.6', x='0', y='0')

class AdminAddDoctor(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)
        
        self.database = Database()
        self.patientDetailsFrame = tk.Frame(self)
        self.firstname_input = tk.StringVar()

        self.FrirstNameLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.FrirstNameLabel.configure(text='First Name')
        self.FrirstNameLabel.place(anchor='nw', relx='0.22', rely='0.13', x='0', y='0')
        self.FirstNameEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.firstname_input)
        self.FirstNameEntry.place(anchor='nw', relx='0.1', rely='0.21', x='0', y='0')

        self.label3 = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.LastNameInput = tk.StringVar()
        self.label3.configure(text='Last Name')
        self.label3.place(anchor='nw', relx='0.74', rely='0.13', x='0', y='0')
        self.LastNameEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.LastNameInput)
        self.LastNameEntry.place(anchor='nw', relx='0.6', rely='0.21', x='0', y='0')
        
        self.officeNumInput = tk.StringVar()
        self.label4 = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.label4.configure(text='Office Number')
        self.label4.place(anchor='nw', relx='0.24', rely='0.3', x='0', y='0')
        self.entry4 = tk.Entry(self.patientDetailsFrame,textvariable=self.officeNumInput)
        self.entry4.place(anchor='nw', relx='0.1', rely='0.38', x='0', y='0')
        
        self.AgeEntryInput = tk.StringVar()
        self.AgeLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.AgeLabel.configure(text='Age')
        self.AgeLabel.place(anchor='nw', relx='0.74', rely='0.3', x='0', y='0')
        self.AgeEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.AgeEntryInput)
        self.AgeEntry.place(anchor='nw', relx='0.6', rely='0.38', x='0', y='0')
        
        self.GenderEntryInput = tk.StringVar()
        self.GenderLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.GenderLabel.configure(text='Gender')
        self.GenderLabel.place(anchor='nw', relx='0.24', rely='0.47', x='0', y='0')
        self.GenderEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.GenderEntryInput)
        self.GenderEntry.place(anchor='nw', relx='0.1', rely='0.54', x='0', y='0')
    
        self.AddressEntryInput = tk.StringVar()
        self.AddressLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.AddressLabel.configure(text='Address')
        self.AddressLabel.place(anchor='nw', relx='0.74', rely='0.47', x='0', y='0')
        self.AddressEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.AddressEntryInput)
        self.AddressEntry.place(anchor='nw', relx='0.6', rely='0.54', x='0', y='0')
       
        self.patientDetailsFrame.configure(background='sky blue', height='100', width='200')
        self.patientDetailsFrame.place(anchor='nw', relheight='0.67', relwidth='0.87', relx='0.06', rely='0.22', x='0', y='0')

        self.titleFrame = tk.Frame(self)
        self.label9 = tk.Label(self.titleFrame)
        self.label9.configure(background='sky blue', text='Add Doctor')
        self.label9.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
        self.titleFrame.configure(background='gold', borderwidth='5', height='200', width='200')
        self.titleFrame.place(anchor='nw', relheight='0.13', relwidth='0.5', relx='0.26', rely='0.03', x='0', y='0')
        
        self.cancelButton = tk.Button(self,command=lambda:controller.show_frame(PatientManagement))
        self.cancelButton.configure(text='Cancel')
        self.cancelButton.place(anchor='nw', relheight='0.09', relwidth='0.17', relx='0.13', rely='0.9', x='0', y='0')
        
        self.CreatePatientButton = tk.Button(self,command=self.createDoctor)
        self.CreatePatientButton.configure(text='Add Doctor')
        self.CreatePatientButton.place(anchor='nw', relheight='0.09', relwidth='0.25', relx='0.59', rely='0.9', x='0', y='0')
       
        self.SpecialtyIdInput = tk.StringVar()
        self.doctorIdEntry = tk.Entry(self.patientDetailsFrame,textvariable=self.SpecialtyIdInput)
        self.doctorIdEntry.place(anchor='nw', relx='0.1', rely='0.7', x='0', y='0')
        self.DocIDLabel = tk.Label(self.patientDetailsFrame,background="sky blue")
        self.DocIDLabel.configure(text='Specialty')
        self.DocIDLabel.place(anchor='nw', relx='0.24', rely='0.62', x='0', y='0')
        
        self.successFrame = tk.Frame(self)
        
        self.successLabel = tk.Label(self.successFrame)
        self.successLabel.configure(background='sky blue')
        self.successFrame.configure(background='gold', borderwidth='5', height='200', width='200')
        
        self.BackButton = tk.Button(self,command=lambda:controller.show_frame(AdminChoices))
        self.BackButton.configure(text='Back to Home')

    

    def createDoctor(self):
         newId = self.database.generateRandomId()
         newDoc = Doctor(newId,self.firstname_input.get(),self.LastNameInput.get(),self.officeNumInput.get(),self.AgeEntryInput.get(),self.GenderEntryInput.get(),self.AddressEntryInput.get(),self.SpecialtyIdInput.get())
       # self.endButton = tk.Button(self,text="Back to Home Page",command=lambda:controller.show_frame(DoctorPage))
         self.database.insertDoctor(newDoc)
         self.patientDetailsFrame.destroy()
         self.cancelButton.destroy()
         self.CreatePatientButton.destroy()
         textsuccess = "Successfully Created Doctor with Id " + str(newId)
         self.successLabel.configure(text=textsuccess)
         self.successLabel.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
         self.successFrame.place(anchor='nw', relheight='0.29', relwidth='0.5', relx='0.26', rely='0.26', x='0', y='0')
         self.BackButton.place(anchor='nw', relheight='0.1', relwidth='0.17', relx='0.42', rely='0.6', x='0', y='0')

class Statistics(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.HeadingLabel = tk.Label(self)
        self.HeadingLabel.configure(text='Stats')
        self.HeadingLabel.pack(padx='40', pady='40', side='top')
        
        fontStyle = font.Font(family="Arial", size=20)
        self.PatientValueNum = tk.StringVar()
        self.NumberOFPatients = tk.Label(self,textvariable=self.PatientValueNum,font=fontStyle)
        self.NumberOFPatients.pack(pady='50', side='top')
        self.DoctorValueNum = tk.StringVar()
        self.NumberOfDcotors = tk.Label(self,textvariable=self.DoctorValueNum,font=fontStyle)
        self.NumberOfDcotors.pack(pady='50', side='top')
        self.BackButton = tk.Button(self,command=lambda:controller.show_frame(AdminChoices))
        self.BackButton.configure(text='Go Back')
        self.BackButton.pack(pady='20', side='top')
        

db1 = Database()


app = ValitudoApps()
app.geometry("700x700")
app.title("Valitudo")
app.mainloop()


