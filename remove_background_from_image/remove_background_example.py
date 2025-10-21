from rembg import remove 
from PIL import Image 
import time
  
input_path =  'test_input.jpg' 
output_path = 'test_output.png' 
  
input = Image.open(input_path) 
input.show()
time.sleep(3)


output = remove(input) 
output.save(output_path)

new_image = Image.open(output_path)
new_image.show()
time.sleep(3)
