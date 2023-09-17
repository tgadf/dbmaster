""" Master Basic Data Container """

__all__ = ["MasterBasic"]


###############################################################################
# Master Basic Info
###############################################################################
class MasterBasic:
    def __init__(self, **kwargs):
        verbose = kwargs.get('verbose', False)
        self.maxModValue = 100
        self.projectName = "pandb"
        self.musicdbName = "pandb"
        if verbose is True:
            print("MasterBasic()")
            print(f"{'  ==> ModVals:': <18}{self.maxModValue}")
            print(f"{'  ==> Project:': <18}{self.getProjectName()}")
            print(f"{'  ==> MusicDB:': <18}{self.getMusicDBName()}")

    def getMaxModVal(self):
        return self.maxModValue
    
    def getModVals(self, listIt=False):
        retval = range(self.getMaxModVal())
        retval = list(retval) if listIt is True else retval
        return retval

    def getProjectName(self):
        return self.projectName

    def getMusicDBName(self):
        return self.musicdbName