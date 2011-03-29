#!/usr/bin/env python

import sys
import subprocess

def pdf_to_html(filename):
    p = subprocess.Popen(["pdftotext", "-layout", "-htmlmeta", filename, "-"])
    html = p.read()
    p.terminate()
    return html


if __name__ == "__main__":
    print pdf_to_html(sys.argv[1])
