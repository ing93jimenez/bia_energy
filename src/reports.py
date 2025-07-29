from src.db import get_engine
import pandas as pd

engine = get_engine()

# Top códigos postales
top_postcodes = pd.read_sql("""
SELECT postcode, COUNT(*) AS cantidad
FROM enriched_postcodes
WHERE postcode IS NOT NULL
GROUP BY postcode
ORDER BY cantidad DESC
LIMIT 10
""", engine)
top_postcodes.to_csv("output/top_postcodes.csv", index=False)

# % sin código postal
stats = pd.read_sql("""
SELECT 
    COUNT(*) FILTER (WHERE postcode IS NULL) * 100.0 / COUNT(*) AS pct_sin_postcode
FROM enriched_postcodes
""", engine)
stats.to_csv("output/data_quality.csv", index=False)