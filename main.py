#! /usr/bin/env python

import argparse
import json

from src.raw_text_to_dict import jsonify_text
from src.read_pdf import pdf_to_raw_text
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("pdf")
args = parser.parse_args()
pdf = args.pdf

out = Path(pdf).stem

if __name__ == "__main__":
    pdf_to_raw_text(pdf, f'buffer/{out}.raw')
    jsonify_text(f'buffer/{out}.raw', f'out/{out}.json')

