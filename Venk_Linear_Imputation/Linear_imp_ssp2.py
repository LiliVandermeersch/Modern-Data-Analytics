# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:42:35 2021

@author: venka
"""


import pandas as pd
import numpy as np
import os
print("Current working directory: {0}".format(os.getcwd()))
path = 'C:\\Users\\venka\\MDA'
try:
    os.chdir(path)
    print("Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    print("Directory: {0} does not exist".format(path))
except NotADirectoryError:
    print("{0} is not a directory".format(path))
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))



ss_pop = pd.read_csv("pop_ssp2.csv")
ss_gdp = pd.read_csv("gdp_ssp2.csv")

test_ss_pop = ss_pop.iloc[:,3:]
test_ss_pop["gID"] = ss_pop["gID"]
test_ss_pop = test_ss_pop[['gID','ISO3',
'p2_1980',
'p2_1990',
'p2_2000',
'p2_2010',
'p2_2020',
'p2_2030',
'p2_2040',
'p2_2050',
'p2_2060',
'p2_2070',
'p2_2080',
'p2_2090',
 'p2_2100',
]]
year = 1980
count = 1
pre = 'p2_'
for i in range(1,120):
    year = year + 1
    if year % 10 != 0:
        col_name = pre + str(year)
        test_ss_pop[col_name] = np.nan
    count = count +1
##########Water gap data is upto 2016 therefore data will be captured till then 
data_pop_2016 = test_ss_pop.iloc[:,1:6]    
for i in range(1,37):
    year = year + 1
    if year % 10 != 0:
        col_name = pre + str(year)
        data_pop_2016[col_name] = np.nan
    count = count +1

data_pop_2016_T = data_pop_2016[[
'p2_1980',
'p2_1981',
'p2_1982',
'p2_1983',
'p2_1984',
'p2_1985',
'p2_1986',
'p2_1987',
'p2_1988',
'p2_1989',
'p2_1990',
'p2_1991',
'p2_1992',
'p2_1993',
'p2_1994',
'p2_1995',
'p2_1996',
'p2_1997',
'p2_1998',
'p2_1999',
'p2_2000',
'p2_2001',
'p2_2002',
'p2_2003',
'p2_2004',
'p2_2005',
'p2_2006',
'p2_2007',
'p2_2008',
'p2_2009',
'p2_2010',
'p2_2011',
'p2_2012',
'p2_2013',
'p2_2014',
'p2_2015',
'p2_2016'
]]
test_ss_pop_tran = data_pop_2016_T.transpose()
###############Linear Imputation###################################
for i in range(0,75227):
    test_ss_pop_tran[i].interpolate(method='linear', direction = 'forward', inplace=True) 

#######################################################################################GDP Linear Imputation###################################
ss_gdp = pd.read_csv("gdp_ssp2.csv")
test_ss_gdp = ss_gdp.iloc[:,3:]

data_gdp_2016 = test_ss_gdp.iloc[:,1:6]   
year = 1980
count = 1
pre2 = 'g2_'
for i in range(1,37):
    year = year + 1
    if year % 10 != 0:
        col_name = pre2 + str(year)
        data_gdp_2016[col_name] = np.nan
    count = count +1

data_gdp_2016_T = data_gdp_2016[[
'g2_1980',
'g2_1981',
'g2_1982',
'g2_1983',
'g2_1984',
'g2_1985',
'g2_1986',
'g2_1987',
'g2_1988',
'g2_1989',
'g2_1990',
'g2_1991',
'g2_1992',
'g2_1993',
'g2_1994',
'g2_1995',
'g2_1996',
'g2_1997',
'g2_1998',
'g2_1999',
'g2_2000',
'g2_2001',
'g2_2002',
'g2_2003',
'g2_2004',
'g2_2005',
'g2_2006',
'g2_2007',
'g2_2008',
'g2_2009',
'g2_2010',
'g2_2011',
'g2_2012',
'g2_2013',
'g2_2014',
'g2_2015',
'g2_2016'
]]


test_ss_gdp_tran = data_gdp_2016_T.transpose()

for i in range(0,75227):
    test_ss_gdp_tran[i].interpolate(method='linear', direction = 'forward', inplace=True) 



ssp2_gdp_final = test_ss_gdp_tran.transpose()
ssp2_gdp_final["ISO3"] = ss_gdp["ISO3"]
ssp2_gdp_final["gID"] = ss_gdp["gID"]
ssp2_pop_final = test_ss_pop_tran.transpose()
ssp2_pop_final["ISO3"] = ss_pop["ISO3"]
ssp2_pop_final["gID"] = ss_pop["gID"]


ssp2_gdp_final.to_csv("ssp2_1980_2016_GDP.csv")

ssp2_pop_final.to_csv("ssp2_1980_2016_pop.csv")

##########water gap####################
import h5py
f = h5py.File('watergap_22d_WFDEI-GPCC_histsoc_pdomww_yearly_1901_2016.nc4', 'r')
f2 = f.keys()
f['pdomww'].shape

pdomww = pd.DataFrame()
water_levels = pd.DataFrame(data={'pdomww': f['pdomww'][-1].reshape(360*720)})
lat = pd.DataFrame(data={'lat': f['lat']})
lon = pd.DataFrame(data={'lon': f['lon']})
time =  pd.DataFrame(data={'time': f['time']})
f,shape
pdomww["pdomww"] = water_levels["pdomww"]

import xarray as xr
import netCDF4
from netCDF4 import Dataset
ds = Dataset('watergap_22d_WFDEI-GPCC_histsoc_pdomww_yearly_1901_2016.nc4')
pdomww = ds['pdomww'][:]
lat = ds['lat'][:]
lon = ds['lon'][:]
year1 = pdomww[1,:,:]

year2 = lat[100,]
year2 = pdomww[81,:,:]
dateee = pd.DataFrame(data = year2)
dateee = pd.melt(dateee, value_name= '1981')
yearN = pd.DataFrame(data = year2)
yearN["lat"] = lat 
yearN.columns = lon
yearN.index = lat

YearT = pd.melt(yearN, ignore_index=False)

data_f = pd.DataFrame()
year = 1980
count = 0
for i in range(80,116):
    data = pdomww[i,:,:]
    if i == 80:
        data_pd = pd.DataFrame(data = data)
        lat = ds['lat'][:]
        data_pd.index =  lat
        lon = ds['lon'][:]
        data_pd.columns = lon
        data_pd = pd.melt(data_pd, ignore_index = False, var_name='lon', value_name='1980')
    else:
        data_I = pd.DataFrame(data = data)
        data_I.index =  lat
        year = year+1
        data_I = pd.melt(data_I,ignore_index = False, value_name= str(year))
        data_pd[str(year)] = data_I.loc[:,str(year)]
        count = count +1
        print(count)

data_pd.to_csv("Extracted_data_pdomww_1980-2016.csv")