import pandas as pd

# given data
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Creating data frame
data_frame = pd.DataFrame(data)

# Adding a new column using existing column
data_frame["A*B"] = data_frame["A"] * data_frame["B"]

# Printing final DataFrame
print(data_frame)
