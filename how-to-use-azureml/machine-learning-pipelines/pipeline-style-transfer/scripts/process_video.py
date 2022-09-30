import argparse
import glob
import os
import subprocess

parser = argparse.ArgumentParser(description="Process input video")
parser.add_argument('--input_video', required=True)
parser.add_argument('--output_audio', required=True)
parser.add_argument('--output_images', required=True)

args = parser.parse_args()

os.makedirs(args.output_audio, exist_ok=True)
os.makedirs(args.output_images, exist_ok=True)

subprocess.run(
    f"ffmpeg -i {args.input_video} {args.output_audio}/video.aac",
    shell=True,
    check=True,
)


subprocess.run(
    f"ffmpeg -i {args.input_video} {args.output_images}/%05d_video.jpg -hide_banner",
    shell=True,
    check=True,
)
