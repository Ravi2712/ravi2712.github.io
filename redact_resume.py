#!/usr/bin/env python3
"""
Redacts sensitive info (phone, email) from the resume PDF.
Replaces them with grey bars — text is permanently removed.
Usage: python3 redact_resume.py
"""
import sys
import fitz  # pymupdf

PDF_PATH = "files/Resume_JP_PhD_SUNY_P.pdf"
REDACT_TARGETS = [
    "6309624268",
    "patel.ravi2712@gmail.com",
]
GREY = (0.45, 0.45, 0.45)


def redact(pdf_path, targets, fill_color):
    doc = fitz.open(pdf_path)
    found_any = False
    for page in doc:
        for target in targets:
            rects = page.search_for(target)
            for rect in rects:
                page.add_redact_annot(rect, fill=fill_color)
                print(f"  Redacted: {target}")
                found_any = True
        page.apply_redactions()

    tmp = pdf_path + ".tmp"
    doc.save(tmp)
    doc.close()

    import os
    os.replace(tmp, pdf_path)
    return found_any


if __name__ == "__main__":
    print(f"Scanning {PDF_PATH}...")
    found = redact(PDF_PATH, REDACT_TARGETS, GREY)
    if not found:
        print("  Nothing to redact (already clean).")
    print("Done.")
