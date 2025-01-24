import kaggle
# downloading the zip file from kaggle
# kaggle datasets download ankitbansal06/retail-orders -f orders.csv -p retails 

# Extract file from zip file to csv
import zipfile
zip_ref = zipfile.ZipFile("retail/orders.csv.zip")
zip_ref.extractall("extractip_zip")# This extracts the csv and stored it the folder
zip_ref.close()

# Read  data csv file to handle null values
import pandas as pd
df = pd.read_csv("extract_zip_csv/orders.csv")
print(df.head(10))

