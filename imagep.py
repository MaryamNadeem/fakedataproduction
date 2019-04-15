
import cv2
import numpy as np
from random import *
import glob
def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def whipeout(image):
    for i in range(3):
        choice=randint(0,1)
        if(choice==0): #whipes out randomly in the image
            x= randint(1, 3)
            if(x==1):
                rectangle_x1 = randint(1,image.shape[0] )
                rectangle_y1 = randint(1, image.shape[1])

                rectangle_x2 = randint(rectangle_x1, rectangle_x1+500)
                rectangle_y2 = randint(rectangle_y1, rectangle_y1+500)
                cv2.rectangle(image, (rectangle_x1, rectangle_y1), (rectangle_x2, rectangle_y2), (255, 255, 255), -1)

            if(x==2):
                x1 = randint(1, image.shape[0])
                y1 = randint(1, image.shape[1])
                radius=randint(1, 50)
                cv2.circle(image, (x1, y1), radius, (255, 255, 255), -1)
            if(x==3):
                x1 = randint(1, image.shape[0])#centre point
                x2 = randint(1, image.shape[1])
                size1 = randint(1, 100)#size
                size2 = randint(1, 100)
                angle1=randint(1, 360)
                angle2=randint(1, 360)

                cv2.ellipse(image, (x1, x2), (size1, size2), 0, angle1, angle2, (255, 255, 255), -1)
        if(choice==1): #whipes out from the centre of the image
            middle0 = int(image.shape[0] / 2 + 200)
            middle1 = int(image.shape[1] / 2 - 250)
            x = randint(1, 3)
            if (x == 1):
                rectangle_x1 = randint(middle0-20, middle0+20)
                rectangle_y1 = randint(middle1-20, middle1+20)

                rectangle_x2 = randint(rectangle_x1, rectangle_x1 + 50)
                rectangle_y2 = randint(rectangle_y1, rectangle_y1 + 50)
                cv2.rectangle(image, (rectangle_x1, rectangle_y1), (rectangle_x2, rectangle_y2), (255, 255, 255), -1)

            if (x == 2):
                x1 = randint(middle0-20, middle0+20)
                y1 = randint(middle1-20, middle1+20)
                radius = randint(1, 50)
                cv2.circle(image, (x1, y1), radius, (255, 255, 255), -1)
            if (x == 3):
                x1 = randint(middle0-20, middle0+20)  # centre point
                x2 = randint(middle1-20, middle1+20)
                size1 = randint(1, 50)  # size
                size2 = randint(1, 50)
                angle1 = randint(1, 360)
                angle2 = randint(1, 360)

                cv2.ellipse(image, (x1, x2), (size1, size2), 0, angle1, angle2, (255, 255, 255), -1)

    return image


images = [cv2.imread(file) for file in glob.glob("images\*.jpg")]
index=0
for img in images:

    for no_of_hair in range (40):
        x = randint(1, 2000)
        y=randint(1, 2000)
        size1 = randint(1,600)
        size2 = randint(1,600)
        cv2.ellipse(img, (x, y), (size1, size2), 0, 160, 260,0, 1)
    #img=whipeout(img)
    noise_intensity=uniform(0,0.05)
    output=sp_noise(img, noise_intensity)
    #cv2.imshow('imageEEE',output) #uncomment to display picture
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


    cv2.imwrite("result\image"+str(index)+".jpg",output)
    index=index+1

