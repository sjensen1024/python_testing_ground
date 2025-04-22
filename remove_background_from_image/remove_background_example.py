from rembg import remove 
from PIL import Image 
  
input_path =  'test_input.jpg' 
output_path = 'test_output.png' 
  
input = Image.open(input_path) 
output = remove(input) 
  
output.save(output_path) 