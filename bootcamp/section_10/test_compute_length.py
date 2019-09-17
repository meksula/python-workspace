import unittest                                 # importujemy naszą bibliotekę
from compute_length import compute_length       # importujemy funkcję, którą będziemy testować

# Teraz musimy utworzyć klasę testową, która musi dziedziczyć po klasie TestCase z unittest

class TestComputeLength(unittest.TestCase):

    # Poprawny test
    def test_length(self):
        value = 'Karol'
        length = compute_length(value)
        self.assertEqual(length, 5)

    # Błędny test demonstracyjny
    def test_length_invalid(self):
        value = 'Karol'
        length = compute_length(value)
        self.assertEqual(length, 6)

# Teraz musimy wywołać tą naszą klaskę i funkcję testującą

if __name__ == '__main__':
    unittest.main()
