import unittest

def is_primo(value):
    # value % div -> resto
    div = 2
    
    if value <= 1:
        return False
    
    while div * div <= value:
        if value % div == 0:
            return False
        div += 1
    return True
        
    
    
class TestPrimos(unittest.TestCase):
    def test_11negativo(self):
        result = is_primo(-11)
        self.assertEqual(result,False)
        
    def test_7negativo(self):
        result = is_primo(-7)
        self.assertEqual(result,False)
        
    def test_3negativo(self):
        result = is_primo(-3)
        self.assertEqual(result,False)
        
    def test_2negativo(self):
        result = is_primo(-2)
        self.assertEqual(result,False)
    
    
    def test_0(self):
        result = is_primo(0)
        self.assertEqual(result,False)
        
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result,False)

        
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result,True)
    
    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result,True)
        
    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result,False)
        
    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result,True)
 
    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result,False)
    
    def test_1112(self):
        result = is_primo(1112)
        self.assertEqual(result,False)
    
    def test_28374(self):
        result = is_primo(28374)
        self.assertEqual(result,False)
    
unittest.main()
    
    
    
    