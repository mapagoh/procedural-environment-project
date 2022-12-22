import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

crosslinkage_table = pd.read_csv("/data/crosslinkage_table.csv")
plt.plot(crosslinkage_table)
plt.ylabel("Crosslinkage")
plt.show()

data_bgmeasures=pd.read_csv("/data/data_bgmeasures.csv")
plt.plot(data_bgmeasures)
plt.ylabel("Background Measures")
plt.show()

data_bgmonitoring=pd.read_csv("/data/data_bgmonitoring.csv")
plt.plot(data_bgmonitoring)
plt.ylabel("Background Monitoring")
plt.show()

data_bgnon_native_bird=pd.read_csv("data/data_bgnon_native_bird.csv")
plt.plot(data_bgnon_native_bird)
plt.ylabel("Native Bird")
plt.show()

data_bgpublication=pd.read_csv("data/data_bgpublication.csv")
plt.plot(data_bgpublication)
plt.ylabel("Background Publications")
plt.show()

data_bgreport=pd.read_csv("data/data_bgreport.csv")
plt.plot(data_bgreport)
plt.ylabel("Background Report")
plt.show()

data_birds_check_list=pd.read_csv("data/data_birds_check_list.csv")
plt.plot(data_birds_check_list)
plt.ylabel("Birds Check List")
plt.show()

data_birds_eu_breeding_trends=pd.read_csv("data/data_birds_eu_breeding_trends.csv")
plt.plot(data_birds_eu_breeding_trends)
plt.ylabel("Birds Eu Breeding Trends")
plt.show()

data_birds_eu_status=pd.read_csv("data/data_birds_eu_status.csv")
plt.plot(data_birds_eu_status)
plt.ylabel("Birds Eu Status")
plt.show()

data_birds_eu_wintering_trends=pd.read_csv("data/data_birds_eu_wintering_trends.csv")
plt.plot(data_birds_eu_wintering_trends)
plt.ylabel("Birds Eu Wintering Trends")
plt.show()

data_birds=pd.read_csv("data/data_birds.csv")
plt.plot(data_birds)
plt.ylabel("Birds")
plt.show()

data_bmeasures=pd.read_csv("data/data_bmeasures.csv")
plt.plot(data_bmeasures)
plt.ylabel("Bmeasures")
plt.show()

data_bpressures_threats=pd.read_csv("data/data_bpressures_threats.csv")
plt.plot(data_bpressures_threats)
plt.ylabel("Bpressures Threats")
plt.show()

species_birds_maes_EU27=pd.read_csv("data/species_birds_maes_EU27.csv")
plt.plot(species_birds_maes_EU27)
plt.ylabel("Birds Mae")
plt.show()
