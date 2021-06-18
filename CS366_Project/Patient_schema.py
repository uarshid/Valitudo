from tkinter import *
import sqlite3
from sqlite3 import Error

#con=sqlite3.connect(':memory:')
#To execute SQLite statements in Python, you need a cursor object. 
# You can create it using the cursor() method.
#coursorObj = con.cursor()
# Now we can use the cursor object to call the execute() method to execute any SQL queries.


def sql_connection():
    try:
        con=sqlite3.connect(':memory:')
        #print("connection is established: Database is created in memory")
        return con
    except Error:
        print(Error)
con = sql_connection()

def sql_table_Patient(con):
    cursorObj=con.cursor()
    #cursorObj.execute("DROP TABLE IF EXISTS Patient")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Patient2 (id integer PRIMARY KEY, name text, gender text, Date_of_Birth text)")
    con.commit()

sql_table_Patient(con)

def Insert(con, id, name,  gender, Date_of_Birth):
    cursorObj=con.cursor()
    cursorObj.execute("INSERT INTO Patient2 VALUES (?, ?, ?, ?)", (id, name, gender, Date_of_Birth))
    a=cursorObj.fetchall()
    cursorObj.execute("SELECT * FROM Patient2")
    a=cursorObj.fetchall()
    print(a)
    #return a

Insert(con, 1, 'Andrew', 'male', '2001-02-06' )
Insert(con, 2, 'Andria', 'female', '1999-04-21' )
Insert(con, 3, 'john', 'male', '1995-01-15' )


def Update(con, name,  gender, Date_of_Birth,id):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Patient2 SET name = ?,gender=?, Date_of_Birth = ? where id = ?',(name, gender,Date_of_Birth,id))
    cursorObj.execute("SELECT * FROM Patient2")
    s=cursorObj.fetchall()
    print(s)
    return s

Update(con,'sam','male', '2001-02-06',1)
Update(con,'john','male', '1990-01-15',3)
def Search(con, id):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Patient2 where id = ?", (id,))
    
    searchResults = cursorObj.fetchall()
    print(searchResults)
    return searchResults
   
Search(con,1)
Search(con, 3)

def Delete(con, id):
    cursorObj = con.cursor()
    cursorObj.execute("DELETE FROM Patient2 WHERE id = ?", (id,))

Delete(con,2)

def Display(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Patient2")
    records = cursorObj.fetchall()
    print(records)
    return records
 
Display(con)

# Tkinter Window
class Application:
    def __init__(self,master):
        self.master=master

        #creating the frames in the master
        self.left=Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right=Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)
        #labels for the window
        self.heading=Label(self.left, text="Patient Record", font=('arial 40 bold'), fg='white',bg='lightgreen')
        self.heading.place(x=0,y=0)


#creating the object
root=Tk()
b=Application(root)

#resolution of the window
root.geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False,False)

#end the loop
root.mainloop()



