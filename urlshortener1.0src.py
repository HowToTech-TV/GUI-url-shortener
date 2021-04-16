import tkinter.messagebox as msg

class NoBitlyError(Exception):
  pass
def NoTokenError():
  msg.showerror("Error", "Please enter a authorization token!")
import tkinter as tk
import os
import webbrowser
try:
  import bitly_api
except:
  raise NoBitlyError("Bit.ly is not installed.")
else:
  import bitly_api


def mainwindow():
  root = tk.Tk()
  root.title("URL Shortener 1.0(GitHub Version)")
  root.geometry("500x300")
  root.resizable(0,0)
  label = tk.Label(root, text = "URL Shortener", bg = "Yellow", font = ("Open Sans", 30))
  label2 = tk.Label(root, text = "Please enter bitly assess token:").pack()
  BITLY_ACCESS_TOKEN = tk.StringVar()
  BITLY_ACCESS_TOKEN.set("924dd0636ccba000c0c1c9153327e8ec6112fa34")
  tokenentry = tk.Entry(root, textvariable=BITLY_ACCESS_TOKEN).pack()
  label3 = tk.Label(root, text = "Please enter the link:").pack()
  link = tk.StringVar()
  link.set("http://www.google.com")
  entry2 = tk.Entry(root, textvariable=link).pack()
  label4 = tk.Label(root, text="Output:")
  txt = tk.Label(root)
  def short():
    if BITLY_ACCESS_TOKEN == "":
      NoTokenError()
    else:
      link1 = link.get()
      connection = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN.get())
      shortlink = connection.shorten(link1)
      txt.config(text = shortlink["url"])
  

    
  button = tk.Button(root, text = "Authorize", command=short).pack()
  label4.pack()
  txt.pack()
  
  label6 = tk.Label(root, text = "\n \n Version 1.0").pack()
  def view():
    webbrowser.open("https://github.com/HowToTech-TV/GUI-url-shortener")
  tk.Button(root, text = "view repo online", command=view).pack()
  
  
  
  
  root.mainloop()
mainwindow()