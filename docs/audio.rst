:description: Learn how to generate audio CAPTCHA in Python.

Audio Captcha
=============

.. rst-class:: lead

    Unlock security with Audio CAPTCHA aastery.

----

.. module:: captcha.audio
    :noindex:

Usage
-----

Generating audio CAPTCHA with the :class:`AudioCaptcha`` class is remarkably simple.

.. code-block:: python

    from captcha.audio import AudioCaptcha

    captcha = AudioCaptcha()
    data: bytearray = captcha.generate('1234')

Here is an example of an audio captcha:

.. raw:: html

    <audio controls="controls">
      <source src="https://github.com/lepture/captcha/releases/download/v0.5.0/demo.wav" type="audio/wav">
    </audio>

Voice library
-------------

The ``AudioCaptcha`` module comes with built-in voice files for
numbers from 0 to 9. However, for enhanced security and customization,
it is highly recommended to use your own voice library. This section
will guide you on how to generate your own voice library using ``espeak``
and ``ffmpeg``.

.. code-block:: bash

  # Set the language code
  export ESLANG=en

  # Create a directory for the specified language code
  mkdir "$ESLANG"

  # Loop through each character (a-z, A-Z, 0-9) and create a directory for each
  for i in {a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9}; do
      mkdir "$ESLANG/$i"
      espeak -a 150 -s 100 -p 15 -v "$ESLANG" "$i" -w "$ESLANG/$i/orig_default.wav"
      ffmpeg -i "$ESLANG/$i/orig_default.wav" -ar 8000 -ac 1 -acodec pcm_u8 "$ESLANG/$i/default.wav"
      rm "$ESLANG/$i/orig_default.wav"
  done

Then use the voice library:

.. code-block:: python

    from captcha.audio import AudioCaptcha

    voice_dir = "path/to/en"  # we generated the wav files in "en" folder
    captcha = AudioCaptcha(voice_dir)

Web server
----------

In addition to generating and saving the voice files in a directory or
cloud storage like Amazon S3, you can also serve the Voice CAPTCHA audio
files on-the-fly.

Let's explore how to use the CAPTCHA library to dynamically serve audio
CAPTCHAs within a Flask application.

.. code-block:: python

    from io import BytesIO
    from flask import Flask, Response
    from captcha.audio import AudioCaptcha

    audio = AudioCaptcha()
    app = Flask(__name__)


    @app.route("/captcha")
    def captcha_view():
        # add your own logic to generate the code
        code = "1234"
        data = audio.generate(code)
        return Response(BytesIO(data), mimetype="audio/wav")
