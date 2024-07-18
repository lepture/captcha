# coding: utf-8

import os
from captcha.image import ImageCaptcha

ROOT = os.path.abspath(os.path.dirname(__file__))


def test_image_generate():
    captcha = ImageCaptcha()
    data = captcha.generate('1234')
    assert hasattr(data, 'read')


def test_save_image():
    captcha = ImageCaptcha()
    filepath = os.path.join(ROOT, 'demo.png')
    captcha.write('1234', filepath)
    assert os.path.isfile(filepath)
