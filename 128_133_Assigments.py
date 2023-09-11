# First Assigment
# --------------------------------------------------------------------------------------------------------------------------
# Test 1 => 10 Is Found In This List [5, 7, 8, 10]
# Test 2 => The Type Of 10 Is Int
# Test 3 => Number 100 Return True
# Test 4 => Empty List [] Return False
# Test 5 => 100 Is Larger Than Or Equal 90

# Write Your Class Here
import unittest
class TestCases(unittest.TestCase):
    def test_case_one(self):
        self.assertIn(10,[5, 7, 8, 10],msg="10 Is Found In This List [5, 7, 8, 10]")
    
    def test_case_two(self):
        self.assertIsInstance(10,int,msg="The Type Of 10 Is Int")

    def test_case_three(self):
        self.assertTrue(100,msg="Number 100 Return True")
    
    def test_case_four(self):
        self.assertFalse([],msg="Empty List [] Return False")
    
    def test_case_five(self):
        self.assertGreaterEqual(100,90,msg="100 Is Larger Than Or Equal 90")
        
if __name__ == "__main__":
    unittest.main()
# ----------------------------------------------------------------------------------------------------------------------------

print("#" * 70)

# ----------------------------------------------------------------------------------------------------------------------------
# Second Assigment
# ----------------------------------------------------------------------------------------------------------------------------
# Examples
# asdf-asdf-asdfgh
# 12as-as12-12as34
import string
import random
all_char = string.digits + string.ascii_letters
serial_list = []
def generate_serial(length):
    
    while length > 0:
        serial_list.append(all_char[random.randint(0,len(all_char)-1)])
        length-=1
    
    serial1 = "".join(serial_list)
    print(serial1[0:4],"-",serial1[4:8],"-",serial1[8:])


generate_serial(14)


emp_s = []
for i in range(14):
    emp_s.append(all_char[random.randint(0,len(all_char)-1)])
    serial = "".join(emp_s)

print(serial[0:4],"-",serial[4:8],"-",serial[8:])


