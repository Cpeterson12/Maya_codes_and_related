import maya.cmds as cmds

def Rename(string):
    sels = cmds.ls(sl=True)
    string.partition("##")
    for count, object in enumerate(sels):
        cmds.rename(object,string.partition('#')[0] + str(count + 1).zfill(string.count('#')) + string.rpartition('#')[2])

Rename("arm_##_jnt")