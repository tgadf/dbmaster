""" Master DB Data """

__all__ = ["MasterDBs"]

from pandas import Series


###############################################################################
# Master List of Databases
###############################################################################
class MasterDBs:
    def __init__(self, **kwargs):
        verbose = kwargs.get('verbose', False)
        self.dbs = ["Discogs", "Spotify", "LastFM", "Genius", "RateYourMusic",
                    "MetalArchives", "Deezer", "AllMusic", "MusicBrainz",
                    "AlbumOfTheYear", "SetListFM", "Beatport", "Traxsource",
                    "MyMixTapez", "ClassicalArchives", "JioSaavn", "Napster",
                    "YouTubeMusic", "AppleMusic", "Wikidata", "Bandcamp",
                    "SpiritOfMetal", "RollDaBeats", "Petrucci"]
        self.dbs = ["AlbumOfTheYear", "AllMusic", "AppleMusic", "Bandcamp",
                    "Beatport", "Deezer", "Discogs", "Genius", "JioSaavn",
                    "LastFM", "MetalArchives", "MusicBrainz", "MyMixTapez",
                    "Napster", "Petrucci", "RateYourMusic", "RollDaBeats",
                    "SpiritOfMetal", "SetListFM", "Spotify", "Traxsource",
                    "Wikidata", "YouTubeMusic"]
        self.dbs += ["Gaana", "Petrucci", "ClassicalArchives", "Qobuz",
                     "YesAsia"]
        # "Petrucci", "ClassicalArchives"
        # self.others ["MusicVF", "DatPiff", "Soundcloud"]
        self.valid = {db: True for db in self.dbs}
            
        self.dbTypeWeights = {"Trusted": 1,
                              "General": 1 / 3,
                              "Genre": 1 / 6,
                              "Dump": 0 / 10}
        
        self.dbTypes = {'AllMusic': 'Trusted',
                        'SetListFM': 'General',
                        'Discogs': 'General',
                        'Spotify': 'General',
                        'YouTubeMusic': 'General',
                        'AppleMusic': 'General',
                        'Napster': 'General',
                        'Wikidata': 'General',
                        'Bandcamp': 'General',
                        'LastFM': 'Dump',
                        'Genius': 'General',
                        'RateYourMusic': 'Trusted',
                        'MetalArchives': 'Genre',
                        'SpiritOfMetal': 'Genre',
                        'Deezer': 'Dump',
                        'MusicBrainz': 'Trusted',
                        'AlbumOfTheYear': 'General',
                        'RollDaBeats': 'Genre',
                        'Beatport': 'Genre',
                        'Traxsource': 'Genre',
                        'MyMixTapez': 'Genre',
                        'ClassicalArchives': 'Genre',
                        'Petrucci': 'Genre',
                        'JioSaavn': 'Genre'}
        
        if verbose is True:
            print("MasterDBs()")
            print(f"{'  ==> DBs:': <18}{self.dbs}")
        
    def isValid(self, db):
        return self.valid.get(db, False)
    
    def getDBType(self, db):
        retval = self.dbTypes.get(db, "Unknown DB!")
        return retval
    
    def getDBs(self):
        return self.dbs
    
    def getDBTypes(self):
        return self.dbTypes
    
    def getDBTypeWeights(self):
        return self.dbTypeWeights
    
    def getDBWeights(self):
        activeDBWeights = {db: dbType for db, dbType in self.dbTypes.items() if db in self.dbs}
        dbWeights = Series(activeDBWeights).map(self.dbTypeWeights.get)
        return dbWeights