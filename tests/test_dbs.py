from pandas import Series
from dbmaster import MasterDBs


def test_dbs():
    mdbs = MasterDBs()
    
    dbs = mdbs.getDBs()
    assert isinstance(dbs, list), "Non-list dbs"
    
    dbTypeWeights = mdbs.getDBTypeWeights()
    assert isinstance(dbTypeWeights, dict), "Non-dict dbTypeWeights"
    for dbType, weight in dbTypeWeights.items():
        assert isinstance(weight, (int, float)), f"dbType [{dbType}] has non-(int/float) weight [{weight}]"
        
    dbTypes = mdbs.getDBTypes()
    assert isinstance(dbTypes, dict), "Non-dict dbTypes"
    for db, dbType in dbTypes.items():
        assert db in dbs, f"db {db} is lists in dbTypes, but not DBs!"
        assert dbType in dbTypeWeights.keys(), f"dbType {dbType} is not valid!"
        
    dbWeights = mdbs.getDBWeights()
    assert isinstance(dbWeights, Series), "Non-Series dbWeights"
    for db, weight in dbWeights.items():
        assert db in dbs, f"db {db} is lists in dbTypes, but not DBs!"
        assert isinstance(weight, (int, float)), f"db [{db}] has non-(int/float) weight [{weight}]"
        
    for db in dbs:
        assert mdbs.isValid(db), f"db [{db}] is not valid!"
        assert mdbs.getDBType(db) in dbTypeWeights.keys(), f"db [{db}] has invalid type [{mdbs.getDBType(db)}]"
        