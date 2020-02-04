#Import statements
import os

if __name__ == "__main__":
	folder_name = "/Volumes/T7 Touch/School/VIP/Data/2018/Pictures/"
	
	count = 0
	for old_file_name in sorted(os.listdir(folder_name)):
		# print(old_file_name)
		if "_" not in old_file_name:
			#print(old_file_name)
			new_file_name = str(count) + ".jpg"

			complete_path_for_old_file = folder_name + old_file_name
			complete_path_for_new_file = folder_name + new_file_name
			
			os.rename(complete_path_for_old_file, complete_path_for_new_file)
			count += 1
	#print(count)