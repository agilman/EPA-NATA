
import os
import sqlite3
import re




conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

        


path = "/".join(os.path.realpath(__file__).split('/')[:-2])+"/Data/"
filePath = path+"DIESEL_PM.txt"


f = open(filePath,'r')
tractLines = f.readlines()

def addToDb(geoid,conc):
    c.execute('SELECT id FROM nataMaps_tract WHERE geoid='+geoid)
    tractId = c.fetchone()[0]

    insertLine = str("INSERT INTO nataMaps_dieselpm (tract_id,total_conc) VALUES(%s,'%s')" %(geoid,conc) ) 
    
    c.execute(insertLine)
    

for tract in tractLines:
    d = tract.split(',')
    
    if d[0].count("OR"): #check state
        if d[4]!='"00000000000"': #check that its not a cummulative for state or county
            geoid = str(d[4][1:-1])
            conc = float(d[20])

            addToDb(geoid,conc)

f.close()
conn.commit()

conn.close()



