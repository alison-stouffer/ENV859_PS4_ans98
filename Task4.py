##---------------------------------------------------------------------
## ArcGIS Messages
##
## Description: Create a describe object and send messages based on its properties.
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

#%% User-Specified Dataset & Describe Object

#Create parameter for user-specified dataset:
dataset = sys.argv[1]
#Create describe object from dataset:
describe = arcpy.da.Describe(dataset)

#%% ArcGIS Messages

#Print dataset path:
arcpy.AddMessage(describe["catalogPath"])

#Print extent of dataset:
extent = describe["extent"]
arcpy.AddMessage("XMin: " + str(round(extent.XMin, 1)))
arcpy.AddMessage("YMin: " + str(round(extent.YMin, 1)))
arcpy.AddMessage("XMax: " + str(round(extent.XMax, 1)))
arcpy.AddMessage("YMax: " + str(round(extent.YMax, 1)))

#Check data type:
datasetType = describe["dataType"]
#Print properties of feature class:
if datasetType == "ShapeFile":
    arcpy.AddWarning("Shapetype: " + describe["shapeType"])
#Print properties of raster:
else:
    arcpy.AddWarning("Format: " + describe["format"])
    arcpy.AddWarning("# of rows: " + str(describe["height"]))
    arcpy.AddWarning("# of columns: " + str(describe["width"]))