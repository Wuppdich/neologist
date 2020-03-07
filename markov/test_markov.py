from unittest import TestCase

import neologist


class MyTestCase(TestCase):
    def test_add_occurence(self):
        self.test_dict = {}
        neologist.add_occurence(self.test_dict, "0", "0")
        self.assertEqual(self.test_dict, {"0": {"0": 1}})
        neologist.add_occurence(self.test_dict, "0", "0")
        self.assertEqual(self.test_dict, {"0": {"0": 2}})
        neologist.add_occurence(self.test_dict, "1", "1")
        self.assertEqual(self.test_dict, {"0": {"0": 2},
                                          "1": {"1": 1}})

