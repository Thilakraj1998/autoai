import os
import pandas as pd
import warnings
from glob import glob

warnings.filterwarnings('ignore')

class SampleData:
    """
    A class to handle sample datasets stored in the package directory.
    
    This class provides methods to list available datasets and load specific datasets 
    for classification and regression tasks.
    """

    def __init__(self):
        """
        Initializes the SampleData class by determining the absolute path of the dataset directory.
        """
        self.dataset_directory = os.path.dirname(os.path.abspath(__file__))

    def get_datasets_namespace(self):
        """
        Lists all available datasets in the classification and regression directories.

        Returns:
            dict: A dictionary with two keys:
                - 'classification': List of available classification dataset names.
                - 'regression': List of available regression dataset names.
        """
        return {
            'classification': self._list_datasets('classification'),
            'regression': self._list_datasets('regression')
        }

    def get_classification_dataset(self, name):
        """
        Loads a classification dataset by name.

        Args:
            name (str): The name of the dataset (without extension).

        Returns:
            pandas.DataFrame: The loaded dataset.

        Raises:
            FileNotFoundError: If the dataset is not found in the classification directory.
        """
        return self._load_dataset('classification', name)

    def get_regression_dataset(self, name):
        """
        Loads a regression dataset by name.

        Args:
            name (str): The name of the dataset (without extension).

        Returns:
            pandas.DataFrame: The loaded dataset.

        Raises:
            FileNotFoundError: If the dataset is not found in the regression directory.
        """
        return self._load_dataset('regression', name)

    def _list_datasets(self, category):
        """
        Helper method to list all datasets in a specified category.

        Args:
            category (str): Either 'classification' or 'regression'.

        Returns:
            list: List of dataset names available in the specified category.
        """
        path = os.path.join(self.dataset_directory, category, "*.pkl")
        return [os.path.splitext(os.path.basename(file))[0] for file in glob(path)]

    def _load_dataset(self, category, name):
        """
        Helper method to load a dataset from a specified category.

        Args:
            category (str): Either 'classification' or 'regression'.
            name (str): The name of the dataset (without extension).

        Returns:
            pandas.DataFrame: The loaded dataset.

        Raises:
            FileNotFoundError: If the dataset is not found.
        """
        file_path = os.path.join(self.dataset_directory, category, f"{name}.pkl")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset '{name}.pkl' not found in '{category}' directory.")
        return pd.read_pickle(file_path)
