"""
us_census.py

Functions:
    - us_census_connector: Extracts data from JSON URL
    - us_census_formatter: Cleans and format data
    - us_census: Combines the two previous functions

Data Credits:
    The United States Census Bureau
    https://data.census.gov/
"""

import pandas as pd
import fips_codes

URL = 'https://api.census.gov/data/2019/pep/population?get=LASTUPDATE,POP,DENSITY,UNIVERSE&for=county:*&in=state:*&key=5436a8b95e523baaa40c22ec906af88a93f405eb'
API_KEY = '5436a8b95e523baaa40c22ec906af88a93f405eb'


def us_census():
    """Data Source for the US census.

    Arguments:
        None

    Returns:
        pandas.DataFrame
    """
    df = us_census_connector()
    return us_census_formatter(df)


def us_census_connector():
    """Extract data from the US Census.


    Description:
        - Opens the zip file URL and extracts the correct CSV
        - Correct CSV: ACS 5Y Statistics

    Returns:
        data (DataFrame with CSV Data)
    """

    data = pd.read_json(URL)
    return data


def us_census_formatter(data):
    """Formatter for US Census.

    Arguments:
        data(pandas.DataFrame): Data as returned by us_census_connector.

    Description:
        - Set columns
        - Rename and lower column names
        - Format dates
        - Enrich state and county data

    Returns:
        pandas.DataFrame
    """
    columns = list(data.iloc[0].map(lambda column: column.lower()))
    columns[columns.index('lastupdate')] = 'last_update'
    columns[columns.index('pop')] = 'population_estimate'
    data.columns = columns
    data.drop(0, inplace=True)
    data["state_name"] = data["state"].apply(lambda state : fips_codes.state_fips_to_name(state))
    data["county_name"] = data["state"] + data["county"]
    data["county_name"] = data["county_name"].apply(lambda county : fips_codes.county_fips_to_name(county))
    data['last_update'] = pd.to_datetime(data.last_update)

    return data
