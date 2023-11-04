import os

j = [1,
     2,
     3
]

test = 1

def very_important_function(template: str, *variables, file: os.PathLike, engine: str, header: bool = True, debug: bool = False):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, 'w') as f:
        pass

if test \
  and test:
      pass


def foo():

    print("All the newlines above me should be deleted!")


if test:

    print("No newline above me!")

    print("There is a newline above me, and that's OK!")


class Point:

    x: int
    y: int