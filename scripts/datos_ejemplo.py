import pandas as pd
import numpy as np

def generar_datos():
    # generar datos sintecos 
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    categories = ["Electrónicos", "Ropa", "Alimentos", "Hogar"]
    regions = ["Norteamérica", "Sudamérica", "Europa", "Asia", "África"]

    data = {
        "Fecha": np.random.choice(dates, 500),
        "Categoria": np.random.choice(categories, 500),
        "Region": np.random.choice(regions, 500),
        "Ventas": np.random.randint(100, 5000, 500),
        "Beneficio": np.random.uniform(50, 2500, 500),
        "Rating": np.random.uniform(1, 5, 500),
        "Latitud": np.random.uniform(-50, 70, 500),
        "Longitud": np.random.uniform(-180, 180, 500)
    }

    return data


