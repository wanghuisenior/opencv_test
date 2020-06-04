#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName: test.py
 @Author: 王辉/Administrator
 @Email: wanghui@zih718.com
 @Date: 2020/6/3 9:35
 @Description:
"""
import face_recognition
image = face_recognition.load_image_file("1.png")
face_locations = face_recognition.face_locations(image)