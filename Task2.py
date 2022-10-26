##---------------------------------------------------------------------
## Selecting Road Types
##
## Description: Iterate through and select road features with desired code type.
##
##
## Created: Fall 2020
## Author: alison.stouffer@duke.edu (for ENV859)
##---------------------------------------------------------------------

#%% Import Modules and Set Environment

#Import modules:
import arcpy

#Set workspace:
arcpy.env.workspace = "V:\\_ProblemSets\\ENV859_PS4_ans98\\Data"

#Allow output to be overwritten:
arcpy.env.overwriteOutput = True

#%% Set Input Feature Class

#Set input feature class (FC) to roads shapefile in Data folder:
inputFC = "Roads.shp"


#%% List Desired Road Type Classes

#Create multi-value string variable with desired road type classes:
roadTypeClass = "0;201;203"
#Create list from multi-value string variable above:
listRdTypeClass = roadTypeClass.split(";")

#%% Create New Feature Classes From Road Type Class Selection

for roadclass in listRdTypeClass:

    #Set output feature class (FC) name and store in Scratch folder:
    outputFC = "V:\\_ProblemSets\\ENV859_PS4_ans98\\Scratch\\roads_"+str(roadclass)+".shp"
    #Set where clause:
    where_clause = 'ROAD_TYPE =' + roadclass
    
    #Select roads with desired class and write to new feature class:
    arcpy.Select_analysis(inputFC, outputFC, where_clause)

#%% Display Messages

print(arcpy.GetMessages())
