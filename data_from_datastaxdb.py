import cassandra
import pandas as pd

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
cloud_config= {
  'secure_connect_bundle':'secure-connect-mushroom.zip'}

auth_provider = PlainTextAuthProvider('bCBiZNtblSWhdGPsWUKGXOrp',
                                      '+pJ8dbf+0LCnx.5irEvLFAFHRHkXaZxpWAUZ-ti3MRMD0RCd4S6_LHnx5a.cDZKmQdXYSSEpP8PdbDdJfnfUprNv1WaO9kChZOa4LblR_8G88kyyKhNjGD3WDJK,gucY')

cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

session = cluster.connect('predictions')

columns = ['cap_color','odor','gill_spacing','gill_size','gill_color','stalk_shape','stalk_surface_above_ring',
           'stalk_surface_below_ring','stalk_color_above_ring','stalk_color_below_ring','ring_type','spore_print_color',
           'population','habitat','result']
values = []


data = session.execute("select * from predictions")

for cap_color,odor,gill_spacing,gill_size,gill_color,stalk_shape,stalk_surface_above_ring,stalk_surface_below_ring,stalk_color_above_ring,stalk_color_below_ring,ring_type,spore_print_color,population,habitat,result in data:
  values.append([cap_color,odor,gill_spacing,gill_size,gill_color,stalk_shape,stalk_surface_above_ring,stalk_surface_below_ring,stalk_color_above_ring,stalk_color_below_ring,ring_type,spore_print_color,population,habitat,result])


df= pd.DataFrame(values,columns = columns)

print(df.head())

df.to_csv('predictions.csv')