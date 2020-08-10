# %%
import pandas as pd
df = pd.read_csv('athlete_events.csv')
df.head()
df.shape
df.columns

# %%
gold_medallists = df[df['Medal'] == 'Gold']
print(gold_medallists)
silver_medallists = df[df['Medal'] == 'Silver']
bronze_medallists = df[df['Medal'] == 'Bronze']
non_medallists = df[df['Medal'].isna()]

# %%
import numpy as np
gold_medallists['Female'] = np.where(gold_medallists['Sex'] == 'F', 1, 0)
print(gold_medallists['Female'])
silver_medallists['Female'] = np.where(silver_medallists['Sex'] == 'F', 1, 0)
bronze_medallists['Female'] = np.where(bronze_medallists['Sex'] == 'F', 1, 0)
non_medallists['Female'] = np.where(non_medallists['Sex'] == 'F', 1, 0)

# %%
gold_medallists['Team'].value_counts()[:10]

# %%
silver_medallists['Team'].value_counts()[:10]

# %%
bronze_medallists['Team'].value_counts()[:10]

# %%
non_medallists['Team'].value_counts()[:10]

# %%
print(gold_medallists['Female'].value_counts())
print(silver_medallists['Female'].value_counts())
print(bronze_medallists['Female'].value_counts())
print(non_medallists['Female'].value_counts())

# %%
def mean_by_gender(df, analyze, gender = 'Female'):
    tmp_1 = df[df[gender] == 1][analyze]
    tmp_2 = df[df[gender] == 0][analyze]
    print("Media {} Mujeres en: {}".format(analyze, tmp_1.mean()))
    print("Media {} Hombres en: {}".format(analyze, tmp_2.mean()))

# %%
for i in [gold_medallists, silver_medallists, bronze_medallists, non_medallists]:
    mean_by_gender(i, 'Weight')

# %%
for i in [gold_medallists, silver_medallists, bronze_medallists, non_medallists]:
    mean_by_gender(i, 'Height')

# %%
