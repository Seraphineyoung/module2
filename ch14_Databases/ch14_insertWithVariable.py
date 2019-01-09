
#####################  TASK 1  #########################
#Create a table and insert data

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('task1.db')
c = conn.cursor()

def create_table():
    
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL , datestamp TEXT, keyword TEXT, value REAL)')
    
#def data_entry():
#    c.execute("INSERT INTO stuffToBuild VALUES(142233222,'2018-01-01','python',5)" )
#data_entry() 
    
    
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0,10)
    c.execute('INSERT INTO stuffToBuild( unix,datestamp,keyword,value) VALUES(?,?,?,?)', (unix,date,keyword,value))
    
    conn.commit()
    
create_table()    
        
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
    
c.close()
conn.close()
    





























