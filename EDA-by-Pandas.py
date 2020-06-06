#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Standard Library Imports
#from pathlib import Path

# Installed packages
import pandas as pd
#from ipywidgets import widgets

# Our package
from pandas_profiling import ProfileReport
#from pandas_profiling.utils.cache import cache_file


# In[ ]:


df = pd.read_csv('Data/RealUKAccidentAnalysisData/dftRoadSafetyData_Accidents_2018.csv')


# In[ ]:


# Generate the Profiling Report
profile = ProfileReport(df, title="UK Accident Data-2018", html={'style': {'full_width': True}}, sort="None")


# In[ ]:


# The Notebook Widgets Interface
profile.to_file('Data/RealUKAccidentAnalysisData/dftRoadSafetyData_Accidents_2018.html')


# In[ ]:




