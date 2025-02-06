# Source Code Directory

The `src` folder is essential for organizing reusable code, utility functions, or larger projects. Here are some reasons to include a `src` folder:

## Benefits of a `src` Folder

- **Reusable Code**: Store functions, classes, and modules that can be imported and reused across multiple notebooks.
- **Separation of Concerns**: Keep core logic and data processing separate from the notebook, allowing the notebook to focus on exploration and visualization.
- **Version Control**: Easier to track changes and manage version control for code that is separated from the notebooks.
- **Collaboration**: Collaborators can work on the core code without interfering with the notebooks.
- **Testing**: Easier to write and run unit tests for code stored in separate Python files.

## Folder Structure

```
src
├── utils
│   ├── data_processing.py
│   ├── visualization.py
├── models
│   ├── linear_regression.py
│   ├── clustering.py
├── config
│   ├── config.yaml
├── scripts
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── data_loader.py
│   ├── feature_engineering.py
```

## Example Usage

You can import and use the functions from the `src` folder in your Jupyter Notebooks.

Example Notebook Cell:

```python
import pandas as pd
from src.utils.data_processing import clean_data

data = pd.read_csv('data/raw/data.csv')
cleaned_data = clean_data(data)
cleaned_data.head()
```