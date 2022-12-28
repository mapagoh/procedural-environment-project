import scipy as sp
import pandas as pd
import numpy as np
import scipy.integrate

from scipy import linealg
def integral(data, a, b):
    l=linealg.det(data)
    f=lambda x:np.exp(l**2)
    i=scipy.integrate.quad(f,a,b)

crosslinkage=pd.read_csv("/data/cosslinkage_table.csv")
l=linealg.det(crosslinkage)
f=lambda x:np.exp(l**2)
i=scipy.integrate.quad(f,0,1)

bgmeasures=pd.read_csv("/data/data_bgmeasures.csv")
l=linealg.det(bgmeasures)
f=lambda x:np.exp(l**2)
i=scipy.integrate.quad(f,0,2)

bgmonitoring=pd.read_csv("/data/data_bgmonitoring.csv")
l=linealg.det(bgmonitoring)
f=lambda x:np.exp(l**2)
i=scipy.integrate.quad(f,0,3)

bgnon_native_bird=pd.read_csv("/data/data_bgnon_native_bird.csv")
integral(bgnon_native_bird,0,4)

bgpublication=pd.read_csv("/data/data_bgpublication.csv")
integral(bgpublication,1,4)

bgreport=pd.read_csv("/data/data_bgreport.csv")
integral(bgreport,0.1,3)

birds_check_list=pd.read_csv("/data/data_birds_check_list.csv")
integral(birds_check_list,0.3,3)

birds_eu_breeding_trends=pd.read_csv("/data/data_birds_eu_breeding_trends.csv")
integral(birds_eu_breeding_trends,0.1,1)

birds_eu_status=pd.read_csv("/data/data_birds_eu_status.csv")
integral(birds_eu_status,0.5,1)

birds_eu_wintering_trends=pd.read_csv("/data/data_birds_eu_wintering_trends.csv")
integral(birds_eu_wintering_trends,0.4,5)

birds=pd.read_csv("/data/data_birds.csv")
integral(birds,0.1,6)

bmeasures=pd.read_csv("/data/data_bmeasures.csv")
integral(bmeasures,0.3,6)

bpressures_threats=pd.read_csv("/data/data_bpressures_threats.csv")
integral(bpressures_threats,0.5,5)

species_birds_maes_EU27=pd.read_csv("/data/data_species_birds_maes_EU27.csv")
integral(species_birds_maes_EU27,1,7)












