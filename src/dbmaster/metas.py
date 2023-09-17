""" Master Metadata Container Class """

__all__ = ["MasterMetas"]


###############################################################################
# Master List of Metas
###############################################################################
class MasterMetas:
    def __init__(self, **kwargs):
        verbose = kwargs.get('verbose', False)
        self.mediaTypes = {"A": "Album", "B": "SingleEP", "C": "Appearance",
                           "D": "Technical", "E": "Mix", "F": "Bootleg",
                           "G": "AltMedia", "H": "Other"}
        self.mediaRanks = {"Primary": ["Album", "SingleEP"],
                           "Secondary": ["Appearance", "Mix", "Bootleg"],
                           "Tertiary": ["Technical", "AltMedia", "Other"]}
        self.mediaAlbums = [self.mediaTypes['A'], self.mediaTypes['B']]
        self.metaTypes = {"Basic": ["Name", "Ref", "NumAlbums"],
                          "Media": [f"{media}Media" for media in self.mediaTypes.values()],
                          "Genre": ["Genre"], "Bio": ["Bio"], "Link": ["Link"],
                          "Metric": ["Metric"], "Counts": ["Counts"]}
        self.summaryTypes = {"Basic": ["Name", "Ref", "NumAlbums"],
                             "Counts": ["Counts"],
                             "Media": [f"{media}Media" for media in self.mediaTypes.values()],
                             "Dates": ["Dates"], "Genre": ["Genre"],
                             "Metric": ["Metric"], "Link": ["Link"]}
        self.matchTypes = ["Name"] + [f"{media}Media" for media in self.mediaTypes.values()]
        self.matches = self.getMatches()
        if verbose is True:
            print("MasterMetas()")
            print("{0: <18}{1}".format("  ==> Media:", list(self.mediaTypes.values())))
            print("{0: <18}{1}".format("  ==> Meta:", list(self.metaTypes.keys())))
            print("{0: <18}{1}".format("  ==> Summary:", list(self.summaryTypes.keys())))
            print("{0: <18}{1}".format("  ==> Match:", self.matchTypes))
            
    def getMatchMedias(self, medias=None):
        medias = medias if isinstance(medias, list) else self.mediaTypes.values()
        retval = []
        for media in medias:
            assert isinstance(media, str) and media in self.mediaTypes.values(), f"Media [{media}] is not in master list of medias"
            retval.append(f"{media}Media")
        return retval
    
    def getMatches(self, medias=None):
        retval = ["Name"] + self.getMatchMedias(medias)
        return retval
        
    def getMediaTypes(self):
        return self.mediaTypes
        
    def getMediaRanks(self):
        return self.mediaRanks
    
    def getMetaTypes(self):
        return self.metaTypes
    
    def getSummaryTypes(self):
        return self.summaryTypes
    
    def getMatchTypes(self):
        return self.matchTypes