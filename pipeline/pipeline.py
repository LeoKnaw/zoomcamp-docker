import sys
import pandas as pd

day = sys.argv[1]

df = pd.DataFrame({"month": [2,55], "passengers": [34,63]})
df["day"] = sys.argv[1]
df.to_parquet("output{day}.parquet")

print(df)


print("fuck the pipeline. today is", day)