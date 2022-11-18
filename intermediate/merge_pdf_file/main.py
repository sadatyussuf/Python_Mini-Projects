import pathlib
from PyPDF2 import PdfFileMerger

current_folder = pathlib.Path(__file__).parent
data_folder = current_folder.joinpath('data')

get_files = list(data_folder.glob('*.pdf'))


merger = PdfFileMerger()

for file in get_files:
    merger.append(file)
merger.write(data_folder.joinpath('merged.pdf'))
merger.close()
# print(get_files)
