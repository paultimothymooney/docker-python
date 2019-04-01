import unittest
import tika
from tika import parser

class TestTika(unittest.TestCase):
    def test_tika(self):
        image = '/input/tests/data/tikatest.jpg'
        tika.initVM()
        parsed = parser.from_file(image)

# below from /chrismattmann/tika-python/tika/tests/test_tika.py
#import unittest
#import tika.parser
#class CreateTest(unittest.TestCase):
#    #"test for file types"
#    def test_remote_pdf(self):
#        #'parse remote PDF'
#        self.assertTrue(tika.parser.from_file(filename='/input/tests/data/tikatest1.pdf'))
#    def test_remote_html(self):
#        #'parse remote HTML' 
##        self.assertTrue(tika.parser.from_file(filename='/input/tests/data/tikatest2.htm'))
# #   def test_remote_mp3(self):
#        #'parese remote mp3'
#        self.assertTrue(tika.parser.from_file(filename='/input/tests/data/tikatest3.mp3'))
#    def test_remote_jpg(self):
#        #'parse remote jpg'
#        self.assertTrue(tika.parser.from_file(filename='/input/tests/data/tikatest4.jpg'))#
#
#if __name__ == '__main__':
#    unittest.main()
