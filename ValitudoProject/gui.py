import tkinter as tk
import tkinter.ttk as ttk
from  Database import Database
from DataClasses import *
import PyQt5




import tkinter as tk
import pygubu


LARGE_FONT= ("Verdana", 12)

#controller
class SeaofBTCapp(tk.Tk):

    def __init__(self,*args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        self.doctorID = 0

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        
        self.frames = {}
        self.pages = (StartPage, DoctorLoginPage, PageTwo,SearchForPatient,createAppointment,PatientManagement,Choices,AddPatient,DeletePatient,PatientChoices)
        for F in self.pages:
            frame = F(container, self,self.pages)

            self.frames[F] = frame

            frame.grid(row=0,column=0,sticky='nsew')

        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


    def changeDoctorID(self,newID):
        self.doctorID = newID
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self,parent)

        self.patientImage = tk.PhotoImage(file="/Users/nanabonsu/Desktop/Valitudo/ValitudoProject/patientLogin.png")
        self.patientLogo = tk.Canvas(self)
        self.patientLogo.create_image(0,0,anchor="ne",image=self.patientImage)
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
        self.button20 = tk.Button(self)
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
                            command=lambda: controller.show_frame(PageTwo))
      #  self.button2.pack()
        
        self.loginButton = tk.Button(self,text='Log In',command=self.validate)
        self.loginButton.pack()

    def sendID(self,ID):
         returned = self.database.findDoctorWithSpecificID(ID)
         tupleReturned = returned[0]
         docName =  "Welcome Doctor "  + tupleReturned[1] +  " " + tupleReturned[2]
         self.controller.frames[self.controller.pages[2]].DoctorIDValue.set(docName)

    def validate(self):
        doctorInfo = self.database.findDoctorWithSpecificID((self.login_input.get()))
        if (len(doctorInfo) == 0):
                    self.errorlabel.configure(text="Invalid login please check again, or register in the database")
                    self.errorlabel.pack()
        else:
            self.sendID(self.login_input.get())
            self.loginButton.configure(command=lambda:self.controller.show_frame(PageTwo))

      
class PageTwo(tk.Frame,DataThings):

    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()
        
        self.DoctorIDValue = tk.StringVar()
        
        self.headingFrame = tk.Frame(self,bg="#FFBB00",bd=5)
        self.headingFrame.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.13)

        self.headingLabel = tk.Label(self.headingFrame, textvariable=self.DoctorIDValue, bg='black', fg='white', font=('Courier',15))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
       
        

        self.label = tk.Label(self, font=LARGE_FONT,textvariable=self.DoctorIDValue)
       

        self.actionFrame = tk.Frame(self,bg="sky blue")
        self.actionFrame.place(relheight='0.7', relwidth='0.82', relx='0.1', rely='0.2')

    
        button1 = tk.Button(self.actionFrame, text="Search for Patient",
                            command=lambda: controller.show_frame(SearchForPatient))
        button1.place(anchor='nw', relheight='0.15', relwidth='0.26', relx='0.2', rely='0.18')


        makeAppointmentButton = tk.Button(self.actionFrame, text="Make Appointment",command=lambda: controller.show_frame(createAppointment))
        makeAppointmentButton.place(anchor='nw', relheight='0.15', relwidth='0.25', relx='0.62', rely='0.18')

        myPatientsButton = tk.Button(self.actionFrame,text=" View My Patients")
        #chnage
        myPatientsButton.place(anchor='nw', relheight='0.15', relwidth='0.26', relx='0.21', rely='0.54')


        AddOrDeletePatientsButton = tk.Button(self.actionFrame,text="Patient Management",command=lambda: controller.show_frame(PatientManagement))
        AddOrDeletePatientsButton.place(anchor='nw', relheight='0.14', relwidth='0.26', relx='0.64', rely='0.53')

        logOutButton = tk.Button(self.actionFrame,text="Log Out",command=lambda: controller.show_frame(DoctorLoginPage))
        logOutButton.place(anchor='nw', relheight='0.14', relwidth='0.26', relx='0.64', rely='0.8')
    


class SearchForPatient(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()

        self.headingFrame = tk.Frame(self,bg="#FFBB00",bd=5)
        self.headingFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

        self.headingLabel = tk.Label(self.headingFrame, text="Search For Patient By ID", bg='black', fg='white', font=('Courier',15))
        self.headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
       

        backButton = tk.Button(self,text="Cancel",command=lambda:controller.show_frame(PageTwo))
        backButton.place(relx=0.28,rely=0.91, relwidth=0.18,relheight=0.08)
    
        self.searchResultsFrame = tk.Frame(self,bg='black')
        self.searchResultsFrame.place(relheight='0.61', relwidth='0.82', relx='0.1', rely='0.3')
        
      #  tk.Scrol

        self.searchinput = tk.StringVar()
        self.searchFeild = tk.Entry(self.searchResultsFrame,textvariable=self.searchinput)
        self.searchFeild.place(anchor='nw', relheight='0.1', relx='0.26', rely='0.14', x='0', y='0')

        searchButton = tk.Button(self.searchResultsFrame,text="Search",command=self.getPatient)
        searchButton.place(anchor='nw', relx='0.66', rely='0.14',relheight='0.1')

        self.display = tk.Label(self.searchResultsFrame,bg="#FFBB00",bd=5)

    def getPatient(self):
        enteredID = self.searchinput.get()
        returned = self.database.findPatientOnlyID(int(enteredID))
        #put here mesage if searched pateint is not in database
        values = returned[0]
        printString = " \n + First name: {} \n\n Last name: {} \n\n DOB: {} \n\n  Age: {} \n\n Gender: {} \n\n Address: {} \n\n".format(values[1],values[2],values[3],values[4],values[5],values[6])  
        self.display.configure(text=printString)
        self.display.place(anchor='nw', relheight='0.46', relwidth='0.51', relx='0.21', rely='0.34')

#Appointment Creation Frame
class createAppointment(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.database = Database()


        
        self.frammeHeading = tk.Frame(self,bg="#FFBB00",bd=5)
        self.frammeHeading.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

        headingLabel = tk.Label(self.frammeHeading, text="Make Appointment", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        self.detailsFrame = tk.Frame(self,bg='black')
        self.detailsFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)


        lb1 = tk.Label(self.detailsFrame,text="Patient ID : ", bg='black', fg='white')
        lb1.place(relx=0.05,rely=0.1, relheight=0.1)

        self.patientIDValue = tk.StringVar()
        patientIDEntry = tk.Entry(self.detailsFrame,textvariable=self.patientIDValue)
        patientIDEntry.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08) 

        dateLabel = tk.Label(self.detailsFrame,text="Appointment Date(MM/DD/YYYY) : ", bg='black', fg='white')
        dateLabel.place(relx=0.05,rely=0.25, relheight=0.08)

        self.dateEntryValue = tk.StringVar()
        dateEntry = tk.Entry(self.detailsFrame,textvariable=self.dateEntryValue)
        dateEntry.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)

        timeLabel = tk.Label(self.detailsFrame,text="Time: ", bg='black', fg='white')
        timeLabel.place(relx=0.05,rely=0.40, relheight=0.08)
        
        self.timeEntryValue = tk.StringVar()
        timeEntry = tk.Entry(self.detailsFrame,textvariable=self.timeEntryValue)
        timeEntry.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08)

        purposeLabel = tk.Label(self.detailsFrame,text="Purpose:", bg='black', fg='white')
        purposeLabel.place(relx=0.05,rely=0.55, relheight=0.08)
  
        self.purposeEntry = tk.StringVar()
        purposeEntry = tk.Entry(self.detailsFrame,textvariable=self.purposeEntry)        
        purposeEntry.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

        self.SubmitBtn = tk.Button(self,text="Create Appointment",bg='#d1ccc0', fg='black',command=self.makeAppointment)
        self.SubmitBtn.place(relx=0.28,rely=0.91, relwidth=0.18,relheight=0.08)

        self.successFrame = tk.Frame(self,bg='black')


        self.endButton = tk.Button(self,text="Back to Home Page",command=lambda:controller.show_frame(PageTwo))
        



       # self.successMessage = 

        self.cancelButton = tk.Button(self,text="Quit",bg='#f7f1e3', fg='black', command=lambda:controller.show_frame(PageTwo))
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
        self.logInButton.pack(side="top")
        self.goBackButton = tk.Button(self,text="Cancel",command=lambda:controller.show_frame(PageTwo))
        self.goBackButton.pack(side="top")

        self.addPatientButton = tk.Button(self,text="Add New Patient",command=lambda:controller.show_frame(AddPatient))
        self.addPatientButton.pack(side="top")
        

        self.errorlabel = tk.Label(self)

     def validate(self):
        patientInfo = self.database.findPatientOnlyID((self.login_input.get()))
        if (len(patientInfo) == 0):
                    self.errorlabel.configure(text="Invalid login please check again, or register patient in the database")
                    self.errorlabel.pack()
        else:
            newStatus = self.login_input.set("")
            self.idEntry.configure(textvariable= newStatus)
            self.logInButton.configure(command=lambda:self.controller.show_frame(Choices))

class Choices(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.label1 = tk.Label(self)
        self.label1.configure(text="What would you like to do for this patient?")
        self.label1.pack(pady='20', side='top')

        self.DeletePatientButton = tk.Button(self,command=lambda:controller.show_frame(DeletePatient))
        self.DeletePatientButton.configure(text='Delete Patient')
        self.DeletePatientButton.pack(pady='20', side='top')

        self.UpdatePatientDetails = tk.Button(self)
        self.UpdatePatientDetails.configure(text='Update Patient Details')
        self.UpdatePatientDetails.pack(side='top')

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
        self.label9.configure(background='sky blue', text='Add Patient')
        self.label9.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
        self.titleFrame.configure(background='gold', borderwidth='5', height='200', width='200')
        self.titleFrame.place(anchor='nw', relheight='0.13', relwidth='0.5', relx='0.26', rely='0.03', x='0', y='0')
        
        self.cancelButton = tk.Button(self,command=lambda:controller.show_frame(PageTwo))
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
       # self.endButton = tk.Button(self,text="Back to Home Page",command=lambda:controller.show_frame(PageTwo))
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

       # self.cancelButton = tk.Button(self,text="Quit",bg='#f7f1e3', fg='black', command=lambda:controller.show_frame(PageTwo))
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

class updatePatient():
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
            self.label9.configure(background='sky blue', text='Add Patient')
            self.label9.place(anchor='nw', relheight='1.0', relwidth='1.0', x='0', y='0')
            self.titleFrame.configure(background='gold', borderwidth='5', height='200', width='200')
            self.titleFrame.place(anchor='nw', relheight='0.13', relwidth='0.5', relx='0.26', rely='0.03', x='0', y='0')
            
            self.cancelButton = tk.Button(self,command=lambda:controller.show_frame(PageTwo))
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
class PatientChoices(tk.Frame):
    def __init__(self, parent, controller,pages):
        tk.Frame.__init__(self, parent)

        self.IdRequestLabel = tk.Label(self)
        self.IdRequestLabel.configure(text='Please enter your patient id')
        self.IdRequestLabel.pack(pady='30', side='top')
        self.entry1 = tk.Entry(self)
        self.entry1.pack(pady='20', side='top')

        self.LoginButton = tk.Button(self)
        self.LoginButton.configure(text='Log In')
        self.LoginButton.pack(padx='30', pady='30', side='top')
        self.cancelButton = tk.Button(self,command=lambda:controller.show_frame(StartPage))
        self.cancelButton.configure(text='Cancel')
        self.cancelButton.pack(side='top')
        



db1 = Database()
db1.deleteDataBase()
2984059923
db = Database()

db.deleteAllAppintments()
doctor = Doctor(2345,"Nana","Bonsu",345,34,"male","2350 Ryer Avenue","cardio")
db.deleteDoctorbyID(doctor)

pharm = Pharmacist(5678,"Apple","Things",34,"Female","34 Cupertino St PHarm")
db.deletePharmacistByID(pharm)

patient2 = Patient(3456,"Deez","John","2/3/44",34,"Female","4533 Martin St")
db.deletePatient(patient2)
patient = Patient(3456,"Deez","John","2/3/44",34,"Female","4533 Martin St")

db.insertDoctor(doctor)
db.insertPharmacist(pharm)
db.insertNewPatient(patient,doctor,pharm)


app = SeaofBTCapp()
app.geometry("700x700")
app.mainloop()


'''


        self.detailsFrame = tk.Frame(self,bg='black')
        self.detailsFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)


        lb1 = tk.Label(self.detailsFrame,text=" First Name: ", bg='black', fg='white')
        lb1.place(relx=0.05,rely=0.1, relheight=0.1)

        self.firstNameValue = tk.StringVar()
        patientNameEntry = tk.Entry(self.detailsFrame,textvariable=self.firstNameValue)
        patientNameEntry.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.08) 

        dateLabel = tk.Label(self.detailsFrame,text="Last Name: ", bg='black', fg='white')
        dateLabel.place(relx=0.05,rely=0.25, relheight=0.08)

        self.lastNameValue = tk.StringVar()
        lastnameEntry = tk.Entry(self.detailsFrame,textvariable=self.lastNameValue)
        lastnameEntry.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.08)

        timeLabel = tk.Label(self.detailsFrame,text="DOB: ", bg='black', fg='white')
        timeLabel.place(relx=0.05,rely=0.40, relheight=0.08)
        
        self.DOBvalue = tk.StringVar()
        DOBEntry = tk.Entry(self.detailsFrame,textvariable=self.DOBvalue)
        DOBEntry.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08)

        purposeLabel = tk.Label(self.detailsFrame,text="Age:", bg='black', fg='white')
        purposeLabel.place(relx=0.05,rely=0.55, relheight=0.08)
  
        self.AgeEntryValue = tk.StringVar()
        AgeEntry = tk.Entry(self.detailsFrame,textvariable=self.AgeEntryValue)        
        AgeEntry.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

        genderLabel = tk.Label(self.detailsFrame,text="Gender:", bg='black', fg='white')
        genderLabel.place(relx=0.05,rely=0.55, relheight=0.08)

        self.genderEntryValue= tk.StringVar()
        genderEntry = tk.Entry(self.detailsFrame,textvariable=self.AgeEntry)        
        genderEntry.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

        address = tk.Label(self.detailsFrame,text="Gender:", bg='black', fg='white')
        genderLabel.place(relx=0.05,rely=0.55, relheight=0.08)
'''