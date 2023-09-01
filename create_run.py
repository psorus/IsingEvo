import os


files=os.listdir("results")
with open("run.sh", "w") as f:
    for file in files:
        file=file.replace(".json",".py")
        f.write("python3 {} \n".format(file))

os.system("chmod +x run.sh")

