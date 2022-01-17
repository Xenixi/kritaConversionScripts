from distutils import filelist
import glob
import os
import string
import uuid
tempID = str(uuid.uuid4())
os.makedirs("Finalized_" + tempID)
for filename in glob.glob("*.kra"):
   
    os.system("krita " + filename + " --export --export-filename " + "Finalized_" + tempID + "/" + filename[:-4] + ".bmp")    
    os.rename(filename,"Finalized_" + tempID + "/" + filename)
    print("KritaConvertToPSD: Converted: " + filename)