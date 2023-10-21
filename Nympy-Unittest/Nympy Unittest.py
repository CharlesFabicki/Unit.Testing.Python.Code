import numpy as np
import unittest


class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        # Initialize the array variable with a NumPy array
        self.array = np.array([1, 2, 3, 4, 5])

    def test_sum_of_elements(self):
        # Test the sum of elements function
        result = np.sum(self.array)
        self.assertEqual(result, 15)

    def test_mean(self):
        # Test the mean function
        result = np.mean(self.array)
        self.assertEqual(result, 3)

    def test_max_value(self):
        # Test the maximum value function
        result = np.max(self.array)
        self.assertEqual(result, 5)

    def test_index_of_max_value(self):
        # Test the index of maximum value function
        result = np.argmax(self.array)
        self.assertEqual(result, 4)

    def test_sort_ascending(self):
        # Test the ascending sort function
        result = np.sort(self.array)
        self.assertListEqual(result.tolist(), [1, 2, 3, 4, 5])

    def test_reverse_sort_descending(self):
        # Test the descending sort function
        result = np.sort(self.array)[::-1]
        self.assertListEqual(result.tolist(), [5, 4, 3, 2, 1])

    def test_std_dev(self):
        # Test the standard deviation function
        result = np.std(self.array)
        self.assertAlmostEqual(result, 1.41421356, places=6)

    def test_median(self):
        # Test the median function
        result = np.median(self.array)
        self.assertEqual(result, 3)

    def test_min_value(self):
        # Test the minimum value function
        result = np.min(self.array)
        self.assertEqual(result, 1)

    def test_index_of_min_value(self):
        # Test the index of minimum value function
        result = np.argmin(self.array)
        self.assertEqual(result, 0)

    def test_product_of_elements(self):
        # Test the product of elements function
        result = np.prod(self.array)
        self.assertEqual(result, 120)

    def test_cumulative_sum(self):
        # Test the cumulative sum function
        result = np.cumsum(self.array)
        self.assertListEqual(result.tolist(), [1, 3, 6, 10, 15])

    def test_unique_values(self):
        # Test the unique values function
        array_with_duplicates = np.array([1, 2, 3, 2, 1])
        result = np.unique(array_with_duplicates)
        self.assertListEqual(result.tolist(), [1, 2, 3])

    def test_elementwise_addition(self):
        # Test the elementwise addition function
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result = np.add(array1, array2)
        self.assertListEqual(result.tolist(), [5, 7, 9])

    def test_elementwise_subtraction(self):
        # Test the elementwise subtraction function
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result = np.subtract(array1, array2)
        self.assertListEqual(result.tolist(), [-3, -3, -3])

    def test_elementwise_multiplication(self):
        # Test the elementwise multiplication function
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result = np.multiply(array1, array2)
        self.assertListEqual(result.tolist(), [4, 10, 18])

    def test_elementwise_division(self):
        # Test the elementwise division function
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result = np.divide(array1, array2)
        self.assertListEqual(result.tolist(), [0.25, 0.4, 0.5])

    def test_matrix_multiplication(self):
        # Test the matrix multiplication function
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[5, 6], [7, 8]])
        result = np.matmul(matrix1, matrix2)
        self.assertListEqual(result.tolist(), [[19, 22], [43, 50]])

    def test_transpose(self):
        # Test the transpose function
        matrix = np.array([[1, 2], [3, 4]])
        result = np.transpose(matrix)
        self.assertListEqual(result.tolist(), [[1, 3], [2, 4]])

    def test_reshape(self):
        # Test the reshape function
        array = np.array([1, 2, 3, 4, 5, 6])
        result = np.reshape(array, (2, 3))
        self.assertListEqual(result.tolist(), [[1, 2, 3], [4, 5, 6]])

    def test_concatenate(self):
        # Test the concatenate function
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result = np.concatenate((array1, array2))
        self.assertListEqual(result.tolist(), [1, 2, 3, 4, 5, 6])

    def test_cross_product(self):
        # Test the cross product function
        array1 = np.array([1, 2, 3])
        array2 = np.array([4, 5, 6])
        result = np.cross(array1, array2)
        self.assertListEqual(result.tolist(), [-3, 6, -3])


if __name__ == "__main__":
    unittest.main()
