"""
Calculator functions
"""
import click
import pandas as pd


def get_df_shape(some_input):
    """
    Function to get the shape of my dataframe
    """
    rows, cols = some_input.shape
    return rows, cols


def load_dataset(input_file):
    """Load dataset and throw exceptions"""

    try:
        df = pd.read_csv(input_file, sep=",", index_col=0)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {input_file}") from exc
    except ValueError as ve:
        raise ValueError(f"Error parsing the csv file: {input_file}") from ve

    return df


@click.command(short_help="Script to perform my data analysis steps")
@click.option("-i", "--input_file", required=True)
def main(input_file):
    """Main function to call others for data analysis"""
    df = load_dataset(input_file)

    rows, col = get_df_shape(df)
    print(rows, col)


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
