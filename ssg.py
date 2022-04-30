import typer
from site import Site

def main(self, source = "content", dest = "dist"):
    config = {source: "source", dest: "dest"}
    build(Site(**config))

typer.run(main())
