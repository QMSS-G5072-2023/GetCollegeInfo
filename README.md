# cscqmsspkg

Python package that allows user to search information for a particular college

## Installation

```bash
$ pip install cscqmsspkg
```

## Usage
 Obtains summary information on colleges throughout the United States, including admissions, tuition, demographics.

    Parameters:
    - college_name_input (str): The name of the college to be queried.
    - api_key (str): The API key.

    Returns:
    - Prints information results from college query.

    This function first checks whether the user has put in the college name as intended, since many colleges have similar names. If there is
    more than one similar name, the user must pick from the list or be more specific and retry the function. Once the user has input the correct
    college name, the user will retrieve results related to summary information, which may be useful if the user is interested in that college, or
    is just curious about the information. 

     Examples
    --------
    >>> from cscqmsspkg import cscqmsspkg
    >>> college_name_input = "Michigan State University"  
    >>> api_key = 'api_key'
    >>> get_college_info(college_name_input, api_key)
    >>> returns: 
    
    [Name: Michigan State University
     Location: East Lansing, MI
     Ownership (1. Public, 2. Private, non-profit, 3. Private, for-profit): 1
     Endowment: $4.43 billion
     Admission Rate: 0.8325
     Graduation Rate: 0.8207
     Tuition (In-State): $14750
     Tuition (Out-of-State): $40562
     Average SAT Scores: {'Reading': 600, 'Math': 610, 'Writing': 520}
     Average ACT Scores: {'Cumulative': 26, 'English': 26, 'Math': 25, 'Writing': 9}
     Race Demographics: {'White': 0.6778, 'Black': 0.0729, 'Hispanic': 0.061, 'Asian': 0.0729, 'Two or More': 0.0369}
     Sex Demographics: {'Male': 0.4842, 'Female': 0.5158}
     Student Size: {'Undergrad': 38424, 'Grad': 11085}]

## Dependencies 
This package requires the following Python libraries:

Pandas
json
requests

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`cscqmsspkg` was created by Timothy Chu. It is licensed under the terms of the MIT license.

## Credits

`cscqmsspkg` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
# GetCollegeInfo
