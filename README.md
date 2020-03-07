# toastmasters-it

Operations scripts for ToastMasters.

## Usage
### `tm.py`
This script prints the dates needed for filling a form on toastmasters.org in order to request an award (like Competent Leader). It extracts the dates from a html file that comes from an Easy Speak website.


In order to run it:
1. Overwrite the contents of source.html. Take the contents from the easy speak:
  This Club -> Club Charts -> Leadership Chart

2. Install dependencies:
```
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the script:
```
python tm.py
```
