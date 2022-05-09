
import random
import os
import shutil

from file_extensions import file_extensions


path_for_test_files = os.path.join(os.getcwd(), "for_tests")
path_for_test_files = os.path.normpath(path_for_test_files)
files_count = 1000


file_extensions_list = [ file_extensions[key] for key in file_extensions.keys() ]
# print(file_extensions_list)


def create_files(root_path, files_count):
	if not os.path.exists(root_path):
		os.mkdir(root_path)

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


if __name__ == "__main__":
	delete_files(path_for_test_files)
	# input("Press Enter for continue...")
	create_files(path_for_test_files, files_count)
