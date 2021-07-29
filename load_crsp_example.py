#CRSP Access In Python
import numpy as np
import pandas as pd
import math
import time

def applyFun(dfGrouped, func):
	ret_list = [func(group) for name, group in dfGrouped]
	return pd.concat(ret_list,axis=0,ignore_index=False)

def print_by_group(group_df):
	print(group_df)
	return group_df   
	
#Load WRDS database
import wrds
db = wrds.Connection()

#View CRSP Daily Returns Database
print(db.describe_table(library="crsp", table="dsf"))

#Load CRSP Daily Returns
#Query WRDS using SQL 
#Returns a Pandas dataframe
#Get Open/High/Low/Close/Volume data for all stocks in 2020
df = db.raw_sql("select permno, date, openprc, bidlo, askhi, prc, vol from crsp.dsf where vol > 0 and date between '2020-01-01' and '2020-12-31'")
db.close()
df.rename(columns={"openprc":"open", "askhi":"high", "bidlo":"low", "prc":"close", "vol":"volume"}, inplace=True)

#group dataset by permno
grouped = df.groupby(['permno'])
 
#measure runtime - start
start = time.time() 
print("Start work")

#run the serial function for the whole dataframe
#this can perform many tasks by modifying the print_by_group function to the desired spec
out_Array = applyFun(grouped,print_by_group)

#measure runtime - end
end = time.time()
print("End work")    
print( (end - start)/60 )
		
# write output to csv file         
path_final = 'my_output.csv'
out_Array.to_csv(path_final, index=False)

