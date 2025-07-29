import pandas as pd
from src.db import get_engine, init_db
from src.enrich import enrich_coordinates

init_db()

# Cargar datos
print("Leyendo CSV...")
df = pd.read_csv("data/postcodesgeo.csv")
df = df.drop_duplicates(subset=["latitude", "longitude"])
df = df.dropna(subset=["latitude", "longitude"])

# Enriquecer
print("Enriqueciendo datos...")
enriched = enrich_coordinates(df)

# Almacenar en base de datos
print("Insertando en DB...")
enriched.to_sql("enriched_postcodes", get_engine(), if_exists="append", index=False)