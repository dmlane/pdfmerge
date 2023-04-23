# pdfmerge
A PDF merger - written in python3

## Installation

Use [pip](https://pip.pypa.io/en/stable/):

`pip install --user (Work in progress)`

## Usage

pdfmerge -i pdf1 -i pdf2 [-i pdfn] [--overwrite] mergedPdf

This will merge all of the input pdfs (in order) to produce mergedPdf.

- The output directory for mergedPdf must exist.
- Providing '--noclobber' will return an error  if mergedPdf exists already
- If any of the input files are missing, then an error will be returned

pdfmerge -V

pdfmerge --version

- Displays the version

