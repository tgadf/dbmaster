""" Master Param Data """

__all__ = ["MasterPaths"]

from utils import DirInfo
import warnings


###############################################################################
# Master List of Paths
###############################################################################
class MasterPaths:
    def __init__(self, **kwargs):
        verbose = kwargs.get('verbose', False)
        permDrivePath = DirInfo("/Volumes/Piggy")
        tempDrivePath = DirInfo("/Volumes/Seagate")
        localDrivePath = DirInfo("/Users/tgadfort/Music")
        
        # Raw Drive Path
        rawPathDrive = permDrivePath
        if not permDrivePath.exists():
            warnings.warn(f"Perm Path [{permDrivePath}] Does Not Exist.")
            if tempDrivePath.exists():
                print(f"Setting Raw Path To [{tempDrivePath}]")
                rawPathDrive = tempDrivePath
            elif localDrivePath.exists():
                print(f"Setting Raw Path To [{localDrivePath}]")
                rawPathDrive = localDrivePath
            else:
                raise OSError("No path exists for raw drive path!")
                
        # ModVal Drive Path
        modValPathDrive = tempDrivePath
        if not modValPathDrive.exists():
            warnings.warn(f"ModVal Path [{modValPathDrive}] Does Not Exist.")
            if localDrivePath.exists():
                print(f"Setting ModVal Path To [{localDrivePath}]")
                modValPathDrive = localDrivePath
            else:
                raise OSError("No path exists for modVal drive path!")
                
        # Summary Drive Path
        summaryPathDrive = tempDrivePath
        if not summaryPathDrive.exists():
            warnings.warn(f"Summary Path [{summaryPathDrive}] Does Not Exist.")
            if localDrivePath.exists():
                print(f"Setting ModVal Path To [{localDrivePath}]")
                summaryPathDrive = localDrivePath
            else:
                raise OSError("No path exists for summary drive path!")
                
        # Match Drive Path
        matchPathDrive = localDrivePath
        if not matchPathDrive.exists():
            raise OSError("No path exists for match drive path!")
        
        # Append Discog To Final Drive Path
        self.rawPath = rawPathDrive.join("Discog")
        self.modValPath = modValPathDrive.join("Discog")
        self.summaryPath = summaryPathDrive.join("Discog")
        self.matchPath = matchPathDrive.join("Discog")
        if verbose is True:
            print("MasterPaths()")
            print(f"{'  ==> Raw:': <18}{self.rawPath}")
            print(f"{'  ==> ModVal:': <18}{self.modValPath}")
            print(f"{'  ==> Summary:': <18}{self.summaryPath}")
            print(f"{'  ==> Match:': <18}{self.matchPath}")
    
    def getRawPath(self):
        return self.rawPath

    def getModValPath(self):
        return self.modValPath

    def getSummaryPath(self):
        return self.summaryPath

    def getMatchPath(self):
        return self.matchPath