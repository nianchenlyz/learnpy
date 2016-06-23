import os
import glob

os.chdir("D:\workspace")
for file in glob.glob("*.json"):
    file_name = os.path.splitext(file)[0]
    print file_name
    extension = os.path.splitext(file)[1]
    print extension
    new_file_name = file_name[:-6] + extension
    print new_file_name
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(e)
    else:
        print("Renamed {} to {}".format(file, new_file_name))
