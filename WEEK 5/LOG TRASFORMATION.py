import pandas as pd
import numpy as np
import seaborn as sns

data = [1, 1, 10, 10, 15, 15, 20, 20, 30, 50, 120, 130, 120, 50, 30, 30,
        25, 20, 20, 15, 15, 13, 11, 9, 7, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2,
        2, 2, 1]
df = pd.DataFrame(data, columns=["positive Skewed"])
print(df)
df.boxplot(column='positive Skewed')
sns.histplot(df)

inp_array = df["positive Skewed"]
print("input array:", inp_array)
out_array = np.log10(inp_array)
print("out_array", out_array)

# Transformation
out_array.boxplot(column='positive Skewed')
# Distribution using transformations
sns.histplot(out_array)

# Reverting transformation
original_val = (10 ** out_array)
print('original values:', original_val)