"""
	Немного модифицированная версия первого варианта: 
	заменил последовательные проверки на цикл и теперь нет зависимости 
	от именования и количества ключей словаря file_extensions.
"""

import os
import datetime as dt

from file_extensions import file_extensions
from create_files_for_tests import path_for_test_files
from file_utils import move_file


path_to_files = path_for_test_files


def sort_files(root_path, file_extensions):
	if not os.path.exists(root_path):
		print(root_path)
		print("Sorry, path not exists!")
		return

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

		result = "Unknown file format! Skipped"
		for el_type in file_extensions:
			if el_ext in file_extensions[el_type]:
				print(el_type)

				# check on book (for example: *.fb2.zip)
				if el_type == "archives":
					el_sub_ext = os.path.splitext(el_name)[1]
					if el_sub_ext != "":
						el_sub_ext = el_sub_ext.lower()
						print(el_sub_ext)

						if el_sub_ext in file_extensions["books"]:
							el_type = "books"
							print(el_type)

				result = move_file(root_path, el_full_name, el_path, el_type)
				break

		print(result)
	

if __name__ == "__main__":
	t1 = dt.datetime.today()
	sort_files(path_to_files, file_extensions)
	t2 = dt.datetime.today()
	print(t2 - t1)
