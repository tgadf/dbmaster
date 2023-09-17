""" Utility Map For Perminant/Persist Directories """

__all__ = ["MasterPersist"]

from utils import DirInfo
from sys import prefix
from .dbs import MasterDBs
from .params import MasterParams


class MasterPersist:
    def __init__(self, **kwargs):
        mkDirs = kwargs.get('mkDirs', False)
        mp = MasterParams()
        mdbs = MasterDBs()

        paths = {}
        
        paths["Prefix"] = DirInfo(prefix)
        paths["Project"] = paths["Prefix"].join(mp.getProjectName())
        paths["PanDB"] = paths["Project"].join("pandb")
        paths["MusicDB"] = paths["Project"].join("musicdb")
        for db in mdbs.getDBs():
            paths[f"MusicDB-{db}"] = paths["MusicDB"].join(db)
        paths["Match"] = paths["Project"].join("match")
        paths["Meta"] = paths["Project"].join("meta")
        paths["PanDBPair"] = paths["Project"].join("pandbpair")

        if mkDirs is True:
            for key, keyPath in paths.items():
                keyPath.mkDir()
            
        self.paths = paths

    def getPrefixDir(self):
        return self.paths["Prefix"]
        
    def getProjectDir(self):
        return self.paths["Project"]
        
    def getPanDBPath(self):
        return self.paths["PanDB"]
    
    def getDBPath(self, db):
        mdbs = MasterDBs()
        assert mdbs.isValid(db) is True, "db [{db}] is not valid!"
        return self.paths[f"MusicDB-{db}"]
    
    def getMatchPath(self):
        return self.paths["Match"]
    
    def getMetaPath(self):
        return self.paths["Meta"]
    
    def getPanDBPairPath(self):
        return self.paths["PanDBPair"]
