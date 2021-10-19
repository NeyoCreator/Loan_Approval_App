from pdf2image import convert_from_path

pdf_file = "first_page.pdf"
pages = convert_from_path(pdf_file, 500)

image_counter = 1

for page in pages:

    filename = "Retrieve/page_" _+str(image_counter) + ".jpg"

    # save the image of the page in the system
    page.save(filename, "JPEG")
    
    # increment the counter to update filename
    image_counter = image_counter + 1
