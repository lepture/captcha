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

.. note::

    The default voice library only includes numbers from 0 to 9.

Voice library
-------------

We can build our customized voice library with the help of ``espeak`` and ``ffmpeg``:

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

Web server
----------
