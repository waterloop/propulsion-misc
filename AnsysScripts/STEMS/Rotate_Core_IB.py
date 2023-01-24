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

oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, selections,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Y",
		"RotateAngle:="		, "90deg"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, selections,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "$core_xoffset",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "$flange_height+$core_offset"
	])

