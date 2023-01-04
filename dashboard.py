import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import connection

table= "crosslinkage"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"s":df["speciesname"]})
col2=pd.DataFrame({"a":df["assessment_specname_EU"]})
data2=col1["s"].value_counts()
data3=col2["a"].value_counts()
plt.plot(data2)
plt.plot(data3)


table= "bgmeasures"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"s":df["sitename"]})
col2=pd.DataFrame({"p":df["project_year"]})
data2=col1["s"].value_counts()
data3=col2["p"].value_counts()
plt.plot(data2)
plt.plot(data3)


table= "bgmonitoring"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col2=pd.DataFrame({"p":df["monitoring_year"]})
data3=col2["p"].value_counts()
plt.plot(data3)


table= "bgpublication"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)
col2=pd.DataFrame({"p":df["other_publication_year"]})
data3=col2["p"].value_counts()
plt.plot(data3)


table= "data_bgreport"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"s":df["national_bird_atlas_year"]})
col2=pd.DataFrame({"p":df["national_bird_redlist_year"]})
data2=col1["s"].value_counts()
data3=col2["p"].value_counts()
plt.plot(data2)
plt.plot(data3)


table= "birds"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"a":df["country"]})
col2=pd.DataFrame({"b":df["speciesname"]})
col3=pd.DataFrame({"c":df["sub_unit"]})
col4=pd.DataFrame({"d":df["common_speciesname"]})
data2=col1["a"].value_counts()
data3=col2["b"].value_counts()
data4=col3["c"].value_counts()
data5=col4["d"].value_counts()
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)
plt.plot(data5)


table= "birds_check_list"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"a":df["country"]})
col2=pd.DataFrame({"b":df["speciesname"]})
col3=pd.DataFrame({"c":df["assessment_specname_EU"]})
data2=col1["a"].value_counts()
data3=col2["b"].value_counts()
data4=col3["c"].value_counts()
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)


table= "data_birds_eu_breeding_trends"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"a":df["population_size_unit"]})
data2=col1["a"].value_counts()
plt.plot(data2)


table= "data_birds_eu_status"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"a":df["season"]})
col2=pd.DataFrame({"b":df["Population_status"]})
col3=pd.DataFrame({"c":df["population_size_unit"]})
data2=col1["a"].value_counts()
data3=col2["b"].value_counts()
data4=col3["c"].value_counts()
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)


table= "data_bpressures_threats"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"a":df["pressurecode"]})
col2=pd.DataFrame({"b":df["rankingcode"]})
data2=col1["a"].value_counts()
data3=col2["b"].value_counts()
plt.plot(data2)
plt.plot(data3)


table= "species_birds_maes_EU27"

query= "SELECT * FROM " + table
cursor= connection.cursor()
cursor.execute(query)
data= cursor.fetchall()

df= pd.DataFrame(data, columns= cursor.column_names)

col1=pd.DataFrame({"a":df["speciesname"]})
col2=pd.DataFrame({"b":df["codeeco"]})
col3=pd.DataFrame({"c":df["sub_unit"]})
data2=col1["a"].value_counts()
data3=col2["b"].value_counts()
data4=col3["c"].value_counts()
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)
