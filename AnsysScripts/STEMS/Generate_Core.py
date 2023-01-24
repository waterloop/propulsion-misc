# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2018.0.0
# 1:04:53  May 26, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
# setting the first open project as the active project
oProject = oDesktop.SetActiveProject(oDesktop.GetProjectList()[0])
oDesign = oProject.SetActiveDesign("Maxwell3DDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "$total_width",
		"YSize:="		, "$total_length",
		"ZSize:="		, "$total_height"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Core",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "$edge_length",
		"ZPosition:="		, "$total_height",
		"XSize:="		, "$total_width",
		"YSize:="		, "$slot_length",
		"ZSize:="		, "-1*$slot_depth"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Slot",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False
	])
oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, "Slot",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, "0mm",
		"YComponent:="		, "$slot_gap",
		"ZComponent:="		, "0mm",
		"NumClones:="		, "$slot_number"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", False
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])

# selecting the all the objects in "Solids", except for the first entry: "Core"
sol = oEditor.GetObjectsInGroup("Solids")[1:]

# subtracting each slot individually
for tool in sol:
	oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Core",
		"Tool Parts:="		, tool
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "0mm",
		"YPosition:="		, "$edge_length",
		"ZPosition:="		, "0mm",
		"XSize:="		, "$coil_inner_width",
		"YSize:="		, "$coil_length",
		"ZSize:="		, "$coil_inner_height"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Inner_Coil"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-$outer_coil_x",
		"YPosition:="		, "$edge_length",
		"ZPosition:="		, "-$outer_coil_z",
		"XSize:="		, "$coil_outer_width",
		"YSize:="		, "$coil_length",
		"ZSize:="		, "$coil_outer_height"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Outer_Coil"
				]
			]
		]
	])

# indices of the target edges are deterministic
# indices of the IDs to be selected for filet
ie = [0,2,4,6]
# collecting edges
edges = oEditor.GetEdgeIDsFromObject("Outer_Coil")
# changing the datatype of the entries to 'int'
filet = [int(edges[i]) for i in ie]

oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "Outer_Coil",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, filet,
			"Vertices:="		, [],
			"Radius:="		, "$coil_filet",
			"Setback:="		, "0mm"
		]
	])

oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Outer_Coil",
		"Tool Parts:="		, "Inner_Coil"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
		"Selections:="		, "Outer_Coil"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Outer_Coil"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material Appearance",
					"Value:="		, True
				]
			]
		]
	])

oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
		"Selections:="		, "Core"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"iron\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Core"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material Appearance",
					"Value:="		, True
				]
			]
		]
	])

selections = ""
# selecting all the objects to center the geometry. 
for objects in oEditor.GetObjectsInGroup("Solids"):
	# python string concatenation
	selections = selections+objects+","

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, selections,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "-1*$total_width/2",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "0mm"
	])

oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, "Outer_Coil",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, "0mm",
		"YComponent:="		, "$slot_gap",
		"ZComponent:="		, "0mm",
		"NumClones:="		, "$slot_number"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", False
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])

sections = ""
# selecting all solids except for the 'Core', which is the first entry
for obj in oEditor.GetObjectsInGroup("Solids")[1:]:
	sections = sections + obj + ","

oEditor.Section(
	[
		"NAME:Selections",
		"Selections:="		, sections,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:SectionToParameters",
		"CreateNewObjects:="	, True,
		"SectionPlane:="	, "YZ",
		"SectionCrossObject:="	, False
	])

sep = ""
# selecting all the sheets
for obj in oEditor.GetObjectsInGroup("Sheets"):
	sep = sep + obj+","

oEditor.SeparateBody(
	[
		"NAME:Selections",
		"Selections:="		, sep,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignInsulating(
	[
		"NAME:CoreInsulate",
		"Objects:="		, ["Core"]
	])

# creating the windings excitations
# initializing the index
i = 0
# creating the winding names
wo = ['A','B','C']
# creating the phase offsets for each of the windings
ph = ["","+2*pi/3","-2*pi/3"]
for wind in wo:
	oModule.AssignWindingGroup(
		[
			"NAME:"+wind,
			"Type:="		, "Voltage",
			"IsSolid:="		, False,
			"Current:="		, "0mA",
			"Resistance:="		, "$coil_resistance",
			"Inductance:="		, "$coil_inductance",
			"Voltage:="		, "$input_voltage*cos(time"+ph[i]+")",
			"ParallelBranchesNum:="	, "1"
		])
	i += 1

