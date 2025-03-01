# Captcha

A captcha library that generates audio and image CAPTCHAs.


[![GitHub Sponsor](https://badgen.net/badge/support/captcha/blue?icon=github)](https://github.com/sponsors/lepture)
[![Build Status](https://github.com/lepture/captcha/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/lepture/captcha/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/lepture/captcha/branch/main/graph/badge.svg?token=xLjcXGMaeo)](https://codecov.io/gh/lepture/captcha)

## Install

Install captcha with pip:

```
pip install captcha
```

## Features

1. Audio CAPTCHAs
2. Image CAPTCHAs

## Usage

Audio and Image CAPTCHAs are in separated modules:

```python
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

audio = AudioCaptcha(voicedir='/path/to/voices')
image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

data = audio.generate('1234')
audio.write('1234', 'out.wav')

data = image.generate('1234')
image.write('1234', 'out.png')
```

This is the APIs for your daily works. We do have built-in voice data and font
data. But it is suggested that you use your own voice and font data.

### Use Custom Colors

In order to change colors you have to specify your desired color as a tuple of Red, Green and Blue value.
Example:- `(255, 255, 0)` for yellow color, (255, 0, 0)` for red color.

```python
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

data = image.generate('1234')
image.write('1234', 'out.png', bg_color=(255, 255, 0), fg_color=(255, 0, 0)) # red text in yellow background
```


## Useful Links

1. GitHub: https://github.com/lepture/captcha
2. Docs: https://captcha.lepture.com/

## Demo

Here are some demo results:

![Image Captcha](https://github.com/lepture/captcha/releases/download/v0.5.0/demo.png)

[Audio Captcha](https://github.com/lepture/captcha/releases/download/v0.5.0/demo.wav)
