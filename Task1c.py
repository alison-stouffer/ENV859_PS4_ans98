##---------------------------------------------------------------------
## Interactive Python Script for Buffering
##
## Description: Create stream buffer from user input.
##
##
## Created: Fall 2020
## Author: alison.stouffer@duke.edu (for ENV859)
##---------------------------------------------------------------------

#%% Import Modules and Set Environment

#Import modules:
import sys, arcpy

#Set workspace:
arcpy.env.workspace = "V:\\_ProblemSets\\ENV859_PS4_ans98\\Data"

#Allow output to be overwritten:
arcpy.env.overwriteOutput = True

#%% Set Input and Output Feature Classes

#Set input feature class (FC) to streams shapefile in Data folder:
inputFC = "streams.shp"
#Set output feature class (FC) name through user input and store in Scratch folder:
outputFC = sys.argv[2]

#%% Create Buffer From User Input

#Set buffer distance through user input:
streamBuffer = sys.argv[1]

#Create feature class with buffered streams:
arcpy.Buffer_analysis(inputFC,outputFC,streamBuffer,'','','ALL')

#%% Display Messages

print(arcpy.GetMessages())
