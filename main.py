from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280, height=90)

capcha_text = 'awsdrgyjilmhbfcsz'
data = image.generate(capcha_text)
image.write(capcha_text, 'Captcha.png')