from pygerber.mathclasses import BoundingBox
from pygerber.meta.meta import Interpolation, Polarity
from pygerber.tokens.token import Token
from unittest import TestCase, main
from pygerber.tokenizer import Tokenizer
from .test_meta.test_aperture import ApertureCollector, ApertureSetTest


class TokenizerTest(TestCase):

    SOURCE_0 = """
            %FSLAX26Y26*%
            %MOMM*%
            %ADD100C,1.5*%
            D100*
            X0Y0D03*
            M02*
            """

    def test_tokenize_string(self):
        tokenizer = Tokenizer(ApertureSetTest.get_dummy_apertureSet())
        tokenizer.tokenize_string(self.SOURCE_0)
        self.assertEqual(tokenizer.token_stack_size, 6)
        self.assertEqual(tokenizer.bbox.as_tuple(), (-0.75, 0.75, 0.75, -0.75))

    def test_tokenize_file_0(self):
        tokenizer = Tokenizer(ApertureSetTest.get_dummy_apertureSet())
        tokenizer.tokenize_file("./tests/gerber/s0.grb")
        self.assertEqual(tokenizer.token_stack_size, 17)
        self.assertEqual(tokenizer.meta.polarity, Polarity.DARK)
        self.assertTrue(10 in tokenizer.meta.apertures.keys())
        self.assertEqual(tokenizer.meta.interpolation, Interpolation.Linear)
        self.assertEqual(tokenizer.bbox.as_tuple(), (-0.005, 5.005, 11.005, -0.005))

    def test_tokenize_file_1(self):
        tokenizer = Tokenizer(ApertureSetTest.get_dummy_apertureSet())
        tokenizer.tokenize_file("./tests/gerber/s1.grb")
        self.assertEqual(tokenizer.token_stack_size, 47)
        self.assertEqual(
            tokenizer.bbox.as_tuple(), (-0.0635, 25.3492, 55.062119999999986, -0.0635)
        )

    def test_tokenize_file_2(self):
        tokenizer = Tokenizer(ApertureSetTest.get_dummy_apertureSet())
        tokenizer.tokenize_file("./tests/gerber/s2.grb")
        self.assertEqual(tokenizer.token_stack_size, 116)
        self.assertEqual(
            tokenizer.bbox.as_tuple(), (-0.0635, 25.3492, 55.062119999999986, -0.0635)
        )

    def test_render(self):
        tokenizer = Tokenizer(ApertureSetTest.get_dummy_apertureSet())
        tokenizer.tokenize_string(self.SOURCE_0)
        self.assertRaises(ApertureCollector.CalledFlash, tokenizer.render)


if __name__ == "__main__":
    main()
