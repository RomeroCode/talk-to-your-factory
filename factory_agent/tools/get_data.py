import pandas as pd

file_path='/workspaces/talk-to-your-factory/factory_agent/data/test_FD001.txt'

# Define the column names
columns = [
    'engine', 'cycle', 'mach', 'altitude', 'temperature', 
    'Fan inlet temperature (°R)',
    'LPC outlet temperature (°R)',
    'HPC outlet temperature (°R)',
    'LPT outlet temperature (°R)',
    'Fan inlet pressure (psia)',
    'bypass-duct pressure (psia)',
    'HPC outlet pressure (psia)',
    'Physical fan speed (rpm)',
    'Physical core speed (rpm)',
    'Engine pressure ratio (P50/P2)',
    'HPC outlet Static pressure (psia)',
    'Ratio of fuel flow to Ps30 (pps/psia)',
    'Corrected fan speed (rpm)',
    'Corrected core speed (rpm)',
    'Bypass Ratio',
    'Burner fuel-air ratio',
    'Bleed Enthalpy',
    'Required fan speed (rpm)',
    'Required fan conversion speed (rpm)',
    'High-pressure turbines Cool air flow (lbm/s)',
    'Low-pressure turbines Cool air flow (lbm/s)'
]

# Read the data into a DataFrame
df = pd.read_csv(file_path, 
                 sep=r"\s+", 
                 names=columns,
                 index_col=['engine', 'cycle'],
                 engine='python')


def get_engine_data_json(engine_id: int) -> dict:
    """
    Returns the current data of a specific engine in JSON (dict) format.
    
    Parameters:
        engine_id (int): The ID of the engine to retrieve data for.
        
    Returns:
        dict: A dictionary containing the data for the specified engine.
            If the engine ID is not found, returns a dictionary with an "error" key and message.

            Example success response:
                {
                    "engine_id": int,
                    "cycle": int,
                    "mach": float,
                    "altitude": float,
                    "temperature": float,
                    "Fan inlet temperature (°R)": float,
                    "LPC outlet temperature (°R)": float,
                    "HPC outlet temperature (°R)": float,
                    "LPT outlet temperature (°R)": float,
                    "Fan inlet pressure (psia)": float,
                    "bypass-duct pressure (psia)": float,
                    "HPC outlet pressure (psia)": float,
                    "Physical fan speed (rpm)": float,
                    "Physical core speed (rpm)": float,
                    "Engine pressure ratio (P50/P2)": float,
                    "HPC outlet Static pressure (psia)": float,
                    "Ratio of fuel flow to Ps30 (pps/psia)": float,
                    "Corrected fan speed (rpm)": float,
                    "Corrected core speed (rpm)": float,
                    "Bypass Ratio": float,
                    "Burner fuel-air ratio": float,
                    "Bleed Enthalpy": float,
                    "Required fan speed (rpm)": float,
                    "Required fan conversion speed (rpm)": float,
                    "High-pressure turbines Cool air flow (lbm/s)": float,
                    "Low-pressure turbines Cool air flow (lbm/s)": float
                }

            Example error response:
                {
                    "error": "Engine ID <id> not found."
                }
    """
    try:
        # Get all data for the given engine
        engine_data = df.loc[engine_id]

        # Get the last cycle (last row) for this engine
        last_cycle_data = engine_data.tail(1)

        # Rebuild full MultiIndex (engine, cycle) for clarity
        last_cycle_data.index = pd.MultiIndex.from_tuples(
            [(engine_id, last_cycle_data.index[0])],
            names=['engine', 'cycle']
        )

        # Convert to JSON-like dictionary
        return last_cycle_data.reset_index().to_dict('records')

    except KeyError:
        return {"error": f"Engine {engine_id} not found."}
