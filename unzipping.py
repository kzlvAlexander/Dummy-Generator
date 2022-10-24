import pathlib
from zipfile import ZipFile

archive = 'file.zip'

with ZipFile(archive, 'r') as zip_file:
    files = [file.filename for file in zip_file.infolist()]
    print(files)
    zip_file.extractall('unzipped_docs')
    abspath_list = []
    for file in files:
        abspath_list.append(str(pathlib.Path(f'unzipped_docs/{file}').resolve()))
    print(abspath_list)
