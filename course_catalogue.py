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

def remove_page_numbers(doc):
    """Remove the lines containing page numbers from doc"""
    clean_doc = ""
    page = 2 # page 1 isn't there
    for l in doc.split("\n"):
        if l.strip().isdigit():
            if int(l.strip()) == page:
                page += 1
                continue
        clean_doc += "\n"+l
    return clean_doc

def parse_course_list(doc):
    r = r'^\s?(?P<id>(?:SCI|SSC|HUM|ACC)\S+)\s+(?P<name>[^.]*)\.+\s*(?P<page>\d+)$'
    return re.findall(r, doc,re.M)


def parse_full(doc):
    doc = remove_page_numbers(doc)
    courses = parse_course_list(doc)
    return courses


if __name__ == "__main__":
    doc = pdf_to_txt(sys.argv[1])
    print parse_full(doc)
