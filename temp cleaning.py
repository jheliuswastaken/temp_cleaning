import os, shutil

windows_path = os.environ['WINDIR']
temp_path = os.path.join(windows_path, 'Temp')
appdata_path = os.getenv('LOCALAPPDATA')
appdata_temp_path = os.path.join(appdata_path, 'Temp')

print(f'[START] {temp_path}')
for filename in os.listdir(temp_path):
    file_path = os.path.join(temp_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f'{file_path} | {e}')
print(f'[END] {temp_path}')

print(f'[START] {appdata_temp_path}')
for filename in os.listdir(appdata_temp_path):
    file_path = os.path.join(temp_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f'{file_path} | {e}')
print(f'[END] {appdata_temp_path}')

os.system('pause')
