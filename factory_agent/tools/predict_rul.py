import pandas as pd

file_path = '/workspaces/talk-to-your-factory/factory_agent/data/RUL_FD001.txt'
df = pd.read_csv(file_path,
                 names=['RUL'],
                 engine='python')

df.index += 1

def predict_engine_rul(engine_id: int) -> int:
    """Get the prediction of the remaining useful life (RUL - cycles of the engine until failure).
    
    Args:
        engine_id (int): The ID from engine to get RUL

    Returns:
        A int with the number of remaining cycles until fail.
    """

    return int(df.loc[engine_id, 'RUL'])
