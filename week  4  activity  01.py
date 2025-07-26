import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
credit_df = pd.read_csv("C:/Users/user3/Music/datasets/creditcard_pprd.csv")
print(credit_df.head(10))
credit_df.plot(x='age',y='income',kind='scatter',marker='o',color="blue")
plt.show()
