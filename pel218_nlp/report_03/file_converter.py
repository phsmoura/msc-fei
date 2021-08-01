import os

class FileConverter:
    """Convert iso-8859 files to utf-8"""
    def __init__(self, name_dir: str, iso_files_dir: str) -> None:
        self.name_subdir = name_dir
        self.iso_files_dir = iso_files_dir
        self.iso_files = list(os.walk(self.iso_files_dir))[0][2]
        self.utf_files_dir = 'corpus_utf_8'

    def convert_files_to_utf_8(self) -> list:
        if not os.path.isdir(self.utf_files_dir):
            os.mkdir(self.utf_files_dir)
        if not os.path.isdir(self.utf_files_dir + '/' + self.name_subdir):
            os.mkdir(self.utf_files_dir + '/' + self.name_subdir)
        
        for f in self.iso_files:
            f = f.replace(' ', '\ ')
            os.system(f'iconv -f ISO-8859-1 -t UTF-8 {self.iso_files_dir}/{f} -o {self.utf_files_dir}/{self.name_subdir}/{f}')

        return list(os.walk(self.utf_files_dir + '/' + self.name_subdir))[0][2]
