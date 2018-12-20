
# coding: utf-8

# In[12]:


import cv2
import glob, os, errno

#replace mydir with the directory that wanted
mydir ='C:\GRAYSCALE DATA'

for file in glob.iglob("C:\GRAYSCALE_DATA\*\*.JPG"):
    image = cv2.imread(file)
    
    #convert to greyscale
    gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
    #write to location with same destination
    cv2.imwrite(os.path.join(mydir,file), gray_image) 

