import pandas as pd
import numpy as np
#This is part of final assignment for econometrics worth 20% of my grade and i decided to use some aspects of codng as part of my quant reasearch.
#This is just basic data analysis for subclaim 4( Government Finances and Revenue). 
#I am still not at the computational stage of complete statistical analysis, so majority of the code is just data cleaning and visualization.
#The main usable statistical analysis will be done in Eviews.
#The observed variables are taxes, government debt and unemployment.

df = pd.read_excel(r"C:\Users\given\Desktop\ECM DATA PROJECT 2\SUB-CLAIM 4 DATA.xlsx", sheet_name="Sheet1") 
df.head()
df.tail()
#these 2 codes are good for returning the first 5 and last 5 rows of the data frame.This is to ensure the data I loaded is correct

df.info()
#sometimes python stores numerical values, so its wise to check your dtype. Especially if you're dealing with numeric data.
df.notnull()
#this code is to return boolean values of whether there is the prescence of NAN entries.
df.index 
#here the goal was to check the index to see what mt index levels were. They turend out to be numeric placeholders.
#for econometric analysis its wise to have the date as your index.
df = df.set_index('DATE')

#before any formal coding, i think it's wise to remove the effects of covide 19( this was in 2019). Since the data is quarterly we will have to pass in a list.
df.tail(30) 
df = df.drop(["2019/03/31","2019/06/30", "2019/09/30", "2019/12/31" ])
df.tail(30)
 #for some basic stats
df.columns
#Index(['TAXES', 'UNM', 'DEBT', 'DEF/SUR'], dtype='object')
df["TAXES"].mean().round(4)
# The average government tax collectible = np.float64(1274997.3043478262), i do like this long number so i rounded it off, np.float64(1274997.3043)
df["UNM"].mean().round(4)

df.describe().transpose().round(4)
#this return the basic stats of my data frame that will be rounded off to 4 decimal places.
#unfortunately i do not much knowledge on machine learing aspects to do my regression analysis here yet.
#I'm trying to improve my skills in coding whilst actively studying to maintain a strong final year GPA, but i am learning as best i can.
#I will be able to do inference by years end (2026). That is my goal anyways.

df["tax_debt_ratio"]= df["TAXES"] / df["DEBT"]
df.head()
#The use of the tax-to-debt ratio controls for scale effects and inflationary trend, which will make my regression analysis far more accurate.


#PLEASE READ SUB CLAIM 4- GOVERNMENT FINANCES & REVENUE, this will give the bigger picture of the arguement I was builiding.


