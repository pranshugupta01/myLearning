# -*- coding: utf-8 -*-
"""predict-using-pipeline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xH2unpoEd79qyFW6q5oAj-qCeO7CFjoh
"""

import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))

# Assume user input
test_input2 = np.array([2, 'male', 31.0, 0, 0, 10.5, 'S'],dtype=object).reshape(1,7)

pipe.predict(test_input2)

