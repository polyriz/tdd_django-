from django.test import TestCase

class SmokeTest(testcase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)