import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper_string(self):
        self.assertEqual("darek".upper(), "DAREK")

    def test_lower_string(self):
        self.assertEqual("DAREK".lower(),"darek")

    def test_tile_string(self):
        self.assertEqual("darek".title(),"Darek")

    def test_is_upper(self):
        self.assertTrue("DAREK".isupper())

    def test_is_not_upper(self):
        self.assertFalse("Darek".isupper())

    def test_split(self):
        expected ={"ala":1, "ma":2, "kota":1,"i":1, "psa":1}
        string ="ala ma kota i ma psa"
        given={}
        for x in string.split(" "):
            if x not in given:
                given[x] = 1
            elif x in given:
                given[x] += 1 
        self.assertDictEqual(given,expected)
    
    def test_len_greater(self):
        name1="Darek"
        name2="Sebastian"
        self.assertGreater(len(name2),len(name1))
        name3="Mikolaj"
        self.assertGreater(len(name2),len(name3))

    def test_len_greater2(self):
        name2="Sebastian"
        name3="Mikolaj"
        self.assertGreater(len(name2),len(name3))
    
    def test_len_less(self):
        name1="Darek"
        name2="Sebastian"
        self.assertLess(len(name1),len(name2))
    
    def test_len_less2(self):
        name2="Sebastian"
        name3="Mikolaj"
        self.assertLess(len(name3),len(name2))




if __name__ == '__main__':
    unittest.main()