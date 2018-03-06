import cv2

def img2gray():
    # Load an color image in grayscale
    img = cv2.imread('download.jpg',0)
    cv2.imshow('image',img)
    
    #Save image in grayscale
    cv2.imwrite('gray.png',img)
    #Wait a key to kill the process
    cv2.waitKey(0)
    cv2.destroyAllWindows()
