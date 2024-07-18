# coding: utf-8

import os
from captcha.audio import AudioCaptcha

ROOT = os.path.abspath(os.path.dirname(__file__))


def test_audio_generate():
    captcha = AudioCaptcha()
    data = captcha.generate('1234')
    assert isinstance(data, bytearray)
    assert bytearray(b'RIFF') in data


def test_audio_random():
    captcha = AudioCaptcha()
    data = captcha.random(4)
    assert len(data) == 4


def test_save_audio():
    captcha = AudioCaptcha()
    filepath = os.path.join(ROOT, 'demo.wav')
    captcha.write('1234', filepath)
    assert os.path.isfile(filepath)
