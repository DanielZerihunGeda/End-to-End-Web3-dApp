import unittest
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class TestNFTCreationEndpoint(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:4001'
        self.create_nft_url = f'{self.base_url}/Create_NFT'
        
        # Set up test data
        self.test_params = {
            'first_name': 'Daniel',
            'last_name': 'Zerihun',
            'training_program': 'Blockchain',
            'date_of_completion': '2022-01-13',
            'duration_of_training': '3 months',
            'issuing_organization': '10 Academy',
            'serial_no_of_certificate': '123456789'
        }

    def test_create_nft_success(self):
        response = requests.post(self.create_nft_url, data=self.test_params)
        self.assertEqual(response.status_code, 200)
        self.assertIn('transaction_id', response.json())

    def test_create_nft_duplicate_asset(self):
        # Call the endpoint twice with the same parameters
        response1 = requests.post(self.create_nft_url, data=self.test_params)
        response2 = requests.post(self.create_nft_url, data=self.test_params)

        # Both responses should have an error since the asset already exists
        self.assertEqual(response1.status_code, 200)
        self.assertIn('transaction_id', response1.json())
        self.assertEqual(response2.status_code, 400)
        self.assertIn('error', response2.json())

if __name__ == '__main__':
    unittest.main()
