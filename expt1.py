import cv2
img=cv2.imread("flower.jpg")
#cv2.imshow('Image',img)
print("Image shape is" ,img.shape)
print("Image size is" ,img.size)
print("Image datatype is" ,img.dtype)

b,g,r = cv2.split(img)
#cv2.imshow('b',b)
#cv2.imshow('g',g)
#cv2.imshow('r',r)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray Image',gray_img)

cropped_image = img[0:450, 0:800]
#cv2.imshow('Cropped Image',cropped_image)

img1=cv2.imread("img1.jpg")
#cv2.imshow('Image 1',img1)
img2=cv2.imread("img2.jpg")
#cv2.imshow('Image 2',img2)
final_img=cv2.addWeighted(img1,0.5,img2,0.4,1)
#cv2.imshow('ADD',final_img)

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")
final_img2=cv2.subtract(img1,img2)
#cv2.imshow('SUBTRACT',final_img2)

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")
final_img3=cv2.multiply(img1,img2)
#cv2.imshow('MULTIPLY',final_img3)

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")
final_img4=cv2.divide(img1,img2)
#cv2.imshow('DIVIDE',final_img4)

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")
img_1=cv2.bitwise_and(img1,img2)
#cv2.imshow('Bitwise AND',img_1)

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")
img_2=cv2.bitwise_not(img1,img2)
#cv2.imshow('Bitwise NOT',img_2)

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")
img_3=cv2.bitwise_or(img1,img2)
#cv2.imshow('Bitwise OR',img_3)

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")
img_4=cv2.bitwise_xor(img1,img2)
cv2.imshow('Bitwise XOR',img_4)


cv2.waitKey(0)
cv2.destroyAllWindows()
