def count_vowels(stroka):
    glasn = set('aeiouAEIOU')
    count = 0
    for i in stroka:
        if i in glasn:
            count += 1        
    return count

import unittest

class TestCountVowels(unittest.TestCase):
    
    def test_a(self):
        self.assertEqual(count_vowels("Natalia"), 4)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("test"), 0)#проверка для просчета отрицательного случая, если заменить на 1, проверка пройдет успешно
        

if __name__ == '__main__':
    unittest.main()
