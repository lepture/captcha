# Captcha

A captcha library that generates audio and image CAPTCHAs.


[![GitHub Sponsor](https://badgen.net/badge/support/captcha/blue?icon=github)](https://github.com/sponsors/lepture)
[![Build Status](https://github.com/lepture/captcha/actions/workflows/test.yml/badge.svg)](https://github.com/lepture/captcha/actions)
[![PyPI](https://badgen.net/pypi/v/captcha)](https://pypi.org/project/captcha)
[![codecov](https://codecov.io/gh/lepture/captcha/branch/master/graph/badge.svg?token=xLjcXGMaeo)](https://codecov.io/gh/lepture/captcha)

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

## Useful Links

1. GitHub: https://github.com/lepture/captcha
2. Docs: https://captcha.lepture.com/

## Demo

Here are some demo results:

1. Image:

  ![Image](https://cloud.githubusercontent.com/assets/290496/5213632/95e68768-764b-11e4-862f-d95a8f776cdd.png)

2. Audio: [wav file](https://github.com/lepture/captcha/releases/download/v0.1-beta/out.wav)
