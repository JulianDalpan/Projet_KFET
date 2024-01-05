import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from io import StringIO

# Importez vos fonctions depuis le fichier features.py
from features import add_new_items, getprice, addsales, get_total

class TestFeatures(unittest.TestCase):

    def test_add_new_items(self):
        with patch('features.database.addItems') as mock_addItems:
            add_new_items('item_name', 10, 20, 5.0)
            mock_addItems.assert_called_once_with('item_name', 10, 20, 5.0)

    def test_getprice(self):
        with patch('features.database.getPrice') as mock_getPrice:
            mock_getPrice.return_value = [{'price': 10.0}]
            result = getprice('item_name')
            self.assertEqual(result, 10.0)

    @patch('features.subbitems')
    @patch('features.database.addSales')
    def test_addsales(self, mock_addSales, mock_subbitems):
        with patch('features.getprice') as mock_getprice:
            mock_getprice.return_value = 5.0
            addsales('item_name', 2)
            mock_subbitems.assert_called_once_with('item_name', 2)
            mock_addSales.assert_called_once_with('item_name', 10.0, 2, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 1)

    def test_get_total(self):
        with patch('features.database.getItemSale') as mock_getItemSale:
            mock_getItemSale.return_value = [{'quantity': 2}, {'quantity': 3}]
            result = get_total('item_name')
            self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
