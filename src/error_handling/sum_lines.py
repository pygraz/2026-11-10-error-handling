import argparse
import logging
from pathlib import Path

_log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        prog="sum_lines",
        description="Print the sum of numbers stored in lines in a text file.",
    )
    parser.add_argument("text_path", metavar="FILE", type=Path)
    arguments = parser.parse_args()
    try:
        print(sum_of_lines_2_with_empty_lines(arguments.text_path))
    except (OSError, NumberLineError) as error:
        print(f"Error: {error}")


def sum_of_lines_1_naive(text_path: Path) -> int:
    text_file = text_path.open()  # happy
    result = 0  # happy
    for line in text_file:  # happy
        result += int(line)  # happy
    text_file.close()  # happy
    return result  # happy


def sum_of_lines_2_with_empty_lines(text_path: Path) -> int:
    text_file = text_path.open()  # happy
    result = 0  # happy
    for line in text_file:  # happy
        if line.rstrip("\n\r") == "":  # special
            pass  # Do nothing.         # special
        else:  # special
            result += int(line)  # happy
    text_file.close()  # happy
    return result  # happy


class NumberLineError(ValueError):
    def __init__(self, path: Path, line_number: int, line: str):
        self._path = path
        self._line_number = line_number
        self._line = line

    def __str__(self):
        line_without_newline = self._line.rstrip("\n\r")
        return (
            f"{self._path.name} at line {self._line_number}: "
            f"Line must be number but is: {line_without_newline!r}."
        )


class ManyDataError(ValueError):
    def __init__(self):
        self._data_errors: list[NumberLineError] = []

    def add(self, data_error: NumberLineError):
        self._data_errors.append(data_error)


def sum_of_lines_3_with_text_error(text_path: Path) -> int:
    text_file = text_path.open()
    result = 0
    for line_number, line in enumerate(text_file, 1):
        if line.rstrip("\n\r") == "":
            pass  # Do nothing.
        else:
            try:
                result += int(line)
            except ValueError:
                raise NumberLineError(text_path, line_number, line)
    text_file.close()
    return result


def sum_of_lines_4_with_cleanup(text_path: Path) -> int:
    text_file = text_path.open()  # happy
    try:  # error
        result = 0  # happy
        for line_number, line in enumerate(text_file, 1):  # happy
            if line.rstrip("\n\r") == "":  # special
                pass  # Do nothing.                                    # special
            else:  # special
                try:  # error
                    result += int(line)  # happy
                except ValueError:  # error
                    raise NumberLineError(text_path, line_number, line)  # error
    finally:  # error
        text_file.close()  # happy
    return result  # happy


def sum_of_lines_5_with_warning(text_path: Path) -> int:
    text_file = text_path.open()  # happy
    result = 0  # happy
    has_lines = False  # warning
    try:  # error
        for line_number, line in enumerate(text_file, 1):  # happy
            if line.rstrip("\n\r") == "":  # special
                pass  # Do nothing.                                      # special
            else:  # special
                try:  # error
                    result += int(line)  # happy
                    has_lines = True  # warning
                except ValueError:  # error
                    raise NumberLineError(text_path, line_number, line)  # error
    finally:  # error
        text_file.close()  # happy
    if not has_lines:  # warning
        print(  # warning
            f"Warning: {text_path.name} did not contain any numbers, "  # warning
            f"using sum of 0."  # warning
        )  # warning
    return result  # happy


def sum_of_lines_6_naive_pythonic(text_path: Path) -> int:
    return sum(int(line) for line in text_path.read_text().splitlines())


if __name__ == "__main__":
    main()
