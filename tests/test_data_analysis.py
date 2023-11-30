"""
Tests for the data analysis part
"""

from unittest import TestCase
import pandas as pd
from src.data_analysis import get_df_shape, load_dataset


class TestDataAnalysis(TestCase):
    """Add test for my data analysis"""

    def setUp(self):
        self.file = "./dataset/train.csv"
        self.data = pd.read_csv(self.file, sep=",", index_col=0)

    def test_columns_input_data(self):
        """Check the shape from the input data"""
        _, columns = get_df_shape(self.data)
        self.assertEqual(columns, 20)

    def test_rows_input_data(self):
        """Check the shape from the input data"""
        rows, _ = get_df_shape(self.data)
        self.assertEqual(rows, 114000)

    def test_error_dataset(self):
        """Check if dataset is not a dataframe"""

        with self.assertRaises(Exception) as context:
            load_dataset("some_file.csv")
        self.assertTrue("File not found" in str(context.exception))
