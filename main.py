import os
import img2pdf
from natsort import natsorted, ns

subfolderStructureCheck = ""
deleteCheck = ""
inputPath = ""
outputPath = ""
filename = ""

imageList = []

while inputPath == "":
    inputPath = input("Enter the input path: ")
while outputPath == "":
    outputPath = input("Enter the output path: ")
while filename == "":
    filename = input("Enter the name of the pdf file that will be created: ")
while subfolderStructureCheck not in ["y", "Y", "n", "N"]:
    subfolderStructureCheck = input("Does the input path have subfolders? (y/n): ")
    if subfolderStructureCheck in ["y", "Y", "n", "N"]:
        break
    else:
        print("Not a valid option.") 
while deleteCheck not in ["y", "Y", "n", "N"]:
    deleteCheck = input("Delete files after completion? (y/n): ")
    if deleteCheck in ["y", "Y", "n", "N"]:
        break
    else:
        print("Not a valid option.") 

if "\\" in inputPath:
    inputPath = inputPath.replace("\\", "/")
if inputPath[-1] != "/":
    inputPath += "/"

if "\\" in outputPath:
    outputPath = outputPath.replace("\\", "/")
if outputPath[-1] != "/":
    outputPath += "/"

if "\"" in inputPath:
    inputPath = inputPath.replace("\"", "")
if "\"" in outputPath:
    outputPath = outputPath.replace("\"", "")

if filename.endswith(".pdf") == False:
    filename += ".pdf"

subfolders = [(f.path + "/") for f in os.scandir(inputPath) if f.is_dir()]
subfolders = natsorted(subfolders, alg=ns.IGNORECASE)  # For some reason, Python seeks dirs with ASCII order and not natural order (1,2...10,11...)
subfolderCheck = subfolderStructureCheck.lower()

if subfolderCheck == "y":
    for folder in subfolders:
        imageList += [(folder + image) for image in os.listdir(folder) if (image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".png"))]
    with open(inputPath + filename, "wb") as file:
        file.write(img2pdf.convert(imageList))

elif subfolderCheck == "n":
    imageList = [(inputPath + image) for image in os.listdir(inputPath) if (image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".png"))]
    imageList = natsorted(imageList, alg=ns.IGNORECASE)
    with open(outputPath + filename, "wb") as file:
        file.write(img2pdf.convert(imageList))