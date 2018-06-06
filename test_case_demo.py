import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("I Will Run Once Before Every Test")

    def test_MethodA(self):
        print("Runnig Method A")

    def test_MethodB(self):
        print("Runnig Method B")

    def tearDown(self):
        print("I will run after every test")


if __name__ == '__main__':
    unittest.main(verbosity=2)
