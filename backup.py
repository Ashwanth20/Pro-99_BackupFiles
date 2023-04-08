import os
import time
import shutil

def delfilefolder():
    del_folder_count = 0
    del_files_count = 0
    
    path = "/Path_to_Del"
    days = 30
    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds >= getfile_or_folderage(root_folder):
                removefolder(root_folder)
                del_folder_count += 1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)
                    if seconds >= getfile_or_folderage(folder_path):
                        removefolder(folder_path)
                        del_folder_count += 1
                
                for file in files:
                    file_path = os.path.join(root_folder,file)
                    if seconds >= getfile_or_folderage(file_path):
                        removefile(file_path)
                        del_files_count += 1
                    else:
                        if seconds >= getfile_or_folderage(path):
                            removefile(path)
                            del_files_count += 1
                        else:
                            print(f'"{path}" is not found')
                            del_files_count += 1
                        print(f"Total folders deleted: {del_folder_count}")
                        print(f"Total files deleted: {del_files_count}")

def removefolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is successfully deleted")
    else:
        print(f"Unable to delete the " + path)

def removefile(path):
    if not os.remove(path):
        print(f"{path} is successfully deleted")
    else:
        print(f"Unable to delete the " + path)

def getfile_or_folderage(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__delfilefolder__':
    delfilefolder()