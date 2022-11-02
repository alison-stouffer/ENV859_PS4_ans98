##---------------------------------------------------------------------
## Feature Class and Point Intersection
##
## Description: Create point & determine whether it intersects a feature class.
##
##
## Created: Fall 2020
## Author: alison.stouffer@duke.edu (for ENV859)
##---------------------------------------------------------------------

#%% Import Modules, Set Environment, and Check Product

#Import modules:
import sys, arcpy

#Set workspace:
arcpy.env.workspace = "V:\\_ProblemSets\\ENV859_PS4_ans98\\Data"

#Allow output to be overwritten:
arcpy.env.overwriteOutput = True

#%% Set User Inputs

featureClass = sys.argv[1]
field = sys.argv[2]

#%% Create Point

point = arcpy.Point()
point.X = 587000
point.Y = 265000

#%% Create Search Cursor & Iterate Through Each Feature

#Create search cursor:
rows = arcpy.da.SearchCursor(featureClass, ['Shape@', field])
#Iterate through each row:
for row in rows:
    #Assign feature's shape to new variable:
    recShape = row[0]
    #Create if statement:
    if point.within(recShape):
        fieldValue = row[1]
        #Print the user-specified field value:
        print("The " + field + " is " + fieldValue)
    else:
        continue
