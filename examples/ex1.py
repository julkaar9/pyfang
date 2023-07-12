from pyfang.tags import *


html = HTML().add(
    Head().add(
        [
            Title("example1"),
        ]
    ),
    Body().add(
        [
            TextTag.H1("Hello World"),
        ]
    ),
)
