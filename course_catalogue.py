#!/usr/bin/env python

import sys
import subprocess
import StringIO
from lxml import html


def pdf_to_html(filename):
    """Convert a pdf file on disk to html.
    Needs the pdftotext binary from the cpdf package."""
    p = subprocess.Popen(["pdftotext", "-layout", "-htmlmeta", filename, "-"],
        stdout=subprocess.PIPE)
    return p.communicate()[0]

def parse_courses(html_doc):
    tree = html.fromstring(html_doc)
    return tree


if __name__ == "__main__":
    html_doc = pdf_to_html(sys.argv[1])
    print dir(parse_courses(html_doc))

