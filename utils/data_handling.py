import pandas as pd
import h5py  # For HDF5 support


def load_data(data_path, format):
    """
    Loads data from various formats (CSV, JSON, HDF5).

    Args:
        data_path (str): The path to the data file.
        format (str): The format of the data (e.g., 'csv', 'json', 'hdf5').

    Returns:
        pandas.DataFrame or numpy.ndarray: The loaded data.

    Raises:
        ValueError: If the data format is not supported.
    """
    if format == 'csv':
        return pd.read_csv(data_path)
    elif format == 'json':
        with open(data_path, 'r') as f:
            return json.load(f)
    elif format == 'hdf5':
        with h5py.File(data_path, 'r') as f:
            return f['data'][:]  # Assuming data is in a dataset named 'data'
    else:
        raise ValueError(f"Unsupported data format: {format}")


def preprocess_data(data):
    """
    Preprocesses data for further use.

    Args:
        data (pandas.DataFrame or numpy.ndarray): The data to be preprocessed.

    Returns:
        The preprocessed data.

    This function is a placeholder for specific preprocessing techniques
    (e.g., normalization, scaling, one-hot encoding) that can be implemented
    based on the task and data type.
    """
    # Implement your specific preprocessing logic here
    # ...
    return data