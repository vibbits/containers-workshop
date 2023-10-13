# ELIXIR-TrP-CodeRep-Example-Python
The repository for developing the python script that is to be available to all the CodeRep courses and then modified to demonstrate that particular courses key concepts.     

Mark took MCebisis' first jupyter notebook version, exported it as a .py and then crafted a version consisting of (codereppyt1.py, plots.py & models.py along with the csv file in datasets folder) to try and create a version that would work well for the Containers course and possibly be of use for the Software Testing group also.

codereppy_batch.py is a full "headless" (non-interactive) implementation and codreppy_min_batch.py is a truncated minimal version of that.
Both need the plots.py & models.py files along with the datasets folder and the html_gen.py file (covered below).      
It takes its inspiration from FastQC in that it produces graphics & text that can be inserted into an HTML doc that can be viewer in the users browser of choice or further processed e.g. with pandoc to create a PDF file.

html_gen.py contains functions to be incorporated into codereppy1.py (and the batch derivatives) to create html entries for its text and graphics outputs.   
html_test.py (along with test_image.png file) was used to test the functions in html_gen.py.

It is envisaged that the CodeRep Documentation and testing group will use the models.py and plots.py for their needs to demonstrate their course concepts and the codereppy.py can be e.g. loaded into a Jupyter notebook or Rmarkdown document and source the two external files.
This should allow the Literate programming course to apply Markdown to the script.    
