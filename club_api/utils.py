# utlis.py
import os
from uuid import uuid4
from django.utils import timezone

def set_logo_img_path(instance, filename): # instance는 이미지 파일
    cls_name = instance.__class__.__name__.lower() # 모델 별로
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    return '/'.join([
        'pic_folder',
        ymd_path,
        filename
    ])


def set_background_img_path(instance, filename): # instance는 이미지 파일
    class_name = instance.__class__.__name__.lower() # 모델 별로
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    return '/'.join([
        'pic_folder',
        class_name,
        ymd_path,
        filename
    ])