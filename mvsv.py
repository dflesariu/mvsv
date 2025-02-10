import subprocess

input_folder = "/Users/{username}/Documents/code/mvsv"
movies_folder = ""
series_folder = ""

#list all file names, A=not implied . and .., 1= only one name per line
listing = subprocess.check_output(['ls', '-A1', input_folder])

print (listing)