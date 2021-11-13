from pdf2image import convert_from_path

# Store Pdf with_convert_from_path function 
image = convert_from_path('second_page.pdf')

for i in range(len(image)):
   
      # Save pages as images in the pdf
    image[i].save('page'+ str(i) +'.jpg', 'JPEG')