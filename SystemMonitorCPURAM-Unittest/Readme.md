# System Monitor Unit Testing

This is a Python script for testing a system monitoring application that uses `psutil` and `tkinter`. The script includes two unit tests to check the CPU and RAM usage labels within the application.

## Requirements

To run the unit tests in this script, you will need the following:

1. Python 3.x installed on your system.
2. The `psutil` library, which can be installed using `pip`:

```
pip install psutil
```
## Running the Unit Tests

To run the unit tests, follow these steps:

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is located.

4. Run the following command to execute the unit tests:

```
python SystemMonitorCPURAM-Unittest.py
```
5. The tests will run, and the results will be displayed in the terminal.

## Unit Test Description

### `test_cpu_label`

This test checks if the CPU label in the application displays the CPU usage and if the usage is greater than or equal to 1%. It uses the `psutil` library to monitor the CPU usage.

### `test_ram_label`

This test checks if the RAM label in the application displays the RAM usage and if the usage is greater than or equal to 10%. It uses the `psutil` library to monitor the RAM usage.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
