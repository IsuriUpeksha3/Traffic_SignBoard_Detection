import os

image_files = []
os.chdir(os.path.join("/content/darknet/data", "obj"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("/content/darknet/data/obj/" + filename)
os.chdir("..")
with open("/content/darknet/data/train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")