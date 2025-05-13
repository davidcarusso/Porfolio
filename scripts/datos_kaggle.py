# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

def df_costo_educacion():
    # Set the path to the file you'd like to load
    file_path = "International_Education_Costs.csv"

    # Load the latest version
    df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "adilshamim8/cost-of-international-education",
    file_path,
    # Provide any additional arguments like 
    # sql_query or pandas_kwargs. See the 
    # documenation for more information:
    # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
    )
    
    ### Espacio para limpiar y modificar datos 
    
    df["Costo Alquiler Total"] =  df["Duration_Years"] * (df["Rent_USD"] * 12)
    df["Costo Seguro Total"] =  df["Insurance_USD"] * df["Duration_Years"]
    df["Costo Carrera Final"] = df["Costo Alquiler Total"] + df["Costo Seguro Total"] + df["Visa_Fee_USD"] + df["Tuition_USD"]
    df["Costo Carrera por año"] = df["Costo Carrera Final"] / df["Duration_Years"]
    
    return df 