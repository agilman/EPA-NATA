
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
    c.execute(str('SELECT id FROM nataMaps_tract WHERE geoid="%s"' %(geoid) ))
    tmp = c.fetchone()
    if tmp:
        tractId = tmp[0]

        insertLine = str("INSERT INTO nataMaps_dieselpm (tract_id,total_conc) VALUES(%s,'%s')" %(tractId,conc) ) 

        #update population info for tract based on info from diesel file...
    
        c.execute(insertLine)
    
#on first pass, fill data about state name, county name and tract population
stateData = {}

for tract in tractLines:
    d = tract.split(',')
    state = str(d[0][1:-1])
    
    if state == "OR": #check state
        if d[4]!='"00000000000"': #check that its not a cummulative for state or county
            geoid = str(d[4][1:-1])
            conc = float(d[20])

            population = int(d[5])
            state = str(d[0][1:-1])
            stateFP = geoid[:2]
            county = str(d[2][1:-1])
            countyFP = int(geoid[2:5])

            addToDb(geoid,conc)
            if stateFP not in stateData:
                stateLine = str('UPDATE nataMaps_tract SET stateName="%s" WHERE stateFP=%s;' %(state,stateFP))
                c.execute(stateLine)
                stateData[stateFP]={'stateName':state,'counties':{ }   }
                stateData[stateFP]['counties'][countyFP] = {'countyName':county,'tracts':{} }
                stateData[stateFP]['counties'][countyFP]['tracts'][geoid] = population

                countyLine = str('UPDATE nataMaps_tract SET countyName="%s" WHERE stateFP=%s AND countyFP=%s;' %(county,stateFP,countyFP))
                c.execute(countyLine)

                populationLine = str('UPDATE nataMaps_tract SET population="%s" WHERE geoid="%s";' %(population,geoid))
                c.execute(populationLine)

            else:
                if countyFP not in stateData[stateFP]['counties']: #if state exists but county doesnt...
                    
                    countyLine = str('UPDATE nataMaps_tract SET countyName="%s" WHERE stateFP=%s AND countyFP=%s;' %(county,stateFP,countyFP))
                    c.execute(countyLine)
                    
                    stateData[stateFP]['counties'][countyFP] = {'countyName':county,'tracts':{} }
                    stateData[stateFP]['counties'][countyFP]['tracts'][geoid] = population

                    populationLine = str('UPDATE nataMaps_tract SET population="%s" WHERE geoid="%s";' %(population,geoid))
                    c.execute(populationLine)
                else:
                    if geoid not in stateData[stateFP]['counties'][countyFP]['tracts']: #if county exists, but tract doesn't...
                        populationLine = str('UPDATE nataMaps_tract SET population="%s" WHERE geoid="%s";' %(population,geoid))
                        c.execute(populationLine)
                        stateData[stateFP]['counties'][countyFP]['tracts'][geoid] = population

f.close()
conn.commit()

conn.close()



