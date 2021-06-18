import patient


MENU_PROMT="""--   PATIENT TABLE --

Please choose one of these options:

1) ADD a new patient
2) See all patients
3) Find a patient by name
4) Remove a patient
5)Exit

Your Selection:"""

def menu():
    connection = patient.connect()
    patient.Create_PatientTable(connection)

    while(user_input := input(MENU_PROMT)) != "5":
        if user_input =="1":
            firstname=input("Enter Patient's first name: " )
            lastname=input("Enter Patient's last name: " )
            gender=input("Enter Patient's gender: " )
            dateOfBirth=input("Enter Patient's date of birth: " )

            patient.Insert_Data(connection,firstname, lastname, gender, dateOfBirth)
        elif user_input =="2":
            patients=patient.GetData(connection)

            for p in patients:
                print(p) 
        elif user_input =="3":
            pass
        elif user_input =="4":
            remove=patient.delete(connection,Id)

            for r in remove:
                print(r)
        else:
            print("Invalid input, Please try again!")


menu()