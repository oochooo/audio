import shutil
import os
from pydub import AudioSegment
from distutils.dir_util import copy_tree

#define your globals here
check_for_the_same_first_letter = True
convert_to_mp3_and_move_to_root = True
destination = 'output'
br = '320k'

# ʕ•́ᴥ•̀ʔっ♡ do not edit lines below this comment ʕ•́ᴥ•̀ʔっ♡
move_to=os.path.expanduser(f'~/Desktop/{destination}')
list_of_files_and_their_sizes = list()
converted = list()
moved = list()
not_moved = list()
allowed_audio_extensions = ['wav', 'mp3', 'aiff', 'aif', 'flac']

def only_audio(path):
    ext = path.split('.')[-1]
    if ext in allowed_audio_extensions:
        return True
    else:
        return False

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def check_for_the_same_file(path):
    size = os.path.getsize(path)
    path_to, file_name = os.path.split(path)
    ext = file_name.split('.')[-1]
    resulting_dict = [d for d in list_of_files_and_their_sizes if (size*0.99 <= d['size'] <= size*1.01)]
    if check_for_the_same_first_letter:
        resulting_dict = [d for d in resulting_dict if d['name'][0] == file_name[0]]
    resulting_dict = [d for d in resulting_dict if d['name'].split('.')[1] == ext]
    if len(resulting_dict) > 0:
        return resulting_dict[0]
    else:
        return False

def audio_process(path):
    path_to, file_name = os.path.split(path)
    ext = file_name.split('.')[-1]
    if ext == 'mp3':
        return False
    elif ext == 'wav':
        audio = AudioSegment.from_wav(path)
    elif ext == 'aif' or ext =='aiff':
        audio = AudioSegment.from_file(path, "aiff")
    elif ext == 'flac':
        audio = AudioSegment.from_file(path, "flac")
    return audio

def main():
    list_of_audio_files = filter(only_audio, getListOfFiles('.'))
    deleted_files = list()
    os.makedirs(os.path.expanduser(f'~/Desktop/{destination}'), exist_ok=True)
    
    for x in list_of_audio_files:
        # print(x)
        path_to, file_name = os.path.split(x)
        ext = file_name.split('.')[-1]
        exists = check_for_the_same_file(x)
        if not exists:
            list_of_files_and_their_sizes.append({
            'name': file_name,
            'size': os.path.getsize(x),
            'ext' : ext,
            'full_path': x
            })
        else:
            print('duplicate -->', x, '// removing..')
            os.remove(x)
            deleted_files.append(x)
            print('removed !')
    # sorted_dict = sorted(list_of_files_and_their_sizes, key=lambda x: x['size'], reverse=True)
    sorted_dict = list_of_files_and_their_sizes
    if convert_to_mp3_and_move_to_root:
        if len(deleted_files) > 0:
            print('here are the files that got deleted ...')
            for x in deleted_files:
                print(x)
        print('starting on conversion')
        for x in sorted_dict:
                audio = audio_process(x['full_path'])
                final_path = f"{move_to}/{x['name'].split('.')[0]+'.mp3'}"
                
                if not audio:
                    print(x['full_path'], 'is mp3 ... therefore not converting. moving the file to ~/Desktop/'+destination)
                   
                    try:
                        shutil.copyfile(x['full_path'], final_path)
                    #     shutil.copyfile(x['full_path'], move_to)
                        moved.append(f"{x['name']} - {x['size']}")
                    except:
                        not_moved.append(f"{x['name']} - {x['size']}")
                        print('theres a problem moving the file to the destination, this might indicate youve previously converted the file before. skipping...')
                else:
                    print('exporting', x['name'])
                    try:
                        #final_path = f"{move_to}/{x['name'].split('.')[0]+'.mp3'}"
                        audio.export(final_path, format='mp3', bitrate=br)
                        print('converted and exported to ...', final_path)
                        converted.append(f"{x['name']} - {os.stat(final_path).st_size} ")
                    except:
                        print('theres an error. skipping ...')
    else:
        print('here are the files that got deleted ...')
        for x in deleted_files:
            print(x)

    #logging

    os.makedirs('./log', exist_ok=True)

    with open('./log/deleted_files.txt', 'w') as df:
        df.write(f"{len(deleted_files)} files deleted\n\n\n\n\n")

        for x in deleted_files:
            df.write(f"{x}\n")

    with open('./log/converted_files.txt', 'w') as cf:
        cf.write(f"{len(converted)} files converted\n\n\n\n\n")
        for x in converted:
            cf.write(f"{x}\n")

    with open('./log/moved_files.txt', 'w+') as mf:
        mf.write(f"{len(moved)} files moved\n\n\n\n\n")
        for x in moved:
            mf.write(f"{x}\n")
    with open('./log/moved_files.txt', 'w+') as nm:
        mf.write(f"{len(not_moved)} files moved\n\n\n\n\n")
        for x in moved:
            nm.write(f"{x}\n")
    copy_tree('./log', f"{move_to}/log")

if __name__ == "__main__":
    main()
        