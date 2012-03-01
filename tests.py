import unittest
from PIL import Image
from thumbnailer import library as thumb
from thumbnailer.library.compat import StringIO

class ThumbnailerTestCase(unittest.TestCase):
    def assertDimensions(self, t):
        w, h = Image.open(t).size
        self.assertLessEqual(w, thumb.DEFAULT_WIDTH)
        self.assertLessEqual(h, thumb.DEFAULT_HEIGHT)

    def test_pdf(self):
        t = thumb.create('files/test.pdf')
        self.assertDimensions(t)

    def test_pdf_file(self):
        t = thumb.create(file('files/test.pdf'))
        self.assertDimensions(t)

    def test_pdf_stream(self):
        t = thumb.create(StringIO(file('files/test.pdf').read()), file_name='test.pdf')
        self.assertDimensions(t)

    def test_png(self):
        t = thumb.create('files/test.png')
        self.assertDimensions(t)

    def test_png_file(self):
        t = thumb.create(file('files/test.png'))
        self.assertDimensions(t)

    def test_png_stream(self):
        t = thumb.create(StringIO(file('files/test.png').read()), file_name='test.png')
        self.assertDimensions(t)

    def test_avi(self):
        t = thumb.create('files/test.avi')
        self.assertDimensions(t)

    def test_avi_file(self):
        t = thumb.create(file('files/test.avi'))
        self.assertDimensions(t)

    def test_avi_stream(self):
        t = thumb.create(StringIO(file('files/test.avi').read()), file_name='test.avi')
        self.assertDimensions(t)

    def test_odt(self):
        t = thumb.create('files/test.odt')
        self.assertDimensions(t)

    def test_odt_file(self):
        t = thumb.create(file('files/test.odt'))
        self.assertDimensions(t)

    def test_odt_stream(self):
        t = thumb.create(StringIO(file('files/test.odt').read()), file_name='test.odt')
        self.assertDimensions(t)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
