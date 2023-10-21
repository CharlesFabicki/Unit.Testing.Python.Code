import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
import json
import matplotlib.pyplot as plt


class TestPandasDataFrame(unittest.TestCase):

    def setUp(self):
        # Set up a sample DataFrame for testing
        self.df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    def test_dataframe_creation(self):
        # Test if the DataFrame is created correctly and has the expected shape, columns, and values.
        self.assertEqual(self.df.shape, (3, 2))
        self.assertListEqual(list(self.df.columns), ['A', 'B'])

        # Sort the values in both DataFrames for comparison
        expected_values = [1, 2, 3, 4, 5, 6]
        actual_values = sorted(self.df.values.flatten())
        self.assertListEqual(actual_values, expected_values)

    def test_dataframe_manipulation(self):
        # Test if DataFrame manipulation (adding a column) produces the expected result.
        df2 = self.df.copy()
        df2['C'] = [7, 8, 9]
        assert_frame_equal(df2, pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}))

    def test_dataframe_operations(self):
        # Test if DataFrame operations (filtering rows) produce the expected result.
        df2 = self.df[self.df['A'] > 1]

        # Reset the index of both DataFrames for comparison
        df2.reset_index(drop=True, inplace=True)

        expected_result = pd.DataFrame({'A': [2, 3], 'B': [5, 6]})
        assert_frame_equal(df2, expected_result)

    def test_dataframe_io(self):
        # Test if DataFrame input/output to a CSV file works correctly and the loaded DataFrame is the same as the original.
        self.df.to_csv('test.csv', index=False)
        df2 = pd.read_csv('test.csv')
        assert_frame_equal(df2, self.df)


class TestCarHandling(unittest.TestCase):

    def test_json_write_and_read_car(self):
        # Create a JSON object representing a car (Audi A4)
        car_data = {
            'make': 'Audi',
            'model': 'A4',
            'year': 2022,
            'color': 'Silver',
            'engine': {
                'type': 'Turbocharged',
                'horsepower': 248
            }
        }

        # Define a file name for writing and reading
        file_name = 'car_data.json'

        # Write the car JSON data to a file
        with open(file_name, 'w') as file:
            json.dump(car_data, file)

        # Read the car JSON data from the file
        with open(file_name, 'r') as file:
            loaded_car_data = json.load(file)

        # Check if the loaded car JSON data matches the original data
        self.assertEqual(car_data, loaded_car_data)


class TestPandasPlotting(unittest.TestCase):

    def test_dataframe_plot_bar_chart(self):
        # Create a sample DataFrame representing product sales
        data = {
            'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
            'Sales': [120, 300, 150, 200]
        }
        df = pd.DataFrame(data)

        # Create a bar chart from the DataFrame
        ax = df.plot(x='Product', y='Sales', kind='bar', title='Product Sales')

        # Save the plot as an image file (e.g., PNG)
        image_filename = 'product_sales_chart.png'
        plt.savefig(image_filename)

        # Verify that the plot file was saved successfully
        self.assertTrue(plt.gcf())

    def tearDown(self):
        # Clean up by closing the plot
        plt.close()


if __name__ == '__main__':
    unittest.main()
