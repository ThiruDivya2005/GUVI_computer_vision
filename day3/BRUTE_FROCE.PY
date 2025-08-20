import cv2
img1=cv2.imread('building.jpeg')
img2=cv2.imread('build.jpeg')
orb=cv2.ORB_create()
KP1,des1=orb.detectAndcompute(img1,None)