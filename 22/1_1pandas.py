import pandas as pd

df = pd.read_csv('input.txt', skip_blank_lines=True)
df.columns = ['cals']
df.sort_values(by=['cals'], ascending=False)
print(max(df['cals']))
