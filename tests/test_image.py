# coding: utf-8

from captcha.image import ImageCaptcha


def test_image_generate():
    captcha = ImageCaptcha()
    data = captcha.generate('1234')
    assert hasattr(data, 'read')
