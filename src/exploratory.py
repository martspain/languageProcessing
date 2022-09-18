import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/train.csv')

def showShape():
  shp = df.shape
  print("Observations: ", shp[0])
  print("Variables: ", shp[1])
  
  dtypes = df.dtypes

  for i in range(shp[1]):
    if i < 4:
      print("\t- name:", df.columns[i], "\t\t\ttype:", dtypes[i])
    else:
      print("\t- name:", df.columns[i], "\ttype:", dtypes[i])

def showFrequency():
  print(df['discourse_effectiveness'].value_counts())
  df['discourse_effectiveness'].value_counts().plot(kind='barh')
  plt.show()
  print("-------------------------------------------")
  print(df['discourse_type'].value_counts())
  df['discourse_type'].value_counts().plot(kind='barh')
  plt.show()
  print("-------------------------------------------")
  print(df['essay_id'].value_counts())
  print("-------------------------------------------")


##################################################################
############################## MAIN ##############################

# Get overall shape of data
# showShape()

# Show frequency tables for relevant variables
# showFrequency()

