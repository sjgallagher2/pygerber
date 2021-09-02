# -*- coding: utf-8 -*-
from __future__ import annotations

from pathlib import Path
from unittest import TestCase, main

from PIL import Image
from pygerber.parser.pillow.parser import ImageSizeNullError, ParserWithPillow

RENDERED_PATH = Path("./tests/gerber/rendered")
GERBER_PATH = Path("./tests/gerber")


class TestPillowParser(TestCase):

    SOURCE_0 = """
            %FSLAX26Y26*%
            %MOMM*%
            %ADD100C,1.5*%
            D100*
            X0Y0D03*
            M02*
            """

    def test_parser_double_none(self):
        self.assertRaises(RuntimeError, lambda: ParserWithPillow(None, None))

    def test_parser_string(self):
        parser = ParserWithPillow(None, self.SOURCE_0)
        self.assertEqual(parser.tokenizer.bbox.width(), 1.5)
        parser.render()
        image = parser.get_image()
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save(RENDERED_PATH/"SOURCE_0.png")
        # self.assertTrue(
        #     are_images_similar(Image.open(RENDERED_PATH / "SOURCE_0.png"), image, 0, 0)
        # )

    def test_parser_double_render(self):
        parser = ParserWithPillow(None, self.SOURCE_0)
        self.assertRaises(RuntimeError, lambda: parser.get_image())
        parser.render()
        self.assertRaises(RuntimeError, lambda: parser.render())
        parser.save(".\\tests\\test_parser\\test_render.png", "png")
        parser.save(".\\tests\\test_parser\\test_render.png")

    def test_parser_null_size_image(self):
        parser = ParserWithPillow(None, "M02*")
        self.assertRaises(ImageSizeNullError, parser.render)

    def test_render_file_and_save(self):
        ParserWithPillow.render_file_and_save(GERBER_PATH / "s0.grb", RENDERED_PATH / "s0_0.png")

    def test_parser_file_0(self):
        image = ParserWithPillow.render_file(GERBER_PATH / "s0.grb", dpi=1600)
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save("./tests/gerber/rendered/s0.png")
        # self.assertTrue(
        #     are_images_similar(Image.open(RENDERED_PATH / "s0.png"), image, 0, 0)
        # )

    def test_parser_file_1(self):
        image = ParserWithPillow.render_file(GERBER_PATH / "s1.grb")
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save("./tests/gerber/rendered/s1.png")
        # self.assertTrue(
        #     are_images_similar(Image.open(RENDERED_PATH / "s1.png"), image, 0, 0)
        # )

    def test_parser_file_2(self):
        image = ParserWithPillow.render_file(GERBER_PATH / "s2.grb")
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save("./tests/gerber/rendered/s2.png")
        # self.assertTrue(
        #     are_images_similar(Image.open(RENDERED_PATH / "s2.png"), image, 0, 0)
        # )

    def test_parser_file_3(self):
        image = ParserWithPillow.render_file(GERBER_PATH / "s3.grb")
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save("./tests/gerber/rendered/s3.png")
        # self.assertTrue(
        #    are_images_similar(Image.open(RENDERED_PATH / "s3.png"), image, 0, 0)
        # )

    def test_parser_file_4(self):
        image = ParserWithPillow.render_file(GERBER_PATH / "s4.grb")
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save("./tests/gerber/rendered/s4.png")
        # self.assertTrue(
        #     are_images_similar(Image.open(RENDERED_PATH / "s4.png"), image, 0, 0)
        # )

    def test_parser_file_5(self):
        image = ParserWithPillow.render_file(GERBER_PATH / "s5.grb", dpi=600, image_padding=50)
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save("./tests/gerber/rendered/s5.png")
        # self.assertTrue(
        #     are_images_similar(Image.open(RENDERED_PATH / "s5.png"), image, 0, 0)
        # )

    def test_parser_file_6(self):
        image = ParserWithPillow.render_file(GERBER_PATH / "s6.grb", dpi=2600)
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save("./tests/gerber/rendered/s6.png")
        # self.assertTrue(
        #    are_images_similar(Image.open(RENDERED_PATH / "s6.png"), image, 0, 0)
        # )

    def test_parser_file_7(self):
        image = ParserWithPillow.render_file(GERBER_PATH / "s7.grb", dpi=2600)
        # to manually validate output uncomment this:
        # image.show()
        # to create new comparison image uncomment this:
        # image.save("./tests/gerber/rendered/s7.png")
        # self.assertTrue(
        #    are_images_similar(Image.open(RENDERED_PATH / "s7.png"), image, 0, 0)
        # )


if __name__ == "__main__":
    main()
