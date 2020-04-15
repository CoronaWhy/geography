# US Census

## General information

- **Description**: Annual Population Estimates for the United States, States and Counties: April 1, 2010 to July 1, 2019.
- **Credits**: The United States Census Bureau https://data.census.gov/.
- **Source**: [API Source](https://api.census.gov/data/2019/pep/population?get=LASTUPDATE,POP,DENSITY,UNIVERSE&for=county:*&in=state:*)

## Description

**last_update**
- Description: Last update of estimation
- Type: datetime

**population_estimate**
- Description: Population estimate of county
- Type: integer

**density**
- Description: Population density of county
- Type: float

**state**
- Description: FIPS Code of county state
- Type: string

**county**
- Description: FIPS Code of county
- Type: string

**state_name**
- Description: Name of county state
- Type: string

**county_name**
- Description: Name of county
- Type: string

## Transformations applied

- Remove columns from first rows and set them to the dataframe
- Rename "lastupdate" and "pop" columns well formatted and with more explicit names
- Create a column "state_name" with the state name of the FIPS code in "state" column
- Create a column "county_name" with the state name of the FIPS code in "county" column
