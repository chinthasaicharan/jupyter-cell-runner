import json
import subprocess
from typing import List

def cell_runner(file_name :str, cell_idx: int):
    if not file_name.endswith("ipynb"):
        raise NameError("File must be a .ipynb file")
    try:
        with open(file_name) as f:
            json_data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("File must be corrupted. Retry with a valid file.")

    code_cell_indices = get_code_cell_indices(json_data)
    if cell_idx not in code_cell_indices:
        raise ValueError("Cell index is out of range. Please check the cell index. fyi (idx starts from 0 to n)")
    cell_code_list = json_data["cells"][cell_idx]["source"]
    cell_code = "".join(cell_code_list)
    subprocess.run(["python", "-c", cell_code])



def get_code_cell_indices(json_var) -> List[int]:
    indices_of_code_cells = []
    for i, cell in enumerate(json_var["cells"]):
        if cell.get('cell_type') == "code":
            indices_of_code_cells.append(i)

    return indices_of_code_cells

cell_runner("exp.ipynb", 2)