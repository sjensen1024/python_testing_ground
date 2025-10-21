import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from rembg import remove
import time

input_path =  'test_input.jpg' 
output_path = 'test_output.png' 

img = mpimg.imread(input_path)

plt.imshow(img)
plt.show()
