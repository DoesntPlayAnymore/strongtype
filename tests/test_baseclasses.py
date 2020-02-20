"""
Tests for strongtype.baseclasses
"""

from strongtype import StronglyTyped
from dataclasses import dataclass
import unittest


@dataclass
class MockStr(StronglyTyped):
    s: str


@dataclass(frozen=True)
class MockStrFrozen(StronglyTyped):
    s: str



class TestStronglyTyped(unittest.TestCase):
    """
    Tests for strongtype.baseclasses.StronglyTyped
    """
        
    def test_typed(self):
        self.assertRaises(
                TypeError,
                MockStr, 1,
       )
    
    def test_equality(self):
        a = MockStr('s')
        
        self.assertEqual(a.s, 's')
        self.assertEqual(a.s, a.s)
        self.assertEqual(a, a)

        b = MockStr('s')
        
        self.assertEqual(a, b)
        self.assertFalse(a is b)
    
    def test_hash(self):
        a = MockStrFrozen('s')
        b = MockStrFrozen('s')
        
        self.assertEqual(hash(a), hash(b))
        
        unique = {a, b}
        self.assertEqual(len(unique), 1)
        
        
    
if __name__=='__main__':
    unittest.main()