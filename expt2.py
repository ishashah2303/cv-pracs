import cv2
import numpy as np
img=cv2.imread("flower.jpg")


height,width = img.shape[0:2]
quarter_height , quarter_width = height/4 , width /4
T1=np.float32([[1,0,quarter_width],[0,1,quarter_height]])
T2=np.float32([[1,0,quarter_width],[0,1,-quarter_height]])
T3=np.float32([[1,0,-quarter_width],[0,1,-quarter_height]])
T4=np.float32([[1,0,-quarter_width],[0,1,quarter_height]])
img_translation = cv2.warpAffine(img,T1,(width,height))
#img_translation = cv2.warpAffine(img,T2,(width,height))
# img_translation = cv2.warpAffine(img,T3,(width,height))
# img_translation = cv2.warpAffine(img,T4,(width,height))
cv2.imshow("Originalimage", img) 
#cv2.imshow('Translation', img_translation) 

# M = np.float32([[1,  0, 0],
#                 [0, -1, height],
#                 [0,  0, 1]])
# reflected_img = cv2.warpPerspective(img, M,
#                                    (int(width),
#                                     int(height)))

M = np.float32([[1,  0, 0],
                [0, -1, height],
                [0,  0, 1]])
reflected_img = cv2.warpPerspective(img, M,
                                   (int(width),
                                    int(height)))


#cv2.imshow('reflection.jpg', reflected_img)

MS = np.float32([[-1,  0, width],
                [0, 1, 0],
                [0,  0, 1]])
reflected_img = cv2.warpPerspective(img, MS,
                                   (int(width),
                                    int(height)))


#cv2.imshow('reflection.jpg', reflected_img)




img_rotation = cv2.warpAffine(img,cv2.getRotationMatrix2D((width/2, height/2),50, 0.6),(width, height))
#cv2.imshow('rotation_out.jpg', img_rotation)


MR = np.float32([[0.2,  0, 0],
                [0, 0.2, 0],
                [0,  0, 1]])
scaled = cv2.warpPerspective(img, MR,
                                   (int(width/5),
                                    int(height/5)))
#cv2.imshow('Shrinking.jpg', scaled)


MR1 = np.float32([[2,  0, 0],
                [0, 2, 0],
                [0,  0, 1]])
scaled1 = cv2.warpPerspective(img, MR1,
                                   (int(width*2),
                                    int(height*2)))
#cv2.imshow('ENLARGING.jpg', scaled1)


cropped_image = img[0:450, 0:800]
#cv2.imshow('Cropped Image',cropped_image)

M1 = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img1 = cv2.warpPerspective(img, M1, (int(width*1.5), int(height*1.5)))
#cv2.imshow('Shearing x img', sheared_img1)


M2 = np.float32([[1, 0, 0], [0.5, 1, 0], [0,0, 1]])
sheared_img2= cv2.warpPerspective(img, M2, (int(width*1.5), int(height*1.5)))
#cv2.imshow('Shearing y img', sheared_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()