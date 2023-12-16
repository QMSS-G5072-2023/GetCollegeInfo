import requests
import pandas as pd
import json
import os

"""
    Obtains summary information on colleges throughout the United States, including admissions, tuition, demographics.

    Parameters:
    - college_name_input (str): The name of the college to be queried.
    - api_key (str): The API key.

    Returns:
    - Prints information results from college query.

    This function first checks whether the user has put in the college name as intended, since many colleges have similar names. If there is
    more than one similar name, the user must pick from the list of possible matching colleges. Once the user has input the correct college name,
    the user will retrieve results related to summary information, which may be useful if the user is interested in that college, or is just
    curious about the information. 

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
    
"""


def get_college_info(college_name, api_key):
    # College Scorecard API for schools
    endpoint = "https://api.data.gov/ed/collegescorecard/v1/schools"
    
    # Parameters
    params = {
        "api_key": api_key,
        "school.name": college_name,
        "fields": "id,school.name,latest.admissions.admission_rate.overall,"
                   "latest.admissions.sat_scores.midpoint,"
                   "latest.admissions.act_scores.midpoint,"
                   "latest.student.demographics.race_ethnicity,"
                   "latest.student.demographics.men,"
                   "latest.student.demographics.women,"
                   "latest.cost.tuition.in_state,"
                   "latest.cost.tuition.out_of_state,"
                   "latest.completion.completion_rate_4yr_150nt,"
                   "school.city,school.state,"
                   "latest.school.endowment.end,"
                   "latest.school.ownership,"
                   "latest.student.size,"
                   "latest.student.grad_students" 
    }


    # Request get from API
    response = requests.get(endpoint, params=params)

    # Check the status of the request
    if response.status_code == 200:
        data = response.json()['results']  # Access data under 'results'
        if not data:
            print(f"No information found for {college_name}. Please check the college name.")
            return None

    # Create a DataFrame from the response to array data
    df = pd.json_normalize(data)


    # Check if there are multiple matches and ask the user to specify one if so
    if len(df) > 1:
        print(f"Multiple possible matches found for '{college_name}'. Please specify one below and reinput into the function:")
        for idx, row in df.iterrows():
            print(f"{idx + 1}. {row['school.name']}")
        return None
            
    # Extract relevant information from our DataFrame
    college_info = {
            "Name": college_name,
            "Location": f"{df['school.city'].iloc[0]}, {df['school.state'].iloc[0]}",
            "Ownership (1. Public, 2. Private, non-profit, 3. Private, for-profit)": df['latest.school.ownership'].iloc[0],
            "Endowment": f"${round(df['latest.school.endowment.end'].iloc[0]/1000000000,2)} billion",
            "Admission Rate": df['latest.admissions.admission_rate.overall'].iloc[0],
            "Graduation Rate": df['latest.completion.completion_rate_4yr_150nt'].iloc[0],
            "Tuition (In-State)": f"${df['latest.cost.tuition.in_state'].iloc[0]}",
            "Tuition (Out-of-State)": f"${df['latest.cost.tuition.out_of_state'].iloc[0]}",
            
            "Average SAT Scores": {
                "Reading": df['latest.admissions.sat_scores.midpoint.critical_reading'].iloc[0],
                "Math": df['latest.admissions.sat_scores.midpoint.math'].iloc[0],
                "Writing": df['latest.admissions.sat_scores.midpoint.writing'].iloc[0],
            },
            
            "Average ACT Scores": {
                "Cumulative": df['latest.admissions.act_scores.midpoint.cumulative'].iloc[0],
                "English": df['latest.admissions.act_scores.midpoint.english'].iloc[0],
                "Math": df['latest.admissions.act_scores.midpoint.math'].iloc[0],
                "Writing": df['latest.admissions.act_scores.midpoint.writing'].iloc[0],
            },
            
            "Race Demographics": {
                "White": df['latest.student.demographics.race_ethnicity.white'].iloc[0],
                "Black": df['latest.student.demographics.race_ethnicity.black'].iloc[0],
                "Hispanic": df['latest.student.demographics.race_ethnicity.hispanic'].iloc[0],
                "Asian": df['latest.student.demographics.race_ethnicity.asian'].iloc[0],
                "Two or More": df['latest.student.demographics.race_ethnicity.two_or_more'].iloc[0],
            },
            
            "Sex Demographics": {
                "Male": df['latest.student.demographics.men'].iloc[0],
                "Female": df['latest.student.demographics.women'].iloc[0],
            },
            
            "Student Size": {
                "Undergrad": df['latest.student.size'].iloc[0],
                "Grad": df['latest.student.grad_students'].iloc[0],    
        }}
        
    return college_info

    # If the request was successful, print results
    if college_info:
        for key, value in college_info.items():
            print(f"{key}: {value}")

    
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return None