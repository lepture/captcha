Image Captcha
=============

.. rst-class:: lead

    Unleash captivating security with image CAPTCHA mastery.

----

.. module:: captcha.image
    :noindex:

Usage
-----

Generating image CAPTCHA with the :class:`ImageCaptcha` class is incredibly straightforward.


.. code-block:: python

    from io import BytesIO
    from captcha.image import ImageCaptcha

    captcha = ImageCaptcha()
    data: BytesIO = captcha.generate('ABCD')

Fonts
-----

Web server
----------
