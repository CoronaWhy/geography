# Government Measures Dataset

## General information

- **Description**:

The **Oxford COVID-19 Government Response Tracker** (OxCGRT) Dataset, provides a systematic way to
track the stringency of government responses to COVID-19 across countries and time. Using a novel index that combines
various measures of government responses, the authors describe variation in government responses, explore whether rising
 stringency of response affects the rate of infection, and identify correlates of more or less stringent responses.


OxCGRT collects publicly available information on 13 indicators of government response (S1-S13). Nine of the indicators
(S1-S7, S12 and S13) take policies such as school closures, travel bans, etc. are recorded on an ordinal scale;
the remainder (S8-S11) are financial indicators such as fiscal or monetary measures.
For more details about the data go to: https://www.bsg.ox.ac.uk/research/research-projects/oxford-covid-19-government-response-tracker

- **Credits**:

HDX, Blavatnik School of Government, University of Oxford
- **Source**:

https://data.humdata.org/dataset/oxford-covid-19-government-response-tracker

## Columns in the refined dataset


 **country**:
- Description: Country
- Type: string

 **country_iso**:
- Description: Country Code in ISO2 format
- Type: string

 **date**:
- Description: Data in ISO format YYYY-MM-DD
- Type: date

 **s1_school closing**:
- Description: Social Distancing Flag
- Type: number

 **s1_isgeneral**:
- Description: Social Distancing Flag
- Type: number

 **s2_workplace closing**:
- Description: Social Distancing Flag
- Type: number

 **s2_isgeneral**:
- Description: Social Distancing Flag
- Type: number

 **s3_cancel public events**:
- Description: Social Distancing Flag
- Type: number

 **s3_isgeneral**:
- Description: Social Distancing Flag
- Type: number

 **s4_close public transport**:
- Description: Social Distancing Flag
- Type: number

 **s4_isgeneral**:
- Description: Social Distancing Flag
- Type: number

 **s5_public information campaigns**:
- Description: Social Distancing Flag
- Type: number

 **s5_isgeneral**:
- Description: Social Distancing Flag
- Type: number

 **s6_restrictions on internal movement**:
- Description: Social Distancing Flag
- Type: number

 **s6_isgeneral**:
- Description: Social Distancing Flag
- Type: number

 **s7_international travel controls**:
- Description: Social Distancing Flag
- Type: number

 **s8_fiscal measures**:
- Description: Social Distancing Flag
- Type: number

 **s9_monetary measures**:
- Description: Social Distancing Flag
- Type: number

 **s10_emergency investment in health care**:
- Description: Social Distancing Flag
- Type: number

 **s11_investment in vaccines**:
- Description: Social Distancing Flag
- Type: number

 **s12_testing framework**:
- Description: Social Distancing Flag
- Type: number

 **s13_contact tracing**:
- Description: Social Distancing Flag
- Type: number

 **confirmedcases**:
- Description: Confirmed COVID-19 Cases
- Type: number

 **confirmeddeaths**:
- Description: Confirmed deaths due to COVID-19
- Type: number

 **stringencyindex**:
- Description: A calculated measurement index which shows how a country is stringent w.r.t to social distancing policies
- Type: number

 **stringencyindexfordisplay**:
- Description: A calculated measurement index which shows how a country is stringent w.r.t to social distancing policies
- Type: number

## Transformations applied

- Removed columns with notes
- Changed column names to lower case
- Converted ISO3 country code to ISO2 country code
- Renamed columns
    - CountryCode -> country_iso
    - CountryName -> country

