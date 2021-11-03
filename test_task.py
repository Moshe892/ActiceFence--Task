from unittest import TestCase
from WorkProject.task import *


class Test(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.state = None

    # testing if the correct keys are successfully removed from
    # the list, and the list now empty
    def test_3_correct_keys(self):
        enterKey('abce1234','bill3333','john9876')
        self.assertEqual(len(list1),0)

    # testing if the correct keys are successfully removed from
    # the list, and the list now contain 1 item only (the other correct key)
    def test_2_correct_keys(self):
        enterKey('abce1234','bad key','john9876')
        self.assertEqual(len(list1),1)

    # testing if the correct key has successfully removed from
    # the list, and the list now contain 2 items (the other 2 correct keys)
    def test_1_correct_key(self):
            enterKey('abce1234', 'bad key', 'wrong key')
            self.assertEqual(len(list1), 2)

    # testing if the the list still contain 3 items, which
    # means correct key has been entered
    def test_0_correct_keys(self):
        enterKey('table8', 'bad key', 'wrong key')
        self.assertEqual(len(list1), 3)

    # testing if the vault sealed after 5 tries, by checking
    # if an exit code has been activated (happens only when the vault sealed)
    def test_vault_sealed_after_5_wrong_tries(self):
        enterKey('1', 'Y', 'Z')
        enterKey('2', 'Y', 'Z')
        enterKey('3', 'Y', 'Z')
        enterKey('4', 'Y', 'Z')
        with self.assertRaises(SystemExit):
            enterKey('4', 'Y', 'Z')

    # testing if the getState function returnd "closed"
    # while there were no tries to open the vault
    def test_getState_0_tries(self):
        self.assertEqual(getState(),"Closed")

    # testing if the getState function returnd "Unlock in progress"
    # while there were 1 to 4 tries to open the vault
    def test_getState_in_progress(self):
        enterKey('1', 'Y', 'Z')
        enterKey('2', 'R', 'B')
        self.assertEqual(getState(),"Unlock in progress")

    # testing if the getState function returnd "open" after
    # the user entered 2 or 3 correct keys in less than 5 tries
    def test_getState_vault_open(self):
        enterKey('abce1234','bill3333','john9876')
        self.assertEqual(getState(),"Open")

    # testing a full process of trying open the vault,
    # using both functions and 2 incorecct tries
    def test_end_to_end(self):
        self.assertEqual(getState(),"Closed")
        enterKey('1', 'Y', 'Z')
        self.assertEqual(getState(),"Unlock in progress")
        enterKey('1', 'Y', 'Z')
        self.assertEqual(getState(),"Unlock in progress")
        enterKey('abce1234','bill3333','john9876')
        self.assertEqual(getState(),"Open")







