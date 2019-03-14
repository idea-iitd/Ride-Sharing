import numpy as np
import timeit
from sklearn.neighbors import BallTree
from math import radians, cos, sin, asin, sqrt
import pickle
import sys

nodes = open('ny_location')

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

for index in range(len(listCoords) ):
	nodeId = listCoords[index][1]
	nodesList[ index ] = nodeId
	listCoords[index] = listCoords[index][0]

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) 
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = list(map(radians, [lon1, lat1, lon2, lat2]))
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def parseTimeFromString(s):
	components = s.split(':')
	return (int(components[0])*60 + int(components[1]))//15

def parseTimeFromStringFloat(s):
	components = s.split(':')
	return (int(components[0])*60 + int(components[1]) + int(components[2])/60)

def getMeTime(s):
	# return parseTimeFromString(s.split(" ")[1])
	return parseTimeFromStringFloat(s.split(" ")[1])

def getMeDate(s):
	return int((s.split(" ")[0]).split("-")[2])

# print(len(listCoords))
tree = BallTree( [ list(map( radians, [a, b])) for (a,b) in listCoords ], metric="haversine")                

fileName = sys.argv[1]
traj = open(fileName)
traj.readline()
traj.readline()
trajPick = {}
for timeBucket in range(96):
	trajPick[timeBucket] = {}

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def mainFun():
	query = 1
	while( 1 ):
		# (long, lat)
		# if( not(query%1000) ):
		# 	save_obj(trajPick, "pickups" + fileName )	
		# 	print query
		query += 1
		lineRead = traj.readline()
		if( lineRead == ""):
			break
		tokens = lineRead.split(",")
		try:
			source  = [ float(latLong) for latLong in tokens[5:7] ] 	
			destination = [ float(latLong) for latLong in tokens[9:11] ]
			dist, indS = tree.query( [list(map(radians, [ source[1], source[0] ] ) )] )
			dist, indD = tree.query( [list(map(radians, [ destination[1], destination[0] ] ) )] )

			timeBucketStart = int(getMeTime( tokens[1] ))
			timeBucketEnd = int(getMeTime( tokens[2] ))
			
			startDate = getMeDate(tokens[1])
			price = float(tokens[17])
			
			print(str(startDate)+' '+str(indS[0][0])+' '+str(timeBucketStart)+' '+str(indD[0][0])+' '+str(price))
		except:
			continue
		# if( indS[0][0] not in trajPick[timeBucket] ):
		# 	trajPick[ timeBucket ][ indS[0][0] ] = {}

		# try:
		# 	trajPick[timeBucket][ indS[0][0] ][ indD[0][0] ] += 1
		# except:
		# 	trajPick[timeBucket][ indS[0][0] ][ indD[0][0] ] = 1

	return 0

mainFun()
# print(timeit.timeit(mainFun, number = 1))

