# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import argparse
import os

print("In extract.py")
print("As a data scientist, this is where I use my extract code.")

parser = argparse.ArgumentParser("extract")
parser.add_argument("--input_extract", type=str, help="input_extract data")
parser.add_argument("--output_extract", type=str, help="output_extract directory")

args = parser.parse_args()

print(f"Argument 1: {args.input_extract}")
print(f"Argument 2: {args.output_extract}")

if args.output_extract is not None:
    os.makedirs(args.output_extract, exist_ok=True)
    print(f"{args.output_extract} created")

with open(os.path.join(args.input_extract, 'Titanic.csv'), 'rb') as f:
    content = f.read()
    with open(os.path.join(args.output_extract, 'Titanic.csv'), 'wb') as fw:
        fw.write(content)
