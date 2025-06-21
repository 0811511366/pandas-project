import pandas as pd
import numpy as np

exam_data = {'name': ['lina','kina','aliza','ran','hadid','nila','ali'],
                      'score': [12,7.6,11,13,2,15,4.5],
                      'attemps':[2,1,2,3,1,2,1],
                      'qualify':['yes','no','no','yes','no','yes','yes']}
labels = ['a','b','c','d','e','f','g']

df = pd.DataFrame(exam_data , index=labels)
print("Summary of  the basic information about this DataFrame and its data:")
print(df.info())