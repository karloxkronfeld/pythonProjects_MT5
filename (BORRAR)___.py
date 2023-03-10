from rembg import remove
from PIL import Image
input_path="C:\Users\Personal\OneDrive\Pictures\imi.jpg"
output_path= "out.png"
entrada=Image.open((input_path))
output= remove(entrada)
output.save(output_path)