import numpy as np
import pandas as pd

#input file name here
filename ='heartdata.csv'
df = pd.read_csv(filename)

#replace "present" with 1 and "absent" with 0 in the famhist column
df.famhist = df.famhist.replace('Present',1)
df.famhist = df.famhist.replace('Absent',0)

raw_data = df.values

cols = range(1, 11) # Getting rid of the first column since it's column numbers
X = raw_data[:, cols]

# We can extract the attribute names that came from the header of the csv
attributeNames = np.asarray(df.columns[cols])

#print(df)
