import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

crosslinkage_table = pd.read_csv("/data/crosslinkage_table.csv")
speciesname=pd.DataFrame({"s":crosslinkage_table["speciesname"]})
assessment_specname_EU=pd.DataFrame({"a":crosslinkage_table["assessment_specname_EU"]})
data2=speciesname["s"].value_counts()
data3=assessment_specname_EU["a"].value_counts()
plt.plot(data2)
plt.plot(data3)


data_bgmeasures=pd.read_csv("/data/data_bgmeasures.csv")
sitename=pd.DataFrame({"s":data_bgmeasures["sitename"]})
project_year=pd.DataFrame({"p":data_bgmeasures["project_year"]})
data2=sitename["s"].value_counts()
data3=project_year["p"].value_counts()
plt.plot(data2)
plt.plot(data3)


data_bgmonitoring=pd.read_csv("/data/data_bgmonitoring.csv")
monitoring_title=pd.DataFrame({"m":data_bgmonitoring["monitoring_title"]})
monitoring_year=pd.DataFrame({"my":data_bgmonitoring["monitoring_year"]})
data2=monitoring_title["m"].value_counts()
data3=monitoring_year["my"].value_counts()
plt.plot(data2)
plt.plot(data3)


data_bgpublication=pd.read_csv("/data/data_bgpublication.csv")
other_publication_year=pd.DataFrame({"y":data_bgpublication["other_publication_year"]})
data2=other_publication_year["y"].value_counts()
plt.plot(data2)


data_birds_check_list=pd.read_csv("/data/data_birds_check_list.csv")
country=pd.DataFrame({"c":data_birds_check_list["country"]})
speciesname=pd.DataFrame({"s":data_birds_check_list["speciesname"]})
assessment_specname_EU=pd.DataFrame({"a":data_birds_check_list["assessment_specname_EU"]})
data2=country["c"].value_counts()
data3=speciesname["s"].value_counts()
data4=assessment_specname_EU["a"].value_counts()
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)


data_birds_eu_status=pd.read_csv("/data/data_birds_eu_status.csv")
season=pd.DataFrame({"s":data_birds_eu_status["season"]})
Population_status=pd.DataFrame({"p":data_birds_eu_status["Population_status"]})
population_size_unit=pd.DataFrame({"u":data_birds_eu_status["population_size_unit"]})
data2=season["s"].value_counts()
data3=Population_status["p"].value_counts()
data4=population_size_unit["u"].value_counts()
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)


data_birds=pd.read_csv("/data/data_birds.csv")
country=pd.DataFrame({"c":data_birds["country"]})
spa_population_unit=pd.DataFrame({"sp":data_birds["spa_population_unit"]})
season=pd.DataFrame({"s":data_birds["season"]})
sub_unit=pd.DataFrame({"su":data_birds["sub_unit"]})
data2=country["c"].value_counts()
data3=spa_population_unit["sp"].value_counts()
data4=season["s"].value_counts()
data5=sub_unit["su"].value_counts()
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)
plt.plot(data5)


species_birds_maes_EU27=pd.read_csv("/data/species_birds_maes_EU27.csv")
species_birds_maes_EU27.head(150)
speciesname=pd.DataFrame({"s":species_birds_maes_EU27["speciesname"]})
codeeco=pd.DataFrame({"c":species_birds_maes_EU27["codeeco"]})
sub_unit=pd.DataFrame({"su":species_birds_maes_EU27["sub_unit"]})
data2=speciesname["s"].value_counts()
data3=codeeco["c"].value_counts()
data4=sub_unit["su"].value_counts()
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)
