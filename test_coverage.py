
class TestCoverage:
    """
    Class that adds coverage test to other unit test classes.

    Unit test class must derive from it. Also test_class var
    must be added to unit test class that holds tested class.

    e.g.
    class TestMyClass(unittest.TestCase, TestCoverage):
        test_class = MyCLass
        ...

    It checks if all methods in tested class that do not start
    with _ have an equivalent (same name with test_ prefix)
    in unit test class.
    """

    def test_checkIfAllMethodsAreCovered(self):
        test_members = list(self.__class__.__dict__.keys())
        class_members = list(self.test_class.__dict__.keys())
        check_for = ['test_' + x for x in class_members if not x.startswith('_')]
        are_covered = all(test in test_members for test in check_for)
        if not are_covered:
            diff = list(set(check_for)-set(test_members))
            print(self.test_class.__name__, "functions that are not covered: ", diff)
            self.assertTrue(False)
