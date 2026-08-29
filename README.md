# Special Training
# Special Training

This workspace contains a lightweight setup for Data Science and Hugging Face workflows (RAG, embeddings, fine-tuning). It includes a `requirement.txt` with commonly-used packages and instructions to reproduce the environment locally.

**Quick summary**:
- **Purpose:** Data science experiments, Jupyter notebooks, Hugging Face models, embeddings, and RAG prototypes.
- **Python:** Tested with Python 3.10+ (this workspace used Python 3.14).
- **Requirements file:** `requirement.txt`

**Install (recommended: virtual environment)**

PowerShell / Windows (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirement.txt
```

Or using a specific Python executable:

```powershell
C:/Users/narte/AppData/Local/Python/pythoncore-3.14-64/python.exe -m pip install -r requirement.txt
```

**Create Jupyter kernel (optional)**

```powershell
python -m ipykernel install --user --name special-training --display-name "Python (special-training)"
```

**Quick verification**

Run a short import check to confirm critical packages are available:

```powershell
python -c "import sys; import numpy, pandas, matplotlib, sklearn, torch; print('imports OK', sys.version)"]
```

If you plan to use GPU for PyTorch, ensure the appropriate CUDA/cuDNN drivers are installed and install a matching `torch` wheel from the official PyTorch instructions: https://pytorch.org/get-started/locally/

**Notes & tips**
- If you prefer reproducible dependency locking, create a `requirements.txt` with pinned versions or use `pip-tools` / `poetry` / `pipenv`.
- Some packages (e.g., `chromadb`, `modal`, GPU-enabled `torch`) may require system-level dependencies or optional extras.
- For large-model training and fine-tuning, consider using cloud instances with sufficient RAM/GPUs or services like Hugging Face Infinity / Modal.

**Files**
- `requirement.txt`: package list used for this workspace.

If you want, I can: create a virtual environment for you, pin package versions, or add a small example notebook to exercise the installed libraries—which should I do next?