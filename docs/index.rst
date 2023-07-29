:description: A Python captcha library that generates audio and image CAPTCHAs.

Captcha
========

.. rst-class:: lead

    A Python captcha library that generates audio and image CAPTCHAs.

----

Installation
------------

Installing captcha is simple with ``pip``::

    $ pip install captcha

Simple Guide
------------

Here is a simple guide on how to use :class:`AudioCaptcha` and :class:`ImageCaptcha`:

.. code-block:: python

    from captcha.audio import AudioCaptcha
    from captcha.image import ImageCaptcha

    audio = AudioCaptcha(voicedir='/path/to/voices')
    image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

    data = audio.generate('1234')
    audio.write('1234', 'out.wav')

    data = image.generate('1234')
    image.write('1234', 'out.png')


Next Steps
----------

.. toctree::
    :caption: Guide

    image
    audio
    api

.. toctree::
    :caption: Development

    contribute
    changelog
