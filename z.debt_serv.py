import pandas as pd
import numpy as np
#for extensive comments and explanations please look a net_gov as the code is  very similar.
df = pd.read_excel(r"C:\Users\given\Desktop\ECM DATA PROJECT 2\SUB CLAIM 3.xlsx")
df.head()
df.tail()
df.info()
df = df.set_index('DATE')
df.head()
df.describe().round(2)
#there really isn't much do here, other python files have far detailed codes however this section of my data set( sub claim 2) does not have much.