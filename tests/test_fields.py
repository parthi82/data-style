"""test all fields"""
import unittest
from tests.base import async_test
from bs4 import BeautifulSoup as q
from data import data


class TestBaseField(unittest.TestCase):
    """Testing BaseField"""
    def setUp(self):
        super(TestBaseField, self).setUp()
        self._field = data.BaseField(coerce=lambda x: "{}:{}".format(x, "coerce"))

    def test_get_value(self):
        """test get value should be inherited in base fields"""
        with self.assertRaises(NotImplementedError):
            self._field.get_value(None)

    def test_clean(self):
        """test for clean method in base fields"""
        value = self._field.clean("anyvalue")
        self.assertEqual(value, "anyvalue")

    def test_coerce(self):
        """test corect method in base fields"""
        value = self._field.coerce("coerce")
        self.assertEqual(value, "coerce:coerce")

class TestTextField(unittest.TestCase):
    """Testing TextField"""
    def setUp(self):
        super(TestTextField, self).setUp()
        self._html = q("<ul><li attr='big'>1</li><li attr2='small'>2</li></ul>")

    def test_get_value_for_noneselector(self):
        """testing the get value to be returning none"""
        field = data.TextField()
        self.assertIsNone(field.get_value(""))

    def test_get_value_for_bs4selector(self):
        """testing the get value if bs4 selector is given"""
        field = data.TextField(selector="li")
        self.assertEqual("1", field.get_value(self._html))

    def test_get_repeated_bs4selector(self):
        """testing the get value if repeated is enabled"""
        field = data.TextField(selector="li", repeated=True)
        self.assertListEqual(["1", "2"], field.get_value(self._html))

class TestAttributeValueField(unittest.TestCase):
    """Testing Attribute field"""
    def setUp(self):
        super(TestAttributeValueField, self).setUp()
        self._html = q("<ul><li attr='big'>1</li><li attr2='small'>2</li></ul>")

    def test_get_value_for_noneattr(self):
        """testing the get value if no attr is given"""
        field = data.AttributeValueField()
        self.assertIsNone(field.get_value(None))

    def test_get_value_for_domattr(self):
        """testing the value if attr is given"""
        field = data.AttributeValueField(attr="attr", selector="li")
        self.assertEqual("big", field.get_value(self._html))

    def test_get_value_for_domrepeated(self):
        """testing the value if repated property is enabled"""
        field = data.AttributeValueField(attr="attr", selector="li", repeated=True)
        self.assertListEqual(["big", None], field.get_value(self._html))
