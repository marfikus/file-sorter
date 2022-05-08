
import os
import shutil

from file_extensions import file_extensions
from create_files_for_tests import path_for_test_files


path_to_files = path_for_test_files


def move_file(root_path, el_full_name, el_path, content_type):
	res = ""
	dst_path = os.path.join(root_path, content_type)
	dst_path = os.path.normpath(dst_path)
	
	if not os.path.exists(dst_path):
		os.mkdir(dst_path)
		
	el_path_new = os.path.join(dst_path, el_full_name)
	el_path_new = os.path.normpath(el_path_new)
	
	if not os.path.exists(el_path_new):
		res = shutil.move(el_path, dst_path)

	return res


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
		
		if el_ext in file_extensions["archives"]:
			print("archives")
			
			# check on book (for example: *.fb2.zip)
			el_sub_ext = os.path.splitext(el_name)[1]
			if el_sub_ext != "":
				el_sub_ext = el_sub_ext.lower()
				print(el_sub_ext)
				
				if el_sub_ext in file_extensions["books"]:
					print("books")
					res = move_file(root_path, el_full_name, el_path, "Books")
					print(res)
					continue
			
			res = move_file(root_path, el_full_name, el_path, "Archives")
			print(res)
			
		elif el_ext in file_extensions["soft"]:
			print("soft")
			res = move_file(root_path, el_full_name, el_path, "Soft")
			print(res)
			
		elif el_ext in file_extensions["books"]:
			print("books")
			res = move_file(root_path, el_full_name, el_path, "Books")
			print(res)
			
		elif el_ext in file_extensions["docs_books"]:
			print("docs_books")
			res = move_file(root_path, el_full_name, el_path, "Docs_books")
			print(res)
			
		elif el_ext in file_extensions["images"]:
			print("images")
			res = move_file(root_path, el_full_name, el_path, "Images")
			print(res)
			
		elif el_ext in file_extensions["torrents"]:
			print("torrents")
			res = move_file(root_path, el_full_name, el_path, "Torrents")
			print(res)
			
		elif el_ext in file_extensions["audio"]:
			print("audio")
			res = move_file(root_path, el_full_name, el_path, "Audio")
			print(res)
			
		elif el_ext in file_extensions["video"]:
			print("video")
			res = move_file(root_path, el_full_name, el_path, "Video")
			print(res)
			
		else:
			print("Unknown file format!")
	

if __name__ == "__main__":
	sort_files(path_to_files, file_extensions)
