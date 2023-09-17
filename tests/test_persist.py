from dbmaster import MasterPersist
from utils import DirInfo

    
def test_permdir():
    mpersist = MasterPersist(mkDirs=True)

    paths = mpersist.paths
    assert isinstance(paths, dict), f"paths [{paths}] is not a dict"

    for name, dinfo in paths.items():
        assert isinstance(dinfo, DirInfo), f"name path [{name}] is not a DirInfo [{dinfo}]"
        assert dinfo.exists(), f"name path [{name}] does not exist [{dinfo}]!"