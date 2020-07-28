
import random
import os
# import file_sorter


# path = r"C:\Python34\my_projects\for_tests"
path = os.getcwd() + r"\for_tests"
# path = file_sorter.path

file_extensions = {
	"archives" : [".rar", ".zip", ".7z", ".tar", ".gz"],
	"soft" : [".exe", ".msi", ".com", ".bat", ".reg"],
	"books" : [".djvu", ".fb2", ".epub", ".mobi"],
	"docs_books" : [".pdf", ".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
	"images" : [".jpg", ".jpeg", ".gif", ".bmp", ".png", ".webp"],
	"torrents" : [".torrent"],
	"audio" : [".mp3", ".wav", ".wma", ".midi", ".ogg", ".flac"],
	"video" : [".avi", ".3gp", ".mpeg", ".mkv", ".mp4", ".flv"]
	# "images" : [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ]
}

# file_extensions_list = []
# for i in file_sorter.file_extensions.keys():
	# file_extensions_list.append(file_sorter.file_extensions[i])

# file_extensions_list = [ file_sorter.file_extensions[i] for i in file_sorter.file_extensions.keys() ]

# for i in file_extensions.keys():
	# file_extensions_list.append(file_extensions[i])

file_extensions_list = [ file_extensions[key] for key in file_extensions.keys() ]

# print(file_extensions_list)

for i in range(30):
	n = random.randint(1000, 1000000)
	f_ext = random.choice(random.choice(file_extensions_list))
	# f_name = path + "\\file_" + str(i) +  f_ext
	f_name = "{0}\\file_{1}{2}".format(path, str(i), f_ext)
	# f_name = "{0}\\file_{1}_{2}{3}".format(path, str(i), str(n), f_ext)
	print(f_name)
	print(n)
	with open(f_name, "w") as file:
		file.write(str(n))
