Captcha
=======

A captcha library that generates audio and image CAPTCHAs.

Features
--------

1. Audio CAPTCHAs
2. Image CAPTCHAs


Installation
------------

Install captcha with pip::

    $ pip install captcha

Usage
-----

Audio and Image CAPTCHAs are in separated modules:

.. code-block:: python

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

Useful Links
------------

1. GitHub: https://github.com/lepture/captcha
2. Docs: https://captcha.lepture.com/


License
-------

Licensed under BSD. Please see LICENSE for licensing details.
