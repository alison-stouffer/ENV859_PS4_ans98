##---------------------------------------------------------------------
## Interactive Python Script for Buffering
##
## Description: Iterate through multiple stream buffers.
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

#%%Set Input Feature Classes

#Set input feature class (FC) to streams shapefile in Data folder:
inputFC = "streams.shp"

#%%Create Buffer

#Set buffer distance:
streamBuffer = [100, 200, 300, 400, 500]

for distance in streamBuffer:

    #Set output feature class (FC) name and store in Data folder:
    outputFC = "V:\\_ProblemSets\\ENV859_PS4_ans98\\Scratch\\buff_"+str(distance)+"m.shp"   

    #Create feature class with buffered streams:
    arcpy.Buffer_analysis(inputFC,outputFC,distance,'','','ALL')

#%%Display Messages

print(arcpy.GetMessages())
