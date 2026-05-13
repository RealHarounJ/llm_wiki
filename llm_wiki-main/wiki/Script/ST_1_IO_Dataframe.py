import pandas as pd
## pandas è la libreria per la manipolazione di dati
data = {
  "calories": [420, 380, 390, 320, 388, 340, 340],
  "duration": [50, 40, 40, 40, 50, 57, 57]
}
type(data)
print(data)
'''
Index -- is used to define the statistical units (i.e., the row)
'''
df = pd.DataFrame(data, index = ["day1", "day2", "day3", "day4", "day5", "day6","day7"])  
df.shape  # it is used to display the dimension of the dataframe
print(df) 
a = int(input('press a number to continue'))
## Selection of a subsect
##
print('calories >385')
print(df[df.calories>385])
# save the subset
dff=df[df.calories>385]
## check
print(dff)
a = int(input('press a number to continue'))
### look at the column "calories"
print('look at the column calories')
print(df["calories"][:])
a = int(input('press a number to continue'))
print('first four elements')
print(df[0:4])  # Please note the slicing - the index starts from zero 
a = int(input('press a number to continue'))
## compute some descriptive statistics
print('descriptive statistics')
dstat=df.agg({"calories": ["min", "max", "median", "mean"]})
print(dstat)
a = int(input('press a number to continue'))
print('conditional arithmetic mean')
print(df.groupby(["duration"])["calories"].mean())
a = int(input('press a number to continue'))   
# here for each "duration" compute the arithmetic mean of "calories"

### Now we deal with the two statitical variables as DISCRETE variables. We count the occurences
print('frequency distribution')
print(df[["duration","calories"]].value_counts())
a = int(input('press a number to continue')) 
print('descriptive statistics of the two columns')
print(df[["duration","calories"]].describe())
#### Please note how we are selecting the columns of the dataframe.
a = int(input('press a number to continue'))

## Select columns and rows from dataframe
#refer to the named index:
print(df.loc["day2"])
a = int(input('press a number to continue')) 
## we save the dataframe in a csv file
print('generate a csv file')
df.to_csv('prova.csv',sep=',',index=False)
a = int(input('press a number to continue')) 

## Reading an excel file
print('Reading an xls file')
file_name ="Heights.xls";
sheet = "Data"; # sheet name or sheet number or list of sheet numbers and names
## librery
dfxls = pd.read_excel(io=file_name, sheet_name=sheet)
print(dfxls.head(10))  # print first 5 rows of the dataframe
a = int(input('press a number to continue')) 

#### Similarly we can read the csv file.
provaD = pd.read_csv('prova.csv',sep=',')
## guardiamo alcune righe del file
provaD.head()
a = int(input('press a number to continue')) 
type(provaD.duration)
## Print the first ten rows 0,1,2...,9  
print(provaD[0:10])
a = int(input('press a number to continue')) 
## to see a large number of row we have to set a counter 
pd.options.display.max_rows = 9999;

## to caputer the column name
provaD_top=list(provaD.columns)
provaD_top
## come possimo lavorare sulle colonne?
provaD.duration[0:10]
