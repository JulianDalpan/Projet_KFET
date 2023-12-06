import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from io import StringIO

# Importez vos fonctions depuis le fichier features.py
from features import additems, subbitems, add_new_items, getquantity, getprice, addsales, generate_sale_pdf, get_total

class TestFeatures(unittest.TestCase):

    @patch('features.database.getStock')
    def test_additems(self, mock_getquantity):
        mock_getquantity.return_value = 5
        with patch('features.database.addItems') as mock_addItems:
            additems('item_name', 3)
            mock_addItems.assert_called_once_with('item_name', getprice('item_name'), 8, 'your_purchased_price')


    # Modifiez votre test_subbitems pour ressembler à ceci
    @patch('features.database.getStock')
    def test_subbitems(self, mock_getStock):
        mock_getStock.return_value = [{'quantity': 5}]  # Assurez-vous que le mock retourne une liste non vide
        with patch('features.database.addItems') as mock_addItems:
            subbitems('item_name', 3)
            mock_addItems.assert_called_once_with('item_name', getprice('item_name'), 2, 'your_purchased_price')



    def test_add_new_items(self):
        with patch('features.database.addItems') as mock_addItems:
            add_new_items('item_name', 10, 20, 5.0)
            mock_addItems.assert_called_once_with('item_name', 10, 20, 5.0)

    def test_getquantity(self):
        with patch('features.database.getStock') as mock_getStock:
            mock_getStock.return_value = [{'quantity': 15}]
            result = getquantity('item_name')
            self.assertEqual(result, 15)

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

    def test_generate_sale_pdf(self):
        with patch('features.database.getpurchased_price') as mock_getpurchased_price:
            with patch('features.get_total') as mock_get_total:
                with patch('features.database.getAllItem') as mock_getAllItem:
                    mock_getpurchased_price.return_value = [{'purchasedprice': 5.0}]
                    mock_get_total.return_value = 3
                    mock_getAllItem.return_value = ['item1', 'item2']
                    
                    with patch('features.database.getItemSale') as mock_getItemSale:
                        mock_getItemSale.return_value = [{'quantity': 2}, {'quantity': 1}]
                        
                        # Redirect stdout to capture print statements
                        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                            generate_sale_pdf()
                            # You can now assert on the printed output if needed

    def test_get_total(self):
        with patch('features.database.getItemSale') as mock_getItemSale:
            mock_getItemSale.return_value = [{'quantity': 2}, {'quantity': 3}]
            result = get_total('item_name')
            self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
