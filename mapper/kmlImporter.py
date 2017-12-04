
import os
import sqlite3
import re



def parseCoordinates(coords):
    #remove last 0.0 coordinate
    myCoords = coords.split(',')[:-1]

    #separate by pairs
    latlngPairs = []
          
    for i in range(int(len(myCoords)/2)):
        lat = myCoords[i*2].strip('0.0 ')
        lng = myCoords[i*2+1]
        latlngPairs.append((lat,lng))

    return latlngPairs

    
def parseTractData(tract):
    
    stateFP = re.findall(r'<SimpleData name="STATEFP">(\d+)</SimpleData>',tract)[0]
    countyFP = re.findall(r'<SimpleData name="COUNTYFP">(\d+)</SimpleData>',tract)[0]
    geoid = re.findall(r'<SimpleData name="GEOID">(\d+)</SimpleData>',tract)[0]

    coordinates = re.findall(r'<coordinates>(.*?)</coordinates>',tract)[0]
    parsedCoords = parseCoordinates(coordinates)


    return (stateFP,countyFP,geoid,parsedCoords)


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def addToDb(tract):
    c.execute("INSERT INTO nataMaps_tract (stateFP, countyFP, geoid) VALUES(%s,%s,%s)" %(tract[0],tract[1],tract[2]) ) 

    tractId = c.lastrowid
    for coordPair in tract[3]:
        line =str("INSERT INTO nataMaps_tractpoint (tract_id, lat, lng) VALUES(%s,%s,%s)" %(tractId,coordPair[0],coordPair[1]))
        c.execute(line)
        


path = "/".join(os.path.realpath(__file__).split('/')[:-2])+"/Data/"
filePath = path+"cb_2016_41_tract_500k.kml"


f = open(filePath,'r')
kmlText = f.read()


markerPattern = r'<Placemark (.*?)</Placemark>'
tractTuples = re.findall(markerPattern, kmlText, re.DOTALL)


for tract in tractTuples:
    parsed = parseTractData(tract)
    addToDb(parsed)

f.close()
conn.commit()

conn.close()



