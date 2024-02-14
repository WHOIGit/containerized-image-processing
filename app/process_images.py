import os

import logging
logging.basicConfig(level=logging.INFO)

from floyd_steinberg import floyd_steinberg_dithering

INPUT_DIRECTORY = '/input'
OUTPUT_DIRECTORY = '/output'

# Get a list of all the files in the input directory
input_files = os.listdir(INPUT_DIRECTORY)

# Process each file
for input_file in input_files:
    # save output file as a png if it's a jpg
    output_file = input_file.replace('.jpg', '.png')
    input_path = os.path.join(INPUT_DIRECTORY, input_file)
    output_path = os.path.join(OUTPUT_DIRECTORY, output_file)
    try:
        floyd_steinberg_dithering(input_path, output_path, resize=True)
        logging.info(f'Processed {input_file}')
    except Exception as e:
        logging.error(f'Error processing {input_file}: {e}')
