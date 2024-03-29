"""
	Более продвинутый вариант, поскольку может отделять не только *.fb2.zip,
	но и другие архивы, благодаря тому, что перед началом работы преобразует 
	словарь file_extensions (объединяет всё категории в один словарь).
"""

import os
import datetime as dt

from file_extensions import file_extensions
from create_files_for_tests import path_for_test_files
from file_utils import move_file


path_to_files = path_for_test_files


def unite_all_extensions(file_extensions):
	"""
		Объединяет все категории в один словарь вида:
		{
			".zip" : "archives",
			".exe" : "soft",
			...
		}
	"""
	result = {}
	for key in file_extensions.keys():
		for el in file_extensions[key]:
			result[el] = key

	return result


def sort_files(root_path, file_extensions):
	if not os.path.exists(root_path):
		print(root_path)
		print("Sorry, path not exists!")
		return

	united_file_extensions = unite_all_extensions(file_extensions)
	print(united_file_extensions)
	content_list = os.listdir(root_path)

	for el_full_name in content_list:
		print("====================================================")
		print(el_full_name)
		el_path = os.path.join(root_path, el_full_name)
		el_path = os.path.normpath(el_path)
		print(el_path)

		if os.path.isdir(el_path):
			print("This is a directory. Skipped")
			continue
			
		el_name, el_ext = os.path.splitext(el_full_name)
		
		if el_ext == "":
			print("Extension is empty. Skipped")
			continue
		
		el_ext = el_ext.lower()
		print(el_ext)
		
		if el_ext in united_file_extensions:
			el_type = united_file_extensions[el_ext]
			print(el_type)
			
			# check on book (for example: *.fb2.zip)
			if el_type == "archives":
				el_sub_ext = os.path.splitext(el_name)[1]
				if el_sub_ext != "":
					el_sub_ext = el_sub_ext.lower()
					print(el_sub_ext)
					
					if el_sub_ext in united_file_extensions:
						el_type = united_file_extensions[el_sub_ext]
						print(el_type)
			
			result = move_file(root_path, el_full_name, el_path, el_type)
			print(result)
			
		else:
			print("Unknown file format! Skipped")
	

if __name__ == "__main__":
	t1 = dt.datetime.today()
	sort_files(path_to_files, file_extensions)
	t2 = dt.datetime.today()
	print(t2 - t1)