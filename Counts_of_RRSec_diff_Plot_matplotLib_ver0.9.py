# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:56:22 2019

@author: Sujith Tenali
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:14:51 2019

@author: Sujith Tenali
"""

import pandas as pd
import random
data = pd.read_csv('df_rhythmInfo_32748_1552798645150441.csv')

data['RRSec_n_plus_1'] = data.RRSec.shift(-1,axis=0)

data['RRSec_diff'] = data['RRSec_n_plus_1'] - data['RRSec']



df = data.groupby(by='RRSec_diff', as_index=False).agg({'RowNumber': pd.Series.nunique})




#print(df)


import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

prop = fm.FontProperties(fname='C:/Users/Sujith Tenali/Desktop/Intern/DayWise/Montserrat-Bold.ttf')
prop2 = fm.FontProperties(fname='C:/Users/Sujith Tenali/Desktop/Intern/DayWise/Montserrat-Medium.ttf')


fig= plt.figure(figsize=(10,5))


plt.grid(b=None, which='major', axis='both',linewidth=0.2)

    
plt.xticks(rotation=35,fontproperties=prop, ha='right', va='top')
plt.yticks(fontproperties=prop)

plt.ylabel('count', fontproperties=prop,size=12)
plt.xlabel('RRSec Differences(secs)', fontproperties=prop,size=12)


plt.ylim(0,df['RowNumber'].max())


plt.title('Counts of RRSec Differences',fontproperties=prop,size=18,color = '#22ACE2')
          


cu = pd.Series(data['RRSec_diff'])

#cu2 is used for bins intervals
cu2 = pd.Series(df['RRSec_diff'])

plt.hist(cu,bins = cu2, facecolor='blue', alpha=0.5,rwidth=0.85)

plt.savefig('counts_diff'+str(random.randint(1,100000))+'.png', dpi=200, facecolor='w', edgecolor='w',
       orientation='landscape', papertype=None, format=None,
      transparent=False, bbox_inches='tight', pad_inches=0.1,
       frameon=None, metadata=None)
