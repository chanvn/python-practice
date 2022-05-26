import pandas as pd

superhero = pd.read_excel("sampledata.xlsx")

#print(superhero.shape[0])

superhero[['date','time']] = superhero['DateTime of birth'].str.split('T', n=1 ,expand=True)
superhero.drop('DateTime of birth',axis=1, inplace=True)


print(superhero.head())

superhero.to_excel('updated-data.xlsx')

