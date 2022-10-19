import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Backend/table.csv")
# data.head(10)
# data = d.copy()

# data.columns
# d.head(5)
l = []
for i in range(0, len(data)):
    # d["venue"][i] = list(' '.split(d["venue"][i]))[-2]
    l.append(data["venue"][i].split()[-1])

data["location"] = l

data = data.to_csv("sample.csv", index=False)

print(data)



# data.venue.value_counts(dropna=False).sort_index().plot(kind='barh')
# plt.show()