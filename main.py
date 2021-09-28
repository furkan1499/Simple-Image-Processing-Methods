import cv2

print("---start blending images---")
# take two images
img1 = cv2.imread('heisenberg.jpg')
img2 = cv2.imread('heisenberg2.jpg')

# convert from BGR to RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# to blend images we must equalize their size
img1 = cv2.resize(img1, (600, 300))
img2 = cv2.resize(img2, (600, 300))

# we give the mixing ratios of the images
blended = cv2.addWeighted(src1=img1, alpha=0.8, src2=img2, beta=0.2, gamma=0)

# we write image
cv2.imwrite('blending.jpg', blended)

print("---end blending images---")

print("---start sobel operator---")
# Sobel Operator
# You can search Sobel Operator on Google. https://en.wikipedia.org/wiki/Sobel_operator

img = cv2.imread('heisenberg.jpg', 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

cv2.imwrite("sobelx_heisenberg.jpg", sobelx)
cv2.imwrite("sobely_heisenberg.jpg", sobely)

print("---end sobel operator---")

print("---start blur images---")

# firstly read the image
img = cv2.imread('heisenberg.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# blurred image
blurred_img = cv2.blur(img, ksize=(20, 20))
cv2.imwrite("blurred_img.jpg", blurred_img)

print("---end blur images---")
