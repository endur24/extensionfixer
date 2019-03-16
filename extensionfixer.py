#Run this file in the directory you wish to rename files in.
#It will rename including files in subfolders

import os, sys

for (dirpath, dirnames, filenames) in os.walk(os.path.dirname(os.path.abspath(__file__))):
	for filename in filenames:
		# print dirpath
		old_file_name = os.path.join(dirpath, filename)
		new_filename = os.path.join(dirpath, filename.split('?')[0])
		if os.path.isfile(old_file_name):
			print('old_file_name: ', old_file_name)
			print('new_filename: ', new_filename)

			os.rename(old_file_name, new_filename)
