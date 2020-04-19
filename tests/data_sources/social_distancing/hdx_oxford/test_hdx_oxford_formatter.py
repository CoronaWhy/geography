from datetime import datetime
from unittest import TestCase

import pandas as pd

from task_geo.data_sources.social_distancing.hdx_oxford.hdx_oxford_formatter import hdx_oxford_formatter
from task_geo.testing import check_dataset_format


class TestHdxApi(TestCase):

    def test_validate_formatter(self):
        """Validate datasource output.
        """
        # Setup
        start_date = datetime(2020, 1, 1).date().isoformat()
        end_date = datetime(2020, 2, 15).date().isoformat()
        countries = ["AW"]
        raw = pd.read_csv('tests/fixtures/hdx_oxfd_fixture.csv')

        # Run
        data = hdx_oxford_formatter(raw, start_date, end_date, countries)

        # Check.
        check_dataset_format(data)