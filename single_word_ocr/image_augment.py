#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author: wu.zheng midday.me

from imgaug import augmenters as iaa

seq = iaa.SomeOf((1, 4), [
  iaa.Salt(p=(0.2, 0.4)),
  iaa.GaussianBlur(sigma=(0, 1.0)) ,
  iaa.CoarseDropout(p=(0.02, 0.1), size_percent=(0.2, 0.6)),
  iaa.JpegCompression(compression=(50,80)),
])


def augment_image(image):
  image = 255 - image
  image_aug = seq(image=image)
  image_aug = 255 - image_aug
  return image_aug 
    

