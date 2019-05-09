# Executive Dashboard Master

[Original project description](https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/projects/exec-dash.md)
With this application, user's will able to view monthly sales data information in a friendly manner: via graph and via user-friendly code

## Monitor Build Status
[![Build Status](https://travis-ci.com/sambeyda/Exec-Dashboard.svg?branch=revisited-testing)](https://travis-ci.com/sambeyda/Exec-Dashboard)

## PREREQUISITES
Python 3.x
Pip
Anaconda

## INSTALLATION

Clone or download from [GitHub source](https://github.com/sambeyda/Exec-Dashboard),then navigate to project repository

Install the necessary packages
```
pip install -r requirements.txt
```

## USAGE

Navigate to app folder and run the shopping cart script:

```
python app/Monthly_sales.py
```

Within the script, you will be prompted to select the month and year of the sales data you wish to visualize

## TESTING

To test, install the `pytest` package if necessary, perhaps within a virtual environment
```
pip install pytest
``` 
And invoke it from the root directory of this repository to run tests:

```py
pytest
```

