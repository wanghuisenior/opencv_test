#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName: getConfig1.py
 @Author: 王辉/Administrator
 @Email: wanghui@zih718.com
 @Date: 2020/6/3 8:23
 @Description:从摄像头框选获取感兴趣区域，并保存最后一帧图片作为依据，同时创建坐标配置文件
"""
import cv2

drawing = False
ix, iy = -1, -1
mx, my = -1, -1


def draw_rectangle(event, x, y, flags, param):
	global ix, iy, drawing, mx, my
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
		mx, my = x, y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:  # (ix, iy), (x, y)  (left, top), (right, bottom)
			cv2.rectangle(frame, (ix, iy), (x, y), (0, 255, 0), 2)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		mx, my = x, y


# 采集自带摄像头
cap = cv2.VideoCapture(0)

print("FPS:", cap.get(cv2.CAP_PROP_FPS))
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 设置窗口全屏显示
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback("image", draw_rectangle)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cap_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('cap display:', cap_width, '*', cap_height)
while cap.isOpened():
	ok, frame = cap.read()
	if not ok:
		break
	cv2.waitKey(1)
	cv2.rectangle(frame, (ix, iy), (mx, my), (0, 255, 0), 2)
	cv2.putText(frame, "press enter to save config file", (20, 40), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 0, 255), 2)
	resize_w = int(cap_width / 4)  # 显示出来窗口的高度，按照cap 高度等比缩放
	resize_h = int(cap_height / 4)  # 显示出来窗口的宽度，按照cap 宽度等比缩放
	# cv2.resizeWindow("image", resize_w, resize_h)  # 改变显示窗口的大小,不改变实际尺寸
	cv2.imshow('image', frame)
	c = cv2.waitKey(10)
	if c & 0xFF == ord('q'):
		break
	elif c & 0xFF == 13:
		cv2.imwrite("config.jpg", frame)
		with open("coordinate.conf", "w", encoding="utf-8") as f:
			f.write("[left,top] = %s\r[right,bottom] = %s" % (str(ix) + "," + str(iy), str(mx) + "," + str(my)))
			f.close()
		print("success")
cap.release()
cv2.destroyAllWindows()
