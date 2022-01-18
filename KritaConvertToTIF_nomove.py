import glob
import os
import string
import uuid


for filename in glob.glob("*.kra"):
   
    os.system("krita " + filename + " --export --export-filename " + filename[:-4] + ".tif")    
   
    print("KritaConvertToTIF_nomove: Converted: " + filename)