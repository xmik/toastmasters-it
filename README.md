# toastmasters-it

Operations scripts for ToastMasters.

## Usage
### `tm.py`
This script prints the dates needed for filling a form on toastmasters.org in order to request an award (like Competent Leader). It extracts the dates from a html file that comes from an Easy Speak website.


In order to run it:

1. The file `source.html` must exist in the current directory. Take the contents from the easy speak:
  This Club -> Club Charts -> Leadership Chart

2. Install dependencies:
```
$ source venv/bin/activate
$ pip install -r requirements.txt
```

3. Run the script. To get the dates for all the users:
```
$ python tm.py
```

  To get the dates for a specified user, e.g.:

  ```
  $ python tm.py "User Eleventh"
  User Eleventh
  Ah-Counter - 02 Jul 19
  07/02/2019

  Speaker - 18 Jun 19
  Timekeeper - 21 May 19
  06/18/2019
  ```

The dates in American notation, e.g. 06/18/2019 should be entered on the toastmasters.org website.

## Test
Run tests with:
```
$ pytest tm_test.py
```
