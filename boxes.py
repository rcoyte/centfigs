# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:44:53 2021

@author: rmc33
"""


import os
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statistics
from scipy.stats import kruskal
from scipy.stats import spearmanr
import seaborn as sns
import scikit_posthocs as sp
import string

PJf = os.path.join('data.csv')
df = pd.read_csv(PJf, 
                     na_values=['OVER', 'nd', 'bdl','n.d.', 'N.D.', 'n.a.', 
                                'n/a','OR','#VALUE','ClO','J', 'censor'])
                                
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

pal = ["#f5f7a3", '#72b555', '#0f4269', '#a8f3ff', '#038499', '#dfadff', 
       '#5f0399','#f79999', '#910303']
       
fig,ax=plt.subplots(figsize=(5,5))
x='x'
y='y'
ylab= 'U ($\mu$g/L)'
xlab= 'HCO$_{3}^{-}$ (mg/L)'
f=sns.scatterplot(x, y, data=df, hue='Cat_2', 
                 edgecolor='k', s=150)
plt.xlabel(xlab)
plt.ylabel(ylab)
ax.legend(bbox_to_anchor=(1.05, 1), loc=2)
#ax.get_legend().remove()
plt.show() 