from dbmaster import MasterBasic


def test_basic():
    mbasic = MasterBasic()
    assert isinstance(mbasic.getMaxModVal(), int), "Non-int max modVal"
    assert isinstance(mbasic.getModVals(), range), "Non-range modVals"
    assert isinstance(mbasic.getModVals(listIt=True), list), "Non-list modVals"