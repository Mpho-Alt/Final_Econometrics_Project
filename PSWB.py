import pandas as pd
import numpy as np
df = pd.read_excel(r"C:\Users\given\Desktop\ECM DATA PROJECT 2\SUB CLAIM 2 DATA.xlsx")
#this is for sub claim 2, i will not comment much because majority of my code is explained in net_gov.py
# i will not be doing much in this code, apart from conditional filtering 
df.head()
df.tail()
df.index
df = df.set_index("DATE")
df.head()
df["GDP_rounded"] = df["GDP_2015B"].round(2)
df["GDP_rounded"]
#I am going to do some conditional filtering s its easier to state my conditions if my numbers are not long, hence the rounding.
df["GDP_rounded"].mean().round(2)
#the mean = np.float64(3275641.94), since we are looking at GDP, any gdp value greater then it's mean is a positive for the country
#Which is why I why i will be passing in that condition to see if there is a consistent trend of improvement within the economy.'
# And if so, is it a sustainable trend. 
df["GDP_rounded"] > 3275641.94
#the code produced the following results:
#(DATE
#1995    False
#1996    False
#1997    False
#1998    False
#1999    False
#2000    False
#2001    False
#2002    False
#2003    False
#2004    False
#2005    False
#2006    False
#2007    False
#2008    False
#2009    False
#2010    False
#2011     True
#2012     True
#2013     True
#2014     True
#2015     True
#2016     True
#2017     True
#2018     True
#2019     True
#2020     True
#2021     True
#2022     True
#2023     True
#2024     True

df["GDP_rounded"].iloc[16:29]
df["GDP_rounded"].loc['2011':"2024"]
#so now i got the exact entries in the series where South Africa showed positive GDP growth. 
# I did 2 methods of grabbing the rows to show i know both methods. I know it's a basic ability but i used struggle with indexing and slicing.
# for the purposes of coding and curiosity i will only focuse on the elements where GDP is greater than the mean.
df.describe().transpose().round(2)
df["GDP_rounded"].sort_values( ascending= False)
#suprising South Africa demonstrated consistent economic growth from 1995 to 2024. I suspected as much but defininetly not in 2019 however.
#this is why conding is very versatile because you get to investigate each data series in the same working directory far more easily than Excel/Eviews.

