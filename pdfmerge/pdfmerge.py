#!/usr/bin/env python
""" Merge the pdfs supplied on the command line - the last file is the output
   """

import argparse
import importlib.metadata
import os
import sys

# import shutil
from PyPDF2 import PdfMerger


class MyException(Exception):
    """Generic exception to avoid pylint errors"""


def __version__():
    try:
        return importlib.metadata.version(__package__ or __name__)
    except importlib.metadata.PackageNotFoundError:
        return "Version not set"


def merge_pdfs(input_files: list, output_file: str, overwrite: bool):
    """Perform the actual merge"""
    if os.path.exists(output_file) and not overwrite:
        raise MyException(
            f"Output file {output_file} already exists (Use '--overwrite' if neccessary)"
        )
    merger = PdfMerger()
    for input_file in input_files:
        if not os.path.exists(input_file):
            raise MyException(f"Input file {input_file} does not exist")
        merger.append(input_file)
    merger.write(output_file)


def main():
    """Main entry point"""
    try:
        parser = argparse.ArgumentParser()
        # parser.add_argument("-i","--input_file", nargs="+")
        parser.add_argument(
            "-i",
            "--input_file",
            action="append",
            required=True,
            help="Input PDF files (>=2)",
        )
        parser.add_argument("-V", "--version", action="version", version=__version__())
        parser.add_argument(
            "--overwrite",
            action="store_true",
            default=False,
            help="Do not overwrite existing output",
        )
        parser.add_argument("output_file")
        options = parser.parse_args()
        if len(options.input_file) < 2:
            raise MyException("You must provide at >2 input files")
        merge_pdfs(options.input_file, options.output_file, options.overwrite)

    except MyException as inst:
        print(inst.args[0], file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    main()
