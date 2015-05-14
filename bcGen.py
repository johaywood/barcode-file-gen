from hubarcode.datamatrix import DataMatrixEncoder
import sys, os
import openpyxl
from PIL import Image

encoder = DataMatrixEncoder("HuDoRa")
encoder.save( "test.png" )


subjects = []

class Subject:
  
  def __init__(self, subj_id, subj_num, barcode):
    self.subj_id = subj_id
    self.subj_num = subj_num
    self.barcode = barcode
    self.barcode_color = self.get_barcode_color(barcode)
    self.barcode_path = self.get_barcode_path(barcode)
    self.barcode_img = self.get_barcode_image(barcode)
    subjects.append(self)
    
  def get_barcode_color(barcode):
    color = ''
    num = int(barcode[:-4])
    if num < 2000:
      color = "Yellow"
      color_rgba = (255, 255, 0, 255)
    if num < 4000:
      color = "Cream"
      color_rgba = (255, 229, 204, 255)
    if num < 6000:
      color = "Orange"
      color_rgba = (255, 128, 0, 255)
    if num < 8000:
      color = "Blue"
      color_rgba = (0, 0, 255, 255)
    if num < 10000:
      color = "Green"
      color_rgba = (0, 225, 0, 255)
    return color, color_rgba
  
  def get_barcode_path(self, barcode):
    cwd = os.getcwd()
    path = cwd + '/' + barcode + '.png'
    return path
  
  def get_barcode_image(self, barcode):
    barcode_img = DataMatrixEncoder(barcode)
    barcode_img.save("%s.png" % barcode)
    return barcode_img
  
  def add_colored_border(barcode):