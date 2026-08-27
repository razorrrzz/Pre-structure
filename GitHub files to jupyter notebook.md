# Pre-structure
# GitHub files to jupyter notebook 

Here is how you can use all the different methods tailored specifically to your file (`ProgressBar.py` from `razorrrzz/Pre-structure`).

---

### Load to the cell directly 
%load https://raw.githubusercontent.com/razorrrzz/Pre-structure/main/ProgressBar.py

### Way 1: Run it directly without showing the code (`%run`)
If you just want all the functions/classes inside `ProgressBar.py` available in your notebook right away:

```python
%run https://raw.githubusercontent.com/razorrrzz/Pre-structure/main/ProgressBar.py
```
*(Shift + Enter to run — everything defined in the script is now in memory)*

---

### Way 2: Download it using `curl` / `wget` and Import
Download the file directly into your current working folder on your device:

**Cell 1 (Download):**
```bash
!curl -O https://raw.githubusercontent.com/razorrrzz/Pre-structure/main/ProgressBar.py
```
*(Or `!wget https://raw.githubusercontent.com/razorrrzz/Pre-structure/main/ProgressBar.py`)*

**Cell 2 (Import and use it):**
```python
import ProgressBar
```

---

### Way 3: Clone the Whole GitHub Repository
Best if your project grows and has multiple files or folders:

**Cell 1 (Clone):**
```bash
!git clone https://github.com/razorrrzz/Pre-structure.git
```

**Cell 2 (Load the local file into a cell):**
```python
%load Pre-structure/ProgressBar.py
```

---

### Way 4: Fetch and Run using Pure Python (`requests` + `exec`)
This method works in any environment (including standard Python scripts) without relying on Jupyter magic commands:

```python
import requests

url = "https://raw.githubusercontent.com/razorrrzz/Pre-structure/main/ProgressBar.py"
code = requests.get(url).text

# Runs the code directly in your session
exec(code)
```

---

### Way 5: Programmatically write it into a New Cell
If you want Python code to dynamically fetch the code and **create a new notebook cell containing the code**:

```python
import requests
from IPython.core.getipython import get_ipython

url = "https://raw.githubusercontent.com/razorrrzz/Pre-structure/main/ProgressBar.py"
code = requests.get(url).text

# Injects the code directly into the next cell
get_ipython().set_next_input(code)
```
*(Run this cell, and a new cell will immediately appear below it filled with your GitHub code!)*

---

### Way 6: Download & Save directly with Python (No CLI tools needed)
If terminal commands (`curl`/`wget`) ever give errors on mobile (like in Pydroid 3), you can save the file locally using pure Python:

```python
import urllib.request

url = "https://raw.githubusercontent.com/razorrrzz/Pre-structure/main/ProgressBar.py"
urllib.request.urlretrieve(url, "ProgressBar.py")

print("File downloaded successfully!")
```
After running this, you can use:
```python
%load ProgressBar.py
```
