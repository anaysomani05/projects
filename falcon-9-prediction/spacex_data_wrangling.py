# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
print(df.head(10))

print(df.isnull().sum()/df.count()*100)

print(df.dtypes)

# Apply value_counts() on column LaunchSite
print(df["LaunchSite"].value_counts())

# Apply value_counts on Orbit column
print(df["Orbit"].value_counts())

# landing_outcomes = values on Outcome column
landing_outcomes = df["Outcome"].value_counts()
print(landing_outcomes)

for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)

# set of outcomes where the second stage did not land successfully:
bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
print(bad_outcomes)

# landing_class = 0 if bad_outcome
# landing_class = 1 otherwise

def onehot(item):
    if item in bad_outcomes:
        return 0
    else:
        return 1
landing_class = df["Outcome"].apply(onehot)
print(landing_class)

df['Class']=landing_class
df[['Class']].head(8)

print(df.head(5))

print(df["Class"].mean())