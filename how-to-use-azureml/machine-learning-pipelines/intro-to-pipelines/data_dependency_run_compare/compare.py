# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import argparse
import os

print("In compare.py")
print("As a data scientist, this is where I use my compare code.")
parser = argparse.ArgumentParser("compare")
parser.add_argument("--compare_data1", type=str, help="compare_data1 data")
parser.add_argument("--compare_data2", type=str, help="compare_data2 data")
parser.add_argument("--output_compare", type=str, help="output_compare directory")
parser.add_argument("--pipeline_param", type=int, help="pipeline parameter")

args = parser.parse_args()

print(f"Argument 1: {args.compare_data1}")
print(f"Argument 2: {args.compare_data2}")
print(f"Argument 3: {args.output_compare}")
print(f"Argument 4: {args.pipeline_param}")

if args.output_compare is not None:
    os.makedirs(args.output_compare, exist_ok=True)
    print(f"{args.output_compare} created")
