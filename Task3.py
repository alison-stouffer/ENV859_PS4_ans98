##---------------------------------------------------------------------
## Benthic Monitoring Sites in the Triangle
##
## Description: Split a point feature class into new, separte feature classes.
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

#Check for advanced license:
if arcpy.CheckProduct("ArcInfo") == "Available":
    msg = 'ArcGIS for Desktop Advanced license is available'
    print(msg)
    sys.exit(msg)
else:
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)
    
#Allow output to be overwritten:
arcpy.env.overwriteOutput = True

#%%