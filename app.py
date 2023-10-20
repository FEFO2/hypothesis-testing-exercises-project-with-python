import numpy as np  
import pandas as pd
import scipy.stats as stats

df = pd.DataFrame({
    'fertilizer1': [20,21,20,19,20],
    'fertilizer2': [22,21,23,22,21],
    'fertilizer3': [24,23,22,23,24],
    })

fvalue, pvalue = stats.f_oneway(df.fertilizer1, df.fertilizer2, df.fertilizer3)
print(fvalue)
print(pvalue)