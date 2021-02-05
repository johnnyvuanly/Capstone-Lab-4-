import camelCase # Name of file
from unittest import TestCase

class TestCamelCase(TestCase):
    
    def test_camelcase_sentance(self):
        
        self.assertEqual('helloWorld', camelCase.camelcase('Hello World'))
        self.assertEqual('minnesotaVikings', camelCase.camelcase('   MInnesota    vIKINGS   '))
        self.assertEqual('', camelCase.camelcase(''))
        self.assertEqual('mVP', camelCase.camelcase(' M v  p'))
        self.assertEqual('!@#$%', camelCase.camelcase('   ! @  # $    %   '))
        

# Test program with -> python -m unittest test_camelCase.py
