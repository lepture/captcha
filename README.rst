Captcha
=======

A captcha library that generates audio and image CAPTCHAs.

.. image:: https://img.shields.io/badge/donate-lepture-ff69b4.svg
   :target: https://lepture.com/donate
   :alt: Donate lepture
.. image:: https://img.shields.io/badge/I0-patreon-f96854.svg
   :target: https://patreon.com/lepture
   :alt: Become a Patreon
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

Audio and Image CAPTCHAs are in separated modules:

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

Voices
------

We can build our customized voice library with the help of espeak and ffmpeg::

   export ESLANG=en

   mkdir $ESLANG

   for i in {a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9}; do mkdir $ESLANG/$i; espeak -a 150 -s 100 -p 15 -v$ESLANG $i -w $ESLANG/$i/orig_default.wav; ffmpeg -i $ESLANG/$i/orig_default.wav -ar 8000 -ac 1 -acodec pcm_u8 $ESLANG/$i/default.wav; rm $ESLANG/$i/orig_default.wav; done


Contribution
------------

We need voice wav files. The voice wav file should be in 8-bit, please keep it
as small as possible. Name your voice file as::

    {{language}}-{{character}}-{{username}}.wav
    # example: zh-1-lepture.wav

TODO: we need a place to upload voice files.
