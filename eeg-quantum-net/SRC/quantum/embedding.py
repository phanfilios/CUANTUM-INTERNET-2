from __future__ import annotations
from typing import Union

import numpy as np
import pandas as pd
from qiskit import QuantumCircuit


def eeg_to_quantum_embedding(
    features: Union[pd.Series, pd.DataFrame, np.ndarray],
    num_qubits: int = 100
) -> QuantumCircuit:
    """
    Convierte un vector de características EEG en un embedding cuántico
    usando rotaciones RY en un circuito de Qiskit.

    Parámetros
    ----------
    features : Union[pd.Series, pd.DataFrame, np.ndarray]
        Características agregadas del EEG.
    num_qubits : int
        Número de qubits del circuito cuántico.

    Returns
    -------
    QuantumCircuit
        Circuito cuántico con el embedding aplicado.
    """


    if isinstance(features, pd.DataFrame):
        arr = features.values.flatten().astype(float)
    elif isinstance(features, pd.Series):
        arr = features.to_numpy(dtype=float)
    elif isinstance(features, np.ndarray):
        arr = features.astype(float).flatten()
    else:
        raise TypeError("features debe ser DataFrame, Series o ndarray")


    def normalize(v: np.ndarray) -> np.ndarray:
        """Normaliza valores entre -π y π."""
        v = np.nan_to_num(v)  
        max_val = np.max(np.abs(v)) or 1.0
        return (v / max_val) * np.pi

    arr = normalize(arr)

  
    qc = QuantumCircuit(num_qubits)

    limit = min(num_qubits, len(arr))

  
    for i in range(limit):
        qc.ry(float(arr[i]), i)

    return qc