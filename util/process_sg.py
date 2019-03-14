import numpy as np
import timeit
from sklearn.neighbors import BallTree
from math import radians, cos, sin, asin, sqrt
import pickle
import sys
import os

nodes = open('sg_location')

lineNum = 0

listCoords = []
while(1):
    line = nodes.readline()
    if( line == "" ):
        break
    lineData = line.split(",")
    listCoords.append( ( ( float(lineData[1]), float(lineData[2]) ), int(lineData[0]) )  ) 

nodesList = [0]*len(listCoords)    

# listCoords.sort(key=lambda tup: (tup[0][0], tup[0][1]) )	

for index in range( len(listCoords) ):
	nodeId = listCoords[index][1]
	nodesList[ index ] = nodeId
	listCoords[index] = listCoords[index][0]

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) 
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def parseTimeFromString(s):
	components = s.split(':')
	return int(components[0])*60 + int(components[1])

def getMeTime(s):
	return parseTimeFromString( s.split(" ")[2] )

def getMeDate(s):
	return int( s.split(" ")[1].split("/")[0] )

tree = BallTree( [ list(map( radians, [a, b])) for (a,b) in listCoords ], metric="haversine")                

# fileName = sys.argv[1]
# traj = open( fileName )

path = './'
listing = os.listdir(path)
cabs = {}
for infile in listing:
	# print infile
	traj =  open(path + infile, 'r')
	if(infile[0:4] != "trip"):
		continue
	
	while( 1 ):
		lineRead = traj.readline()
		# exit
		if( lineRead == ""): 
			break

		tokens = lineRead.split(",")
		try:
			source  = [ float(latLong) for latLong in tokens[4:6] ] 	
			destination = [ float(latLong) for latLong in tokens[6:8] ]
			if( tokens[8] not in cabs):
				cabs[ tokens[8] ] = 1 		
		except:
			continue

		dist, indS = tree.query( [ list(map(radians, [ source[1], source[0] ] )) ] )
		dist, indD = tree.query( [ list(map(radians, [ destination[1], destination[0] ] )) ] )

		timeBucket = getMeTime( tokens[2] )
		# print timeBucket

		# timeBucketD = getMeTime( lineRead.split(",")[3] ) 

		date = getMeDate( tokens[2] )
		revenue = tokens[10].lstrip()
		print(str(date)+' '+str(indS[0][0])+' '+str(timeBucket)+' '+str(indD[0][0])+' '+revenue)
	# print "LEN", len(cabs)
	# break