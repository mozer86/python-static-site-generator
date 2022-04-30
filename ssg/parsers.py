import shutil
from typing import List
from pathlib import Path

class Parser:

    extentions=List[str[]]

    def valid_extension(self, extension):
        return extention in self.extension

    def parse(self, path, source, dest):
        self.path=Path(path)
        self.source=Path(source)
        self.dest=Path(dest)

        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source,dest):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):

        extentions = [".jpg", ".png", ".gif", ".css", ".html"]

        def parse(self, path, source, dest):
            self.path=Path(path)
            self.source=Path(source)
            self.dest=Path(dest)
            Parser.copy(path, source, dest)
            raise NotImplementedError
