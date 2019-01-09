import sqlite3

conn = sqlite3.connect('task1.db')
c = conn.cursor()

def create_table():
    
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL , datestamp TEXT, keyword TEXT, value REAL)')
    
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222,'2018-01-01','python',5)" )
        
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()
