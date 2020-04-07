import io

import pandas as pd
import requests


def south_korea_patients_connector(*args, **kwargs):
    """Retrieves data from south_korea_patients.

    Arguments:
        url(string): Dataset url
    Returns:
        pandas.DataFrame
    """
    csv = requests.get(kwargs['url']).content
    return pd.read_csv(io.StringIO(csv.decode('utf-8')))


def south_korea_patients_formatter(df):
    """Formats data retrieved from south_korea_patients.

    Arguments:
      df(pandas.DataFrame):

    Returns:
      pandas.DataFrame
    """
    cols_ordered = [
        'country', 'state', 'province', 'confirmed_date',
        'released_date', 'deceased_date', 'exposure_start',
        'exposure_end', 'global_id', 'birth_year',
        'local_id', 'sex', 'disease',
        'group', 'infection_reason', 'infection_order',
        'infected_by', 'contact_number'
    ]
    df = df.reindex(columns=cols_ordered)
    df['confirmed_date'] = pd.to_datetime(df.confirmed_date)
    df['released_date'] = pd.to_datetime(df.released_date)
    df['deceased_date'] = pd.to_datetime(df.deceased_date)
    df['exposure_start'] = pd.to_datetime(df.exposure_start)
    df['exposure_end'] = pd.to_datetime(df.exposure_end)
    return df


def south_korea_patients(*args, **kwargs):
    """Data Source for south_korea_patients.

    Arguments:
        url(string): Dataset url

    Returns:
        pandas.DataFrame
    """
    data = south_korea_patients_connector(*args, **kwargs)
    return south_korea_patients_formatter(data)
