import pandas as pd
crosslinkage_table = pd.read_csv("/data/crosslinkage_table.csv")
crosslinkage_table.head()
columns=list(crosslinkage_table.columns)

print(crosslinkage_table.isnull().mean())
print(crosslinkage_table.dtypes)
for i in str_cols:
    crosslinkage_table[i] = crosslinkage_table[i].str.strip()

data_bgmeasures=pd.read_csv("/data/date_bgmeasures.csv")
data_bgmeasures.head()
columns=list(data_bgmeasures.columns)

print(data_bgmeasures.isnull().mean())
print(data_bgmeasures.dtypes)
for i in str_cols:
    data_bgmeasures[i] = data_bgmeasures[i].str.strip()

data_bgmonitoring=pd.read_csv("/data/data_bgmonitoring.csv")
data_bgmeasures.head()
columns=list(data_bgmonitoring.columns)

print(data_bgmonitoring.isnull().mean())
print(data_bgmonitoring.dtypes)
for i in str_cols:
    data_bgmonitoring[i] = data_bgmonitoring[i].str.strip()

data_bgnon_native_bird=pd.read_csv("data/data_bgnon_native_bird.csv")
data_bgnon_native_bird.head()
columns=list(data_bgnon_native_bird.columns)

print(data_bgnon_native_bird.isnull().mean())
print(data_bgnon_native_bird.dtypes)
for i in str_cols:
    data_bgnon_native_bird[i] = data_bgnon_native_bird[i].str.strip()

data_bgpublication=pd.read_csv("data/data_bgpublication.csv")
data_bgpublication.head()
columns=list(data_bgpublication.columns)

print(data_bgpublication.isnull().mean())
print(data_bgpublication.dtypes)
for i in str_cols:
    data_bgpublication[i] = data_bgpublication[i].str.strip()

data_bgreport=pd.read_csv("data/data_bgreport.csv")
data_bgreport.head()
columns=list(data_bgreport.columns)

print(data_bgreport.isnull().mean())
print(data_bgreport.dtypes)
for i in str_cols:
    data_bgreport[i] = data_bgreport[i].str.strip()

data_birds_check_list=pd.read_csv("data/data_birds_check_list.csv")
data_birds_check_list.head()
columns=list(data_birds_check_list.columns)

print(data_birds_check_list.isnull().mean())
print(data_birds_check_list.dtypes)
for i in str_cols:
    data_birds_check_list[i] = data_birds_check_list[i].str.strip()

data_birds_eu_breeding_trends=pd.read_csv("data/data_birds_eu_breeding_trends.csv")
data_birds_eu_breeding_trends.head()
columns=list(data_birds_eu_breeding_trends.columns)

print(data_birds_eu_breeding_trends.isnull().mean())
print(data_birds_eu_breeding_trends.dtypes)
for i in str_cols:
    data_birds_eu_breeding_trends[i] = data_birds_eu_breeding_trends[i].str.strip()

data_birds_eu_status=pd.read_csv("data/data_birds_eu_status.csv")
data_birds_eu_status.head()
columns=list(data_birds_eu_status.columns)

print(data_birds_eu_status.isnull().mean())
print(data_birds_eu_status.dtypes)
for i in str_cols:
    data_birds_eu_status[i] = data_birds_eu_status[i].str.strip()

data_birds_eu_wintering_trends=pd.read_csv("data/data_birds_eu_wintering_trends.csv")
data_birds_eu_wintering_trends.head()
columns=list(data_birds_eu_wintering_trends.columns)

print(data_birds_eu_wintering_trends.isnull().mean())
print(data_birds_eu_wintering_trends.dtypes)
for i in str_cols:
    data_brids_eu_wintering_trends[i] = data_brids_eu_wintering_trends[i].str.strip()

data_birds=pd.read_csv("data/data_birds.csv")
data_birds.head()
columns=list(data_birds.columns)

print(data_birds.isnull().mean())
print(data_birds.dtypes)
for i in str_cols:
    data_birds[i] = data_birds[i].str.strip()

data_bmeasures=pd.read_csv("data/data_bmeasures.csv")
data_bmeasures.head()
columns=list(data_bmeasures.columns)

print(data_bmeasures.isnull().mean())
print(data_bmeasures.dtypes)
for i in str_cols:
    data_bmeasures[i] = data_bmeasures[i].str.strip()

data_bpressures_threats=pd.read_csv("data/data_bpressures_threats.csv")
data_bpressures_threats.head()
columns=list(data_bpressures_threats.columns)

print(data_bpressures_threats.isnull().mean())
print(data_bpressures_threats.dtypes)
for i in str_cols:
    data_bpressures_threats[i] = data_bpressures_threats[i].str.strip()

species_birds_maes_EU27=pd.read_csv("data/species_birds_maes_EU27.csv")
species_birds_maes_EU27.head()
columns=list(species_birds_maes_EU27.columns)

print(species_birds_maes_EU27.isnull().mean())
print(species_birds_maes_EU27.dtypes)
for i in str_cols:
    species_birds_maes_EU27[i] = species_birds_maes_EU27[i].str()
    


