# Read data from csv and clean

import pandas as pd
import os
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot

os.chdir(os.path.dirname(__file__))

dfAdobeRaw = pd.read_csv(r'ADBE.csv')
dfAdobeAdjPrice = dfAdobeRaw['Adj Close']

# ARIMA Model
import statsmodels  