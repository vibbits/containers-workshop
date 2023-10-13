# Code to provide functions to create and annotate an html report file for script results

# start_html
def start_html():
  f = open('report.html','w')
  message = "<html><head></head><body>"
  f.write(message)
  f.close()

def html_para(text):
  f = open('report.html','a')
  message = "<p>" + text + "</p>"
  f.write(message)
  f.close()
  
def html_img(text, img_path):
  f = open('report.html','a')
  message =  "<p>" + text + "</p>" + "<p><img src=\"" + img_path + "\"></p>"
  f.write(message)
  f.close()
  
def end_html():
  f = open('report.html','a')
  message = "</body></html>"
  f.write(message)
  f.close()
