# Python Unit Testing and Data Handling

This README provides an overview of the Python unit testing and data handling code, which includes tests for Pandas DataFrames, JSON handling for car data, and creating a bar chart from a Pandas DataFrame using Matplotlib.

## Python Unit Testing with `unittest`

The code contains a set of unit tests written using Python's built-in `unittest` framework. These tests ensure that various aspects of data handling and manipulation are working correctly. 

### `TestPandasDataFrame` Class

This class tests the creation, manipulation, operations, and input/output of Pandas DataFrames.

1. `test_dataframe_creation`: Checks if a sample DataFrame is created correctly with the expected shape, columns, and values.

2. `test_dataframe_manipulation`: Tests whether adding a new column to a DataFrame produces the expected result.

3. `test_dataframe_operations`: Verifies that DataFrame operations, such as filtering rows, produce the expected result.

4. `test_dataframe_io`: Ensures that DataFrame input/output to a CSV file works correctly and the loaded DataFrame matches the original one.

### `TestCarHandling` Class

This class tests writing and reading car data in JSON format.

1. `test_json_write_and_read_car`: Creates a JSON object representing a car and tests writing it to a file and then reading it back. It checks whether the loaded JSON data matches the original data.

### `TestPandasPlotting` Class

This class tests creating a bar chart from a Pandas DataFrame using Matplotlib.

1. `test_dataframe_plot_bar_chart`: Generates a bar chart from a sample DataFrame and saves it as an image file (e.g., PNG). It then verifies that the plot file was saved successfully.

## Running the Tests

To run the unit tests, execute the script using Python:

```bash
python Pandas_Unittest.py
```

## Dependencies

The code relies on several libraries:

- `unittest`: The built-in Python testing framework.
- `pandas`: Used for working with DataFrames.
- `json`: Used for reading and writing JSON data.
- `matplotlib`: Used for creating and saving plots.

Ensure that these libraries are installed in your Python environment before running the tests.

## License

This code is released under the MIT License.
