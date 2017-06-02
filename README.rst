Captcha
=======

A captcha library that generates audio and image CAPTCHAs.

.. image:: https://img.shields.io/badge/donate-lepture-green.svg
   :target: https://typlog.com/donate?amount=10&reason=lepture%2Fcaptcha
   :alt: Donate lepture
.. image:: https://travis-ci.org/lepture/captcha.svg?branch=master
   :target: https://travis-ci.org/lepture/captcha
.. image:: https://ci.appveyor.com/api/projects/status/amm21f13lx4wuura?svg=true
   :target: https://ci.appveyor.com/project/lepture/captcha
.. image:: https://coveralls.io/repos/lepture/captcha/badge.svg?branch=master
   :target: https://coveralls.io/r/lepture/captcha

Features
--------

1. Audio CAPTCHAs `DEMO <https://github.com/lepture/captcha/releases/download/v0.1-beta/out.wav>`_
2. Image CAPTCHAs

.. image:: https://cloud.githubusercontent.com/assets/290496/5213632/95e68768-764b-11e4-862f-d95a8f776cdd.png


Installation
------------

Install captcha with pip::

    $ pip install captcha

Usage
-----

Audio and Image CAPTCHAs are in seprated modules:

.. code:: python

    from captcha.audio import AudioCaptcha
    from captcha.image import ImageCaptcha

    audio = AudioCaptcha(voicedir='/path/to/voices')
    image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

    data = audio.generate('1234')
    audio.write('1234', 'out.wav')

    data = image.generate('1234')
    image.write('1234', 'out.png')

This is the APIs for your daily works. We do have built-in voice data and font
data. But it is suggested that you use your own voice and font data.


Contribution
------------

We need voice wav files. The voice wav file should be in 8-bit, please keep it
as small as possible. Name your voice file as::

    {{language}}-{{character}}-{{username}}.wav
    # exmaple: zh-1-lepture.wav

TODO: we need a place to upload voice files.
