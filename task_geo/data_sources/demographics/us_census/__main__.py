"""
Main method

Description:
    - Runs us_census which gets the finalized DataFrame for US Census Data
    - Converts and exports to CSV
"""

import argparse
from task_geo.data_sources.demographics.us_census import us_census


def get_argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-o', '--output', required=True,
        help='Destination file to store the processed dataset.')

    return parser


def main():
    parser = get_argparser()
    args = parser.parse_args()

    dataset = us_census()
    dataset.to_csv(args.output, index=False, header=True)


if __name__ == '__main__':
    main()
