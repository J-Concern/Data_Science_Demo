import pandas as pd
from path import path
import numpy as np
import ccutils

# Calls csv from imported path and assigns unclean data to data frame.
unclean_data = pd.read_csv(path)
df = pd.DataFrame(unclean_data)
# Drops name from the data frame
df = df.drop('Name', axis =1)

#Fills all NaN with 0
df = df.fillna(0)

# Changes Sex to a numerical value
df['Sex'] = (
    df["Sex"]
        .map({"male": 1, "female": 2})
        .fillna(0)
        .astype(int) #declares type int
)

# Changes embarked to a numerical value
df['Embarked'] = (
    df["Embarked"]
        .map({'S': 1, 'C': 2, 'Q': 3})
        .fillna(0)
        .astype(int)
)


#converts cabin data to numeric
df['Cabin'] = ccutils.edit_pd_column(df, 'Cabin')


#converts ticket data to numeric
strings = df['Ticket']
df['Ticket'] = ccutils.strip_all_alpha(strings)


#export to csv
df.to_csv('cleandata', header=None, index=False)