# BlobCity SampleData Module

## Overview

The `SampleData` module in the `BlobCity` package provides easy access to pre-stored datasets for classification and regression tasks. It allows users to list available datasets and load them efficiently for quick experimentation.

## Features

- 📂 **List Available Datasets**: Fetch the names of available classification and regression datasets.
- 📊 **Load Datasets**: Load datasets directly into Pandas DataFrames.

## Usage

### Import the Module

```python
from blobcity import SampleData
```

### Initialize the `SampleData` Class

```python
data_loader = SampleData()
```

### List Available Datasets

```python
datasets = data_loader.get_datasets_namespace()
print(datasets)
```

#### Example Output:
```python
{
    'classification': ['iris', 'mnist', 'spam'],
    'regression': ['housing', 'sales', 'temperature']
}
```

### Load a Classification Dataset

```python
df = data_loader.get_classification_dataset("iris")
print(df.head())
```

### Load a Regression Dataset

```python
df = data_loader.get_regression_dataset("insurance")
print(df.head())
```

## Error Handling

If a dataset is missing, an appropriate error message is shown:

```python
FileNotFoundError: "Dataset 'nonexistent.pkl' not found in classification directory."
```

## Directory Structure

The datasets are stored in a predefined structure inside the package:

```
blobcity/
│── data_store/
│   │── classification/
│   │   ├── iris.pkl
│   │── regression/
│   │   ├── insurance.pkl
```


