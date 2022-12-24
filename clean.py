import pandas as pd
import inspect

crosslinkage_table = pd.read_csv("/data/crosslinkage_table.csv")
crosslinkage_table.head()
columns=list(crosslinkage_table.columns)
rows=crosslinkage_table.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
crosslinkage_table.to_sql("crosslinkage_table", if_exists="replace", index=False)
crosslinkage_table.tail()
crosslinkage_table.describe()
crosslinkage_table.sort_values(ascending=False)
crosslinkage_table.hist(figsize=(16, 12), bins=50)


print(crosslinkage_table.isnull().mean())
print(crosslinkage_table.dtypes)
for i in columns:
    crosslinkage_table[i] = crosslinkage_table[i].str.strip()

data_bgmeasures=pd.read_csv("/data/data_bgmeasures.csv")
data_bgmeasures.head()
columns=list(data_bgmeasures.columns)
rows=data_bgmeasures.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_bgmeasures.to_sql("data_bgmeasures", if_exists="replace", index=False)
data_bgmeasures.tail()
data_bgmeasures.describe()
data_bgmeasures.sort_values(ascending=False)
data_bgmeasures.hist(figsize=(16, 12), bins=50)

print(data_bgmeasures.isnull().mean())
print(data_bgmeasures.dtypes)
for i in columns:
    data_bgmeasures[i] = data_bgmeasures[i].str.strip()

data_bgmonitoring=pd.read_csv("/data/data_bgmonitoring.csv")
data_bgmonitoring=data_bgmonitoring.dropna(subset=["monitoring_year"])
data_bgmonitoring["monitoring_year"]=data_bgmonitoring["monitoring_year"].astype(int)
data_bgmonitoring.head()
columns=list(data_bgmonitoring.columns)
rows=data_bgmonitoring.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_bgmonitoring.to_sql("data_bgmonitoring", if_exists="replace", index=False)
data_bgmonitoring.tail()
data_bgmonitoring.describe()
data_bgmonitoring.sort_values(ascending=False)
data_bgmonitoring.hist(figsize=(16, 12), bins=50)

print(data_bgmonitoring.isnull().mean())
print(data_bgmonitoring.dtypes)
for i in columns:
    data_bgmonitoring[i] = data_bgmonitoring[i].str.strip()

data_bgnon_native_bird=pd.read_csv("data/data_bgnon_native_bird.csv")
data_bgnon_native_bird.head()
columns=list(data_bgnon_native_bird.columns)
rows=data_bgnon_native_bird.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_bgnon_native_bird.to_sql("data_bgnon_native_bird", if_exists="replace", index=False)
data_bgnon_native_bird.tail()
data_bgnon_native_bird.describe()
data_bgnon_native_bird.sort_values(ascending=False)
data_bgnon_native_bird.hist(figsize=(16, 12), bins=50)

print(data_bgnon_native_bird.isnull().mean())
print(data_bgnon_native_bird.dtypes)
for i in columns:
    data_bgnon_native_bird[i] = data_bgnon_native_bird[i].str.strip()

data_bgpublication=pd.read_csv("data/data_bgpublication.csv")
data_bgpublication.head()
columns=list(data_bgpublication.columns)
rows=data_bgpublication.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_bgpublication.to_sql("data_bgpublication", if_exists="replace", index=False)
data_bgpublication.tail()
data_bgpublication.describe()
data_bgpublication.sort_values(ascending=False)
data_bgpublication.hist(figsize=(16, 12), bins=50)

print(data_bgpublication.isnull().mean())
print(data_bgpublication.dtypes)
for i in columns:
    data_bgpublication[i] = data_bgpublication[i].str.strip()

data_bgreport=pd.read_csv("data/data_bgreport.csv")
data_bgreport=data_bgreport.dropna(subset=["national_bird_atlas_year"])
data_bgreport["national_bird_atlas_year"]=data_bgreport["national_bird_atlas_year"].astype(int)
data_bgreport=data_bgreport.dropna(subset=["national_bird_redlist_year"])
data_bgreport["national_bird_redlist_year"]=data_bgreport["national_bird_redlist_year"].astype(int)
data_bgreport=data_bgreport.dropna(subset=["plans_under_prep"])
data_bgreport["plans_under_prep"]=data_bgreport["plans_under_prep"].astype(int)
data_bgreport.head()
columns=list(data_bgreport.columns)
rows=data_bgreport.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_bgreport.to_sql("data_bgreport", if_exists="replace", index=False)
data_bgreport.tail()
data_bgreport.describe()
data_bgreport.sort_values(ascending=False)
data_bgreport.hist(figsize=(16, 12), bins=50)

print(data_bgreport.isnull().mean())
print(data_bgreport.dtypes)
for i in columns:
    data_bgreport[i] = data_bgreport[i].str.strip()

data_birds_check_list=pd.read_csv("data/data_birds_check_list.csv")
data_birds_check_list=data_birds_check_list.dropna(subset=["euringcode"])
data_birds_check_list["euringcode"]=data_birds_check_list["euringcode"].astype(int)
data_birds_check_list=data_birds_check_list.dropna(subset=["assessment_code_EU"])
data_birds_check_list["assessment_code_EU"]=data_birds_check_list["assessment_code_EU"].astype(int)
data_birds_check_list=data_birds_check_list.dropna(subset=["assessment_code_trend"])
data_birds_check_list["assessment_code_trend"]=data_birds_check_list["assessment_code_trend"].astype(int)
data_birds_check_list.head()
columns=list(data_birds_check_list.columns)
rows=data_birds_check_list.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_birds_check_list.to_sql("data_birds_check_list", if_exists="replace", index=False)
data_birds_check_list.tail()
data_birds_check_list.describe()
data_birds_check_list.sort_values(ascending=False)
data_birds_check_list.hist(figsize=(16, 12), bins=50)

print(data_birds_check_list.isnull().mean())
print(data_birds_check_list.dtypes)
for i in columns:
    data_birds_check_list[i] = data_birds_check_list[i].str.strip()

data_birds_eu_breeding_trends=pd.read_csv("data/data_birds_eu_breeding_trends.csv")
data_birds_eu_breeding_trends=data_birds_eu_breeding_trends.dropna(subset=["BrRngSizeRnd"])
data_birds_eu_breeding_trends["BrRngSizeRnd"]=data_birds_eu_breeding_trends["BrRngSizeRnd"].astype(int)
data_birds_eu_breeding_trends.head()
columns=list(data_birds_eu_breeding_trends.columns)
rows=data_birds_eu_breeding_trends.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_birds_eu_breeding_trends.to_sql("data_birds_eu_breeding_trends", if_exists="replace", index=False)
data_birds_eu_breeding_trends.tail()
data_birds_eu_breeding_trends.describe()
data_birds_eu_breeding_trends.sort_values(ascending=False)
data_birds_eu_breeding_trends.hist(figsize=(16, 12), bins=50)

print(data_birds_eu_breeding_trends.isnull().mean())
print(data_birds_eu_breeding_trends.dtypes)
for i in columns:
    data_birds_eu_breeding_trends[i] = data_birds_eu_breeding_trends[i].str.strip()

data_birds_eu_status=pd.read_csv("data/data_birds_eu_status.csv")
data_birds_eu_status=data_birds_eu_status.dropna(subset=["PopSizeMax"])
data_birds_eu_status["PopSizeMax"]=data_birds_eu_status["PopSizeMax"].astype(int)
data_birds_eu_status.head()
columns=list(data_birds_eu_status.columns)
rows=data_birds_eu_status.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_birds_eu_status.to_sql("data_birds_eu_status", if_exists="replace", index=False)
data_birds_eu_status.tail()
data_birds_eu_status.describe()
data_birds_eu_status.sort_values(ascending=False)
data_birds_eu_status.hist(figsize=(16, 12), bins=50)

print(data_birds_eu_status.isnull().mean())
print(data_birds_eu_status.dtypes)
for i in columns:
    data_birds_eu_status[i] = data_birds_eu_status[i].str.strip()

data_birds_eu_wintering_trends=pd.read_csv("data/data_birds_eu_wintering_trends.csv")
data_birds_eu_wintering_trends.head()
columns=list(data_birds_eu_wintering_trends.columns)
rows=data_birds_eu_wintering_trends.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_birds_eu_wintering_trends.to_sql("data_birds_eu_wintering_trends", if_exists="replace", index=False)
data_birds_eu_wintering_trends.tail()
data_birds_eu_wintering_trends.describe()
data_birds_eu_wintering_trends.sort_values(ascending=False)
data_birds_eu_wintering_trends.hist(figsize=(16, 12), bins=50)

print(data_birds_eu_wintering_trends.isnull().mean())
print(data_birds_eu_wintering_trends.dtypes)
for i in columns:
    data_birds_eu_wintering_trends[i] = data_birds_eu_wintering_trends[i].str.strip()

data_birds=pd.read_csv("data/data_birds.csv")
data_birds=data_birds.dropna(subset=["euringcode"])
data_birds["euringcode"]=data_birds["euringcode"].astype(int)
data_birds=data_birds.dropna(subset=["spa_population_min"])
data_birds["spa_population_min"]=data_birds["spa_population_min"].astype(int)
data_birds=data_birds.dropna(subset=["spa_population_max"])
data_birds["spa_population_max"]=data_birds["spa_population_max"].astype(int)
data_birds=data_birds.dropna(subset=["spa_population_method"])
data_birds["spa_population_method"]=data_birds["spa_population_method"].astype(int)
data_birds.head()
columns=list(data_birds.columns)
rows=data_birds.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_birds.to_sql("data_birds", if_exists="replace", index=False)
data_birds.tail()
data_birds.describe()
data_birds.sort_values(ascending=False)
data_birds.hist(figsize=(16, 12), bins=50)

print(data_birds.isnull().mean())
print(data_birds.dtypes)
for i in columns:
    data_birds[i] = data_birds[i].str.strip()

data_bmeasures=pd.read_csv("data/data_bmeasures.csv")
data_bmeasures.head()
columns=list(data_bmeasures.columns)
rows=data_bmeasures.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_bmeasures.to_sql("data_bmeasures", if_exists="replace", index=False)
data_bmeasures.tail()
data_bmeasures.describe()
data_bmeasures.sort_values(ascending=False)
data_bmeasures.hist(figsize=(16, 12), bins=50)

print(data_bmeasures.isnull().mean())
print(data_bmeasures.dtypes)
for i in columns:
    data_bmeasures[i] = data_bmeasures[i].str.strip()

data_bpressures_threats=pd.read_csv("data/data_bpressures_threats.csv")
data_bpressures_threats=data_bpressures_threats.dropna(subset=["quality"])
data_bpressures_threats["quality"]=data_bpressures_threats["quality"].astype(int)
data_bpressures_threats.head()
columns=list(data_bpressures_threats.columns)
rows=data_bpressures_threats.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
data_bpressures_threats.to_sql("data_bpressures_threats", if_exists="replace", index=False)
data_bpressures_threats.tail()
data_bpressures_threats.describe()
data_bpressures_threats.sort_values(ascending=False)
data_bpressures_threats.hist(figsize=(16, 12), bins=50)

print(data_bpressures_threats.isnull().mean())
print(data_bpressures_threats.dtypes)
for i in columns:
    data_bpressures_threats[i] = data_bpressures_threats[i].str.strip()

species_birds_maes_EU27=pd.read_csv("data/species_birds_maes_EU27.csv")
species_birds_maes_EU27=species_birds_maes_EU27.dropna(subset=["euringcode"])
species_birds_maes_EU27["euringcode"]=species_birds_maes_EU27["euringcode"].astype(int)
species_birds_maes_EU27.head()
columns=list(species_birds_maes_EU27.columns)
rows=species_birds_maes_EU27.shape[0]
for  data in inspect.getmembers(columns):
    if data.startswith('__'):
        continue
species_birds_maes_EU27.to_sql("species_birds_maes_EU27", if_exists="replace", index=False)
species_birds_maes_EU27.tail()
species_birds_maes_EU27.describe()
species_birds_maes_EU27.sort_values(ascending=False)
species_birds_maes_EU27.hist(figsize=(16, 12), bins=50)

print(species_birds_maes_EU27.isnull().mean())
print(species_birds_maes_EU27.dtypes)
for i in columns:
    species_birds_maes_EU27[i] = species_birds_maes_EU27[i].str.strip()

    


