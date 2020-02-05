from fizzbuzz import *
import unittest

class testFizzBUzz(unittest.TestCase): # On crée un objet avec "Class" . unittest.TestCase est une bibliotheque
    def test1(self):
        self.assertEqual(1, fizzBuzz(1))#sert a comparer deux choses : le resultat qu'on va lui donner et le resultat du code

    def test2(self):
        self.assertEqual(2, fizzBuzz(2))

    def test3(self):
        self.assertEqual('fizz', fizzBuzz(3))

    def test5(self):
        self.assertEqual('Buzz', fizzBuzz(5))

    def test15(self):
        self.assertEqual('fizzBuzz', fizzBuzz(15))

    def test20(self):
        self.assertEqual('Buzz', fizzBuzz(20))

    def test150(self):
        self.assertEqual('fizzBuzz', fizzBuzz(150))

    def test12(self):
        self.assertEqual('fizz', fizzBuzz(12))

    def test142(self):
        self.assertEqual(142, fizzBuzz(142))

unittest.main() # executer la fonction unittest
