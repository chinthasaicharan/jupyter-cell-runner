
# `cell_runner`

`cell_runner` is a Python command-line tool that allows you to execute a specific code cell from a Jupyter notebook (`.ipynb` file) directly from the command line. It is particularly useful when you want to run a single code cell from a notebook without opening the Jupyter interface.

## Features

- Execute any specific code cell from a Jupyter notebook (`.ipynb` file) via CLI.
- Works without requiring the entire notebook to be executed or opened.
- Simple and easy-to-use.

## Installation

You can install `cell_runner` locally by running the following command:

```bash
pip install cell-runner
```

## Requirements

Make sure you have the following dependencies installed before using `cell_runner`:

- Python 3.6 or higher
- Jupyter (for working with `.ipynb` files)
- json
- subprocess
- argparse (comes with Python 3.6+)

You can install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

Once installed, you can use the `cell_runner` command to run a code cell from a Jupyter notebook.

### Command Syntax

```bash
cell_runner <notebook_file> <cell_index>
```

- `<notebook_file>`: The path to the `.ipynb` file (Jupyter notebook).
- `<cell_index>`: The index of the code cell to execute (starting from 0).

### Examples

#### 1. Running a specific cell from a notebook

To execute the code in the 3rd cell (index 2) of a notebook named `example.ipynb`:

```bash
cell_runner example.ipynb 2
```

#### 2. Handling Errors

- **If the file is not a Jupyter notebook**:
  If you pass a file that does not end with `.ipynb`, you'll see an error:

  ```bash
  File must be a .ipynb file
  ```

- **If the cell index is out of range**:
  If you specify an index that is out of the range of available code cells, the tool will raise an error:

  ```bash
  Cell index is out of range. Please check the cell index. (Index starts from 0)
  ```

### Example Notebook

Suppose `example.ipynb` has the following cells:

- **Cell 0**:

  ```python
  print("Cell 0")
  ```

- **Cell 1**:

  ```python
  print("Cell 1")
  ```

- **Cell 2**:

  ```python
  print("Cell 2")
  ```

Running the command:

```bash
cell_runner example.ipynb 1
```

Will execute the code in **Cell 1**, and you will see the following output:

```bash
Cell 1
```

## Testing

To test the functionality of the `cell_runner` package, you can use the following steps:

1. Create a test Jupyter notebook (`test.ipynb`) with several code cells.
2. Run the `cell_runner` command on various cell indices to ensure that the correct cell is executed.

For example, to run a test on the 1st cell (index 0):

```bash
cell_runner test.ipynb 0
```

Additionally, you can add automated tests using `pytest`:

```bash
pip install pytest
pytest tests/
```

Make sure you have test cases in the `tests/` directory.

## Development

To contribute or modify the package, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd my_python_package
   ```

2. Install the package in editable mode:

   ```bash
   pip install -e .
   ```

3. Modify the code as needed in the `cell_runner` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
