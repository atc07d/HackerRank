# Script to walk a dir, create a zip, and email the zip using the smtp mail utility of your choice
# Replace My Dir and My Folder with directory names and replace myProc.exe with smtp mail utility

import os, sys, subprocess, datetime, zipfile, psutil

def kill(proc_id):
	process = psutil.Process(proc_id)
	for proc in process.children(recursive=True):
		proc.kill()
	process.kill()

yesterday = int(datetime.date.today().strftime("%d")) - 1
today = int(datetime.day.today().strftime("%d"))
tomorrow = int(datetime.day.today().strftime("%d")) + 1

os.chdir("My dir")

todaysZip = zipfile.("LOGS.zip", "w", zipfile.ZIP_DEFLATED)

for folderName, subFolders, fileNames in os.walk("My dir"):
	for fileName in fileNames:
		if fileName[:2] == str(today) or (fileName[:2] == str(tomorrow) and folderName == "My folder"):
			os.chdir(folderName)
			todaysZip.write(fileName)

todaysZip.close()

os.chdir("My dir")

myProc = subprocess.Popen(["myProc.exe", "body.txt", "-attach", "LOGS.zip", "-s", "Logs", "-tf", "address.txt"])

try:
	blatProc.wait(timeout=3)
except subprocess.TimeoutExpired:
	kill(blatProc.pid)
