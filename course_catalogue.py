#!/usr/bin/env python

import sys
import subprocess


def pdf_to_txt(filename):
    """Convert a pdf file on disk to text.
    Needs the pdftotext binary from the cpdf package."""
    p = subprocess.Popen(["pdftotext", "-layout", filename, "-"],
        stdout=subprocess.PIPE)
    return p.communicate()[0]

def parse_course_list(doc):
    course_list = []
    doc = doc[:doc.find("Description of Courses in the Academic Core")]
    doc = doc[doc.find("ACC"):]
    doc = doc.split("\n")
    for l in doc:
        course = l.split()
        if len(course) < 2:
            continue
        if course[-2][-1] == ".":
            course = [course[0], " ".join(course[1:-1]).strip(".")]
        course_list.append(course)
    return course_list


def parse_full(doc):
    courses = parse_course_list(doc)
    return courses


if __name__ == "__main__":
    doc = pdf_to_txt(sys.argv[1])
    print parse_full(doc)
