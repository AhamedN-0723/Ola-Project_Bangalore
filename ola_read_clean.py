import pandas as pd
import seaborn as sns

df = pd.read_excel('OLA_DataSet.xlsx')
print('Total rows, columns:\n',df.shape)
print('\nFirst 5 rows\n',df.head())
print('\nLast 5 rows\n',df.tail())
print('\nDtypes:\n',df.dtypes)
print(df.info())
print(df.describe(include='all'))

print(df.isnull().sum().sort_values(ascending=False))
missing = (df.isnull().sum()/len(df))*100
print(missing)
print(df.duplicated().sum())
df.drop(columns=['Vehicle Images'], inplace=True)
df = df.fillna('NA')
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
print(df['booking_status'].unique())
print(df['payment_method'].unique())
print(df['ride_distance'].describe())
#sns.boxplot(df['ride_distance'])
#plt.show()
#sns.boxplot(df['booking_value'])
#plt.show()
print(df.head())

df.to_csv('ola_clean.csv', index=False)