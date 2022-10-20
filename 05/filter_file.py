# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=unspecified-encoding
# pylint: disable=consider-using-with


from typing import Generator, List, TextIO, Union


def filter_file(
    file: Union[str, TextIO], to_find: List[str]
) -> Generator[str, None, None]:
    to_find_set = set(map(str.lower, to_find))

    if isinstance(file, str):
        f = open(file, "r")
    else:
        f = file  # type: ignore
    for line in f:
        line = line.strip("\n")
        parsed_line = set(map(str.lower, line.split(" ")))
        if len(parsed_line.intersection(to_find_set)):
            yield line

    if isinstance(file, str):
        f.close()
