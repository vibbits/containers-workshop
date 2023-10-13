import html_gen as hg

# Script to test functions in html_gen.py
# https://github.com/mfernandes61 2023

# create html file header
hg.start_html()

# Add a text paragraph to html file
my_text = "Hello wild & wacky Internet denizens. This is just some test code."
hg.html_para(my_text)

# Create a anchor link to an existing graphics file
img_text = " An example plot<br>"
img_name = "test_image.png"
hg.html_img(img_text, img_name)

# Finish up the web page
hg.end_html()

print("That's all folks!")
