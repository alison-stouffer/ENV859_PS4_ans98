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

#%% Set Input Feature Classes

#Set input feature class (FC) to roads shapefile in Data folder:
inputFC = "Roads.shp"

#%%