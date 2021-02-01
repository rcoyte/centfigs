# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:44:53 2021

@author: rmc33
"""
###############################################################################
#THESE ARE THE THINGS YOU NEED TO EDIT TO MAKE THIS CODE WORK
###############################################################################
filename = 'data.xlsx' #YOUR FILE NAME
x='x'
y='y'
ylab= 'U ($\mu$g/L)' #WHAT THE Y LABEL WILL SAY
xlab= 'HCO$_{3}^{-}$ (mg/L)' #WHAT THE X LABEL WILL SAY
category = 'Cat_1' #THE CATEOGRIES YOU ARE BREAKING YOUR DATA UP INTO
perc_hi = 90 #THE TOP PERCENTILE
perc_lo = 10 #THE BOTTOM PERCENTILE
###############################################################################
#IF YOU WANT TO CHANGE THE COLORS ASK ME HOW TO DO THE PALETTE BELOW
###############################################################################
pal = ['#F7931D', '#00B9F1', '#00A875', 'ECDE38', '#F15A22', '#00000', 
       '#0072BC', '#DA6FAB']  
###############################################################################
#DONT MESS WITH ANYTHING BELOW THIS LINE. SERIOUSLY. 
###############################################################################
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



SMALL_SIZE = 10
MEDIUM_SIZE = 16
BIGGER_SIZE = 20
plt.rc('font', family='serif')
plt.rc('xtick', labelsize= SMALL_SIZE)
plt.rc('ytick', labelsize='x-small')
plt.rc('axes', titlesize='small')     # fontsize of the axes title
plt.rc('axes', labelsize= BIGGER_SIZE, labelweight='bold')    # fontsize of the x and y labels
plt.rc('ytick.major', size=10,)
plt.rc('ytick.minor', size = 5)
plt.rc('xtick.major', size=10,)
plt.rc('xtick.minor', size = 5)
plt.rc('xtick', labelsize= BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize= BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize= MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=MEDIUM_SIZE)  # fontsize of the figure title


filetype = filename.split('.')[-1]
PJf = os.path.join(filename)
if filetype == 'csv':
    df = pd.read_csv(PJf, 
                     na_values=['OVER', 'nd', 'bdl','n.d.', 'N.D.', 'n.a.', 
                                'n/a','OR','#VALUE','ClO','J', 'censor'])
elif filetype == 'xlsx':
    df = pd.read_excel(PJf, 
                     na_values=['OVER', 'nd', 'bdl','n.d.', 'N.D.', 'n.a.', 
                                'n/a','OR','#VALUE','ClO','J', 'censor'])
else: 
    print('ERROR: INPUT FILE MUST BE CSV OR XLSX')




cats = df[category].unique()

  
k=len(cats)
del pal[k:]


fig,ax=plt.subplots(figsize=(5,5))
f=sns.scatterplot(x, y, data=df, hue=category, 
                 edgecolor='k', s=150, palette =  pal)
plt.xlabel(xlab)
plt.ylabel(ylab)
for indexi, i in enumerate(cats):
    x25 = np.percentile(df[df[category]== i][x], perc_lo)
    x75 = np.percentile(df[df[category]== i][x], perc_hi)
    y25 = np.percentile(df[df[category]== i][y], perc_lo)
    y75 = np.percentile(df[df[category]== i][y], perc_hi)
    left = x25
    bottom=y25
    width=x75-x25
    height=y75-y25
    rect = plt.Rectangle((left, bottom), width, height,
                     fill=False)
    ax.add_patch(rect)
    rect = plt.Rectangle((left, bottom), width, height,
                     facecolor=pal[indexi], alpha=0.1)
    ax.add_patch(rect)
ax.legend(bbox_to_anchor=(1.05, 1), loc=2)
#ax.get_legend().remove()
plt.show() 