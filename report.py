#taking the scores, normalize them and plot a bargraph
# check https://docs.google.com/document/d/1BKUZlRhjtckP8GE7OKepq_7KMr8xX5p483xrNK2SeeM/edit#
#this is a sample
import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
nacad=int((7*10)/24)
nadj=int((3*10)/18)
nsocial=int((5*10)/10)
nfam=int((9*10)/12)
nhealth=int((1*10)/9)
data = {'academic':nacad, 'personality/adjustment':nadj, 'social':nsocial,
        'family':nfam,'clinical/health':nhealth} 

courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='lightgreen',
        width = 0.4)
 
plt.savefig(r"C:\sudhira\project\StudentCounseling\new_image.jpg",bbox_inches='tight')
plt.show()