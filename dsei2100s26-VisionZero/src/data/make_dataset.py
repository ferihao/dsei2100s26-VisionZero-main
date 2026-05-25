# -*- coding: utf-8 -*-
import logging
import click
import pandas as pd
import numpy as np
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)

COLUMNS_TO_DROP = [
    'vehicle_type_code_3', 'vehicle_type_code_4', 'vehicle_type_code_5',
    'contributing_factor_vehicle_3', 'contributing_factor_vehicle_4',
    'contributing_factor_vehicle_5',
    'off_street_name',
]

RENAME_MAP = {
    'number_of_persons_injured': 'num_injured',
    'number_of_persons_killed':  'num_killed',
    'contributing_factor_vehicle_1': 'factor_vehicle_1',
    'contributing_factor_vehicle_2': 'factor_vehicle_2',
    'vehicle_type_code_1': 'vehicle_type_1',
    'vehicle_type_code_2': 'vehicle_type_2',
}

CATEGORICAL_COLS = [
    'borough', 'zip_code', 'factor_vehicle_1', 'factor_vehicle_2',
    'vehicle_type_1', 'vehicle_type_2', 'on_street_name', 'cross_street_name',
]


def assign_severity(df):
    conditions = [
        df['num_killed'] > 0,
        (df['num_injured'] > 0) & (df['num_killed'] == 0),
    ]
    return np.select(conditions, [2, 1], default=0)


def make_time_features(df):
    dates = pd.to_datetime(df['crash_date'], errors='coerce')
    hours = pd.to_datetime(df['crash_time'], format='%H:%M', errors='coerce').dt.hour

    df['crash_date'] = dates       
    df['year'] = dates.dt.year
    df['month'] = dates.dt.month
    df['day_of_week'] = dates.dt.day_name()
    df['hour'] = hours
    df['is_weekend'] = dates.dt.dayofweek.isin([5, 6]).astype(int)
    df['is_rush_hour'] = hours.isin(list(range(7, 10)) + list(range(16, 20))).astype(int)

    # Dropping rows where date or time could not be parsed
    df = df.dropna(subset=['crash_date', 'hour'])
    return df


@click.command()
@click.argument('input_filepath',  type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """Clean raw collision data."""

    logger.info(f'Loading raw data from: {input_filepath}')
    df = pd.read_csv(input_filepath, low_memory=False)
    logger.info(f'Original shape: {df.shape[0]:,} rows x {df.shape[1]} columns')

    # 1. Normalizing column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # 2. Renaming key columns
    df = df.rename(columns=RENAME_MAP)

    # 3. Severity target
    df['severity'] = assign_severity(df)

    # 4. Time features
    df = make_time_features(df)

    # 5. Drop high-missingness columns (ignore if already absent)
    df = df.drop(columns=[c for c in COLUMNS_TO_DROP if c in df.columns])

    # 6. Treat invalid coordinates as missing
    df.loc[df['latitude'] == 0, 'latitude'] = np.nan
    df.loc[df['longitude'] == 0, 'longitude'] = np.nan

    # 7. Clean and fill categorical columns
    # zip_code is stored as float (e.g. 11207.0) — convert to clean string first
    if 'zip_code' in df.columns:
        df['zip_code'] = df['zip_code'].apply(
            lambda x: str(int(x)) if pd.notna(x) and x != 0 else np.nan
        )

    for col in CATEGORICAL_COLS:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper()
            df[col] = df[col].replace({'NAN': 'UNKNOWN', '': 'UNKNOWN'})

    # 8. Save
    Path(output_filepath).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_filepath, index=False)
    logger.info(f'Final shape:    {df.shape[0]:,} rows x {df.shape[1]} columns')
    logger.info(f'Saved cleaned dataset to: {output_filepath}')


if __name__ == '__main__':
    project_dir = Path(__file__).resolve().parents[2]
    load_dotenv(find_dotenv())
    main()
