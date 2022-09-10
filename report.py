#taking the scores, normalize them and plot a bargraph
# check https://docs.google.com/document/d/1BKUZlRhjtckP8GE7OKepq_7KMr8xX5p483xrNK2SeeM/edit#
#this is a sample
import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'academic':6, 'personality/adjustment':7, 'social':3,
        'family':8,'clinical/health':9}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='lightgreen',
        width = 0.4)
 
plt.savefig(r"C:\sudhira\project\new_image.jpg",bbox_inches='tight')
plt.show()