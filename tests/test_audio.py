# coding: utf-8

from captcha.audio import AudioCaptcha


def test_audio_generate():
    captcha = AudioCaptcha()
    data = captcha.generate('1234')
    assert isinstance(data, bytearray)
    assert bytearray(b'RIFF') in data


def test_audio_random():
    captcha = AudioCaptcha()
    data = captcha.random(4)
    assert len(data) == 4
