# coding: utf-8

from captcha.audio import AudioCaptcha


def test_audio_generate():
    captcha = AudioCaptcha()
    data = captcha.generate('1234')
    assert bytearray('RIFF') in data
