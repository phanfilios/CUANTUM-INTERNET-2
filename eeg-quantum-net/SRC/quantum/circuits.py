from qiskit import QuantumCircuit
import numpy as np

def eeg_to_quantum_embedding(features, num_qubits=100):
    """
    Convierte un vector de características EEG en un estado cuántico
    usando codificación por ángulos (Angle Embedding).

    - Normaliza valores para evitar errores
    - Rellena si hay menos datos que qubits
    - Limita la amplitud angular para estabilidad

    Parámetros:
    -----------
    features : pandas.Series o numpy.ndarray
        Vector de características ya procesado (EEG features).
    num_qubits : int
        Número de qubits a usar (por defecto 100).

    Retorna:
    --------
    qc : QuantumCircuit
        Circuito de embedding listo para simulación.
    """


    if hasattr(features, "values"):
        arr = features.values.astype(float)
    else:
        arr = np.array(features, dtype=float)


    if np.max(np.abs(arr)) > 0:
        arr = arr / np.max(np.abs(arr))


    if len(arr) < num_qubits:
        padding = np.zeros(num_qubits - len(arr))
        arr = np.concatenate([arr, padding])


    arr = np.clip(arr, -1, 1) * np.pi


    qc = QuantumCircuit(num_qubits)

    for i in range(num_qubits):
        qc.ry(float(arr[i]), i)

    return qc