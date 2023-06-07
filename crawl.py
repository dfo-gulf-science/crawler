import os
import argparse
import re
from copy import deepcopy
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--source_dir', help='the root directory from which this script will begin crawling', required=True)
parser.add_argument('--target_dir', help='where should the converted jpg images be stored.', required=True)
args = parser.parse_args()
source_dir = args.source_dir
target_dir = args.target_dir

# ensure that the source and target dirs exist
assert os.path.exists(source_dir), f"Source directory '{source_dir}' does not exist."
assert os.path.exists(target_dir), f"Target directory '{target_dir}' does not exist."
assert source_dir[-1] not in ["/", '\\'], f"Source directory must not have a trailing slash."
assert target_dir[-1] not in ["/", '\\'], f"Target directory must not have a trailing slash."

# iterate through all files, beginning from source_dir
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # use some regex to make sure the structure of the file is good
        ## we are expecting something like: 2023-30922-037.tif
        pattern = """
           (?P<year>^20[\d]{2})  # the year, will start with 20**
           (-)
           (?P<sample_id>[\d]*)  # the sample id
           (-)
           (?P<fish_number>[\d]{3}[ab]{0,1})  # the zero-padded fish number
           (\.)
           (?P<file_type>tif$|tiff$) #  the file extention
           """
        search = re.search(pattern, file.lower(), re.VERBOSE)

        if search:
            new_file = deepcopy(file)
            new_file = new_file.lower().replace(search.groupdict().get("file_type"), "jpg")

            infile = os.path.join(root, file)
            if "enhanced" in infile.lower():
                new_file = f'{new_file.split(".")[0]}_enhanced.{new_file.split(".")[1]}'

            outfile = os.path.join(target_dir, new_file)

            # inspired by https://stackoverflow.com/questions/28870504/converting-tiff-to-jpeg-in-python
            try:
                im = Image.open(infile)
                im.thumbnail(im.size)
                im.save(outfile, "JPEG", quality=100)
            except Exception as ex:
                print(ex, "cannot convert file:", infile)
        else:
            print(f"ignoring file: {file}")
