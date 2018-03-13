import maya.cmds as cmds

selection = cmds.ls(selection=True)
allGeo = cmds.ls(geometry = True)

size = cmds.polyEvaluate (a = True)

if len(selection) == 0:
    cmds.warning("No mesh selected! Please select the reference mesh that you want to hide with the same or smaller size")
else:
    confirm = cmds.confirmDialog( title='Confirm', message='Selected geometry: '+ str(selection) +'\nGrouping and hiding mesh smaller than '+ str(size) + ' ?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
    
    if confirm == 'Yes':
        if not cmds.objExists('hiddenMesh_grp'):
            hiddenGroup = cmds.group(em=True, name='hiddenMesh_grp')
        else:
            hiddenGroup = 'hiddenMesh_grp'
            
        for obj in allGeo:
            cmds.select (obj)
            meshSize = cmds.polyEvaluate (a = True)
            
            
            if meshSize <= size:
                print obj + ": Size of " + str(meshSize)
                transformShape = cmds.listRelatives(allParents=True)
                cmds.hide(transformShape)
                try:
                    cmds.parent( transformShape, hiddenGroup)
                except:
                    pass