"""
===================================================
Analysis Tools (:mod:`pchangetools.analysis_tools`)
===================================================

.. currentmodule:: pchangetools.analysis_tools

Tools for generating graphics for teaching computational thinking from
ECMWF reanalysis data. Initial work by Scott Collis scollis@anl.gov

.. autosummary::
    :toctree: generated/

    Anal_Obj


"""
import xarray as xr


class Anal_Obj(object):
    """A class for manipulating reanalyses


    Cooldocs

    Attributes
    ----------

    era_data : xarray dataset
             xarray data set ith the initial ERA reanalysis

    data_loc : string
              String with the location of the netcdf file for
              the ERA data

    """

    def __init__(self, era_filename):
        self.data_loc = era_filename
        self.era_data = xr.open_dataset(self.data_loc)
