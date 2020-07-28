
import os
import shutil


# path = "D:\Downloads"
# path = r"C:\Python34\my_projects\for_tests"
path = os.getcwd() + r"\for_tests"

# archives = [".rar", ".zip", ".7z", ".tar", ".gz"]
# soft = [".exe", ".msi", ".com", ".bat", ".reg"]
# books = [".djvu", ".fb2", ".epub", ".mobi"]
# docs_books = [".pdf", ".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"]
# images = [".jpg", ".jpeg", ".gif", ".bmp", ".png", ".webp"]
# torrents = [".torrent"]
# audio = [".mp3", ".wav", ".wma", ".midi", ".ogg", ".flac"]
# video = [".avi", ".3gp", ".mpeg", ".mkv", ".mp4", ".flv"]
# images = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ]

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

content_list = os.listdir(path)

def move_file(path, el_full_name, el_path, content_type):
	res = ""
	dst_path = os.path.join(path, content_type)
	dst_path = os.path.normpath(dst_path)
	
	if not os.path.exists(dst_path):
		os.mkdir(dst_path)
		
	el_path_new = os.path.join(dst_path, el_full_name)
	el_path_new = os.path.normpath(el_path_new)
	
	if not os.path.exists(el_path_new):
		res = shutil.move(el_path, dst_path)

	return res


for el_full_name in content_list:
	print("====================================================")
	print(el_full_name)
	el_path = os.path.join(path, el_full_name)
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
				res = move_file(path, el_full_name, el_path, "Books")
				print(res)
				continue
		
		res = move_file(path, el_full_name, el_path, "Archives")
		print(res)
		
	elif el_ext in file_extensions["soft"]:
		print("soft")
		res = move_file(path, el_full_name, el_path, "Soft")
		print(res)
		
	elif el_ext in file_extensions["books"]:
		print("books")
		res = move_file(path, el_full_name, el_path, "Books")
		print(res)
		
	elif el_ext in file_extensions["docs_books"]:
		print("docs_books")
		res = move_file(path, el_full_name, el_path, "Docs_books")
		print(res)
		
	elif el_ext in file_extensions["images"]:
		print("images")
		res = move_file(path, el_full_name, el_path, "Images")
		print(res)
		
	elif el_ext in file_extensions["torrents"]:
		print("torrents")
		res = move_file(path, el_full_name, el_path, "Torrents")
		print(res)
		
	elif el_ext in file_extensions["audio"]:
		print("audio")
		res = move_file(path, el_full_name, el_path, "Audio")
		print(res)
		
	elif el_ext in file_extensions["video"]:
		print("video")
		res = move_file(path, el_full_name, el_path, "Video")
		print(res)
		
	else:
		print("Unknown file format!")
	
