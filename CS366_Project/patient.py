import sqlite3

conn = sqlite3.connect("patientdb.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Patient")
c.execute("DROP TABLE IF EXISTS Doctor")

def create_tables():
    c.execute(
        "CREATE TABLE IF NOT EXISTS Patient (Id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, gender TEXT, dateOfBirth TEXT);"
        )

    c.execute(
        "CREATE TABLE IF NOT EXISTS Doctor (Id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT,address TEXT, qualification TEXT, field TEXT,joing_date TEXT);"
    )
def Insert_Data():
   
    c.execute("INSERT INTO Patient(firstname, lastname, gender, dateOfBirth) VALUES ('Md', 'Ahmed','M','04-07-1999')")
    c.execute("INSERT INTO Doctor(firstname, lastname, gender, address, qualification,field, joining_date) VALUES ('John', 'Doe','M','M.D.','Cardio','01-17-1993')")
    

def Display_Patient_table():
   dis=c.execute("SELECT * FROM Doctor").fetchall()
   print(dis)

def Display_Doctor_table():
    print(c.execute("SELECT * FROM Doctor").fetchall())
   





"""
# SQL Inquery
Create_Patient_Table = "CREATE TABLE IF NOT EXISTS patient_table (Id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, gender TEXT, dateOfBirth TEXT);"
Insert_Info = "INSERT INTO patient_table(firstname, lastname, gender, dateOfBirth) VALUES (?, ?, ?, ?);"
Get_Data = "SELECT * FROM patient_table;"
Get_Data_By_Name = "SELECT * FROM patient_table WHERE lastname = ?;"
delete_data= "DELETE  FROM patient_table WHERE Id = ?"

def connect():
    return sqlite3.connect("patient.db")

def Create_PatientTable(connection):
    with connection:
        connection.execute(Create_Patient_Table)
def Insert_Data(connection,Id,firstname, lastname, gender, dateOfBirth):
    with connection:
        connection.execute(Insert_Info,(Id,firstname, lastname, gender, dateOfBirth))
def GetData(connection):
    with connection:
        return connection.execute(Get_Data).fetchall()

def GetDataByName(connection,lastname):
    with connection:
        return connection.execute(Get_Data_By_Name, (lastname,)).fetchall()

def delete(connection,Id):
    with connection:
        return connection.execute(delete_data,(Id,)).fetchall()  """








