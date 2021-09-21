import cv2

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
blended = cv2.addWeighted(src1=img1, alpha=0.85, src2=img2, beta=0.15, gamma=0)

# we write image
cv2.imwrite('blending.jpg', blended)
