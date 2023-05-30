import urllib.request
url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/cars_clus.csv'
filename = 'cars_clus.csv'
df=urllib.request.urlretrieve(url, filename)
import pandas as pd
pdf = pd.read_csv(filename)
pdf
