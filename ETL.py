import pandas as pd
import sqlite3


file_path = 'production.xls'
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()
annual_data = df.groupby('API WELL  NUMBER')[['OIL', 'GAS', 'BRINE']].sum().reset_index()
conn = sqlite3.connect('production_data.db')
annual_data.to_sql('production', conn, if_exists='replace', index=False)
conn.close()

