## Lab 10: Pandas ##

_author_ = "Burgess Doan III"
_credits_ = [""]
_email_ = "doanbs@mail.uc.edu"

# Formatted with Black Formatter
# https://pypi.org/project/black/

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
sh_raw = pd.read_csv('movies.csv', 
   header = None, 
   names = ['Year','Title','Comic','IMDB','RT','','OpeningWeekendBoxOffice','AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])

sh = sh_raw[np.isfinite(
          sh_raw.OpeningWeekendBoxOffice)]
# print(sh.head(5))

# Normalize and scatterplot the scores
# imdb_normalized = sh.IMDB / 10         
# sh.insert(10,'IMDBNormalized',imdb_normalized)
# rt_normalized = sh.RT/100        
# sh.insert(11, 'RTNormalized', rt_normalized)
# sh.plot.scatter(x ='RTNormalized', y ='IMDBNormalized')
# plt.show()

# print(sh[['RTNormalized','IMDBNormalized']].corr())
# print(sh[['RTNormalized','IMDBNormalized']].describe())

#My Methods

def PrintDC():
    for movie, row in sh.iterrows():
        if row["Comic"] == 'DC':
            print(row)
            
def PrintDCYearAndTitle():
    for movie, row in sh.iterrows():
        if row['Comic'] == 'DC':
            print(row['Year'], row['Title'])
            
def PrintMarvelYearAndTitle():
    for movie, row in sh.iterrows():
        if row["Comic"] == 'Marvel':
            print(row['Year'], row['Title'])
            
def TicketPriceByYearScatter():
    sh.plot.scatter(x ='Year', y ='AvgTicketPriceThatYear')
    plt.show()
    
def TicketPriceByYearCorr():
    print(sh[['Year','AvgTicketPriceThatYear']].corr())
    
def OpeningWeekendSummary():
    print(sh[['OpeningWeekendBoxOffice']].describe())
    
#Calling my Methods

#PrintDC()
#PrintDCYearAndTitle()
#PrintMarvelYearAndTitle()
#TicketPriceByYearScatter()
#TicketPriceByYearCorr()
#OpeningWeekendSummary()