import os
import re

from provenance.capture import Step, Logger

from floyd_steinberg import floyd_steinberg_dithering

INPUT_DIRECTORY = '/input'
OUTPUT_DIRECTORY = '/output'

# Get a list of all the files in the input directory
input_files = os.listdir(INPUT_DIRECTORY)

RESIZE = True

logger = Logger.file('/logs/output.log')

with Step(description='Apply dithering to images', logger=logger) as job:
    job.add_parameter(name='dithering_algorithm', value='Floyd-Steinberg')
    job.add_parameter(name='color_space', value='grayscale')
    job.add_parameter(name='resize', value=RESIZE)
    # Process each file
    for input_file in input_files:
        # save output file as a png
        output_file = re.sub(r'\.\w+$', '.png', input_file)
        input_path = os.path.join(INPUT_DIRECTORY, input_file)
        output_path = os.path.join(OUTPUT_DIRECTORY, output_file)
        try:
            with Step(parent=job) as step:
                step.add_input(name=input_file)
                step.add_output(name=output_file)
                step.add_parameter(name='resize', value=RESIZE)
                floyd_steinberg_dithering(input_path, output_path, resize=RESIZE)
        except:
            # error is already logged by the Step, proceed to the next file
            continue
