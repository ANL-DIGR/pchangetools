from ..analysis_tools import Anal_Obj
import os


def test_one_plus_one_is_two():
    "Check that one and one are indeed two."
    assert 1 + 1 == 2


def test_era_read():
    data_path = os.path.join(os.path.dirname(__file__), '../data')
    era_microfile = os.path.join(data_path, 'era_microfile.nc')
    era_inst = Anal_Obj(era_microfile)
    assert era_inst.era_data.t2m.units == 'K'
