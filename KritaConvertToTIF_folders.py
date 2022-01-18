import glob
import os
import string

for filename in glob.glob("*.kra"):
    os.makedirs(filename[:-4])
    os.system("krita " + filename + " --export --export-filename " + filename[:-4] + "/" + filename[:-4] + ".tif")    
    os.rename(filename, filename[:-4] + "/" + filename)
    print("KritaConvertToTIF_folders: Converted: " + filename)