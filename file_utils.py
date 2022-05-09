
import random
import os
import shutil


def create_test_files(root_path, files_count, file_extensions):
	if not os.path.exists(root_path):
		os.mkdir(root_path)

	file_extensions_list = [file_extensions[key] for key in file_extensions.keys()]

	for i in range(files_count):
		n = random.randint(1000, 1000000)
		file_ext = random.choice(random.choice(file_extensions_list))
		if file_ext == ".zip":
			sub_ext = random.choice(["", ".fb2"])
			file_ext = sub_ext + file_ext

		file_name = "file_{0}{1}".format(str(i), file_ext)
		file_path = os.path.join(root_path, file_name)
		file_path = os.path.normpath(file_path)
		print(file_path)
		print(n)
		with open(file_path, "w") as file:
			file.write(str(n))


def delete_files(root_path):
	if os.path.exists(root_path):
		shutil.rmtree(root_path)


def move_file(root_path, el_full_name, el_path, content_type):
	result = ""
	dst_path = os.path.join(root_path, content_type.capitalize())
	dst_path = os.path.normpath(dst_path)
	
	if not os.path.exists(dst_path):
		os.mkdir(dst_path)
		
	el_path_new = os.path.join(dst_path, el_full_name)
	el_path_new = os.path.normpath(el_path_new)
	
	if not os.path.exists(el_path_new):
		result = shutil.move(el_path, dst_path)

	return result
