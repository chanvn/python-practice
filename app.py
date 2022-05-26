import pandas as pd

superhero = pd.read_excel("sampledata.xlsx")

#print(superhero.shape[0])

superhero['DateTime of birth'].str.split('T',expand=True)
superhero
print(superhero)

