# #!/usr/bin/env python
# # encoding: utf-8
# import unittest
#
# class ExampleTest(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def test_abc(self):
#         assert(True)
#
# if __name__ == "__main__":
#     unittest.main()


from nose.tools import assert_equal
from nose.tools import with_setup
import  unittest

def test_math_add():
    result=5+6
    assert_equal(10,result,"Match ")

test_math_add()
