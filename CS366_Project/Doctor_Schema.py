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

def sql_table_Doctor(con):
    cursorObj=con.cursor()
    #cursorObj.execute("DROP TABLE IF EXISTS Patient")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Doctor_Table (id integer PRIMARY KEY, name text, gender text, Date_of_Birth text)")
    con.commit()

sql_table_Doctor(con)

def Insert(con, id, name,  gender, Date_of_Birth):
    cursorObj=con.cursor()
    cursorObj.execute("INSERT INTO Doctor_Table VALUES (?, ?, ?, ?)", (id, name, gender, Date_of_Birth))
    a=cursorObj.fetchall()
    cursorObj.execute("SELECT * FROM Doctor_Table")
    a=cursorObj.fetchall()
    print(a)


Insert(con, 1, 'Md', 'male', '1985-02-06' )
Insert(con, 2, 'Priya', 'female', '1978-04-21' )
Insert(con, 3, 'Roni', 'male', '1992-01-15' )


def Update(con, name,  gender, Date_of_Birth,id):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Doctor_Table SET name = ?,gender=?, Date_of_Birth = ? where id = ?',(name, gender,Date_of_Birth,id))
    cursorObj.execute("SELECT * FROM Doctor_Table")
    s=cursorObj.fetchall()
    print(s)
    return s

Update(con,'Ahmed','male', '2001-02-06',1)
Update(con,'Roni','male', '1990-01-15',3)
def Search(con, id):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Doctor_table where id = ?", (id,))
    
    searchResults = cursorObj.fetchall()
    print(searchResults)
    return searchResults

Search(con,1)
Search(con, 3)

def Delete(con, id):
    cursorObj = con.cursor()
    cursorObj.execute("DELETE FROM Doctor_Table WHERE id = ?", (id,))

Delete(con,2)

def Display(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Doctor_Table")
    records = cursorObj.fetchall()
    print(records)
    return records
 
Display(con)



