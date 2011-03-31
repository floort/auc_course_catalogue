#!/usr/bin/env python

import sys
import subprocess
import re

def pdf_to_txt(filename):
    """Convert a pdf file on disk to text.
    Needs the pdftotext binary from the xpdf package."""
    p = subprocess.Popen(["pdftotext", "-layout", filename, "-"],
        stdout=subprocess.PIPE)
    return p.communicate()[0]

def parse_course_list(doc):
    return
    re.findall(r'^(?P<id>(?:SCI|SSC|HUM|ACC)\S+)\s+(?P<name>[^.]*)',doc,re.M)


def parse_full(doc):
    courses = parse_course_list(doc)
    return courses


if __name__ == "__main__":
    doc = pdf_to_txt(sys.argv[1])
    print parse_full(doc)
