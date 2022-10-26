##---------------------------------------------------------------------
## Interactive Python Script for Buffering
##
## Description: Create 1,000 meter buffer from streams.
##
##
## Created: Fall 2020
## Author: alison.stouffer@duke.edu (for ENV859)
##---------------------------------------------------------------------

#%% Import Modules and Set Variables

#Import modules:
import arcpy

#Set input feature class (FC) to streams shapefile in Data folder:
inputFC = "V:\\_ProblemSets\\ENV859_PS4_ans98\\Data\\Streams.shp"
#Set output feature class (FC) name to StrmBuff1km and store in Scratch folder:
outputFC = "V:\\_ProblemSets\\ENV859_PS4_ans98\\Scratch\\StrmBuff1km.shp"

#%% Create Buffer

#Set buffer distance:
streamBuffer = "1000 meters"

#Create feature class with buffered streams:
arcpy.Buffer_analysis(inputFC,outputFC,streamBuffer,'','','ALL')

#%% Display Messages

print(arcpy.GetMessages())
