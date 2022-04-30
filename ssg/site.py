import Path from pathlib

Class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(source)

    def create_dir(self, path):
        directory = self.dest / relative_to(self.source)


    def build (self):
        mkdir(directory, parents = True, exist_ok = True)
        for path in self.source.rglob("*"):
            if path = directory:
                create_dir(path)

                
