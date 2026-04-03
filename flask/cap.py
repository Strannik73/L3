from io import BytesIO
# from flask import Flask, Response
from captcha.image import ImageCaptcha

captcha = ImageCaptcha()
data: BytesIO = captcha.generate('ABCD')