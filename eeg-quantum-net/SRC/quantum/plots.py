
import matplotlib.pyplot as plt
import pandas as pd

def plot_band_distribution(df: pd.DataFrame, figsize=(12, 8)):
    """
    Genera histogramas para cada columna numérica del DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con las bandas EEG o cualquier conjunto de características numéricas.
    figsize : tuple
        Tamaño de la figura.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Figura generada para poder guardarla o procesarla externamente.
    """


    if df is None or df.empty:
        raise ValueError("El DataFrame está vacío o no es válido.")


    fig = plt.figure(figsize=figsize)

  
    df.hist(figsize=figsize)

    plt.tight_layout()
    plt.close(fig)  
    return fig