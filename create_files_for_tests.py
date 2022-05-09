
import os

from file_extensions import file_extensions
from file_utils import delete_files, create_test_files


path_for_test_files = os.path.join(os.getcwd(), "for_tests")
path_for_test_files = os.path.normpath(path_for_test_files)
files_count = 1000

if __name__ == "__main__":
	delete_files(path_for_test_files)
	# input("Press Enter for continue...")
	create_test_files(path_for_test_files, files_count, file_extensions)
