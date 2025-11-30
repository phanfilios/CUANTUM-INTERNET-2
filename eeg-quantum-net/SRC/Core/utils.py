from datetime import datetime
import numpy as np
import pandas as pd

def current_timestamp():

    return datetime.utcnow().isoformat()

def ensure_numeric(df: pd.DataFrame, cols):
 
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def normalize_vector(vec):
    
    vec = np.array(vec, dtype=float)
    min_v, max_v = vec.min(), vec.max()
    if max_v - min_v == 0:
        return vec
    return (vec - min_v) / (max_v - min_v)

def safe_dict(object):

    if isinstance(object, (list, dict)):
        return object
    if hasattr(object, "_dict_"):
        return object._dict_
    return str(object)