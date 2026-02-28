# test_codesypher.py
"""
Tests for CodeSypher module.
"""

import unittest
from codesypher import CodeSypher

class TestCodeSypher(unittest.TestCase):
    """Test cases for CodeSypher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CodeSypher()
        self.assertIsInstance(instance, CodeSypher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CodeSypher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
