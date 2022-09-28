#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Kelsey Husted (kelsey.husted@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = 'data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file=file_name, mode = 'r')

#Read contents of file into a list
lineString = file_object.readline()

#Pretend we read or extract one line of data from the file
while lineString:
    
    #Check to see if the lineString is a data line
    if lineString[0] =="#" or lineString[0] == 'u':
        lineString = file_object.readline()
        continue

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0] # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude
    
    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    
    #Move to the next line in the file
    lineString = file_object.readline()

#CLose the file object
file_object.close()

