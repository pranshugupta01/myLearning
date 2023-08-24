# -*- coding: utf-8 -*-
"""pandas_profiling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VEIgOH9FbbMCzA67gxJU1e0QJn5Zi8xW
"""

import pandas as pd

df = pd.read_csv('train.csv')

df.head()

!pip install pandas-profiling

from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='output.html')
