import sys
sys.path.append('/home/user/my_package')

import unittest
from normalized_data import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_data(self):
        response = self.app.get('/api/all')
        self.assertEqual(response.status_code, 200)

    def test_get_song_by_title(self):
        response = self.app.get('/api/song?title=3AM')
        self.assertEqual(response.status_code, 200)
    
    def test_rate_song(self):
        response = self.app.post('/api/rate', data={'id': '5vYA1mW9g2Coh1HUFUSmlb', 'rating': '5'})
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
