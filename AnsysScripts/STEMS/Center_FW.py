# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2018.0.0
# 22:23:21  Jun 17, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
# setting the first open project as the active project
oProject = oDesktop.SetActiveProject(oDesktop.GetProjectList()[0])
oDesign = oProject.SetActiveDesign("Maxwell3DDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

selections = ""
# selecting all the objects to center the geometry. 
for objects in oEditor.GetObjectsInGroup("Solids"):
	# python string concatenation
	selections = selections+objects+","

for sheets in oEditor.GetObjectsInGroup("Sheets"):
    selections = selections+sheets+","


oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, selections,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "-$fly_radius",
		"TranslateVectorZ:="	, "-$total_length/2"
	])
