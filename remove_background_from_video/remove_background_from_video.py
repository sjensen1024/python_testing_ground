from rembg import remove
from moviepy import VideoFileClip
from PIL import Image 
import numpy
import yaml

def run():
    config = setup_config()
    extract_frames_and_remove_backgrounds(config)
    # TODO: Refactor and make the code do the following:
    #       1) Combine the frames into a result .mp4
    #       2) Clear out the input/output directories if there are already existing files, as well as the result.

def setup_config():
    with open("./config.yml", 'r') as stream:
        config = yaml.safe_load(stream)
    return {
      'original_frames_directory': config.get('original_frames_directory'),
      'transparent_frames_directory': config.get('transparent_frames_directory'),
      'input_file': config.get('input_file'),
      'output_file': config.get('output_file'),
      'save_original_frames': config.get('save_original_frames')
    }

def extract_frames_and_remove_backgrounds(config):
    original_video =  VideoFileClip(config.get('input_file')) 
    count = 0
    for frame in original_video.iter_frames():
        count += 1
        frame_file_name = get_frame_file_name(count, original_video.n_frames)
        export_frame_as_images(frame, config, frame_file_name)

def get_frame_file_name(current_frame, number_of_frames):
    file_name = '_'
    duration_digits = get_number_of_digits(number_of_frames)
    frame_digits = get_number_of_digits(current_frame)
    if duration_digits == frame_digits:
        return file_name + str(current_frame) + '.png'
    prefix = '0' * (duration_digits - frame_digits)
    return file_name + prefix + str(current_frame) + '.png'

def export_frame_as_images(frame, config, file_name):
    original_image = get_frame_as_image(frame)
    if config.get('save_original_frames'):
        original_image.save(config.get('original_frames_directory') + file_name)
    image_without_background = remove(original_image)
    image_without_background.save(config.get('transparent_frames_directory') + file_name)

def get_frame_as_image(frame):
    return Image.fromarray(numpy.uint8(frame))

def get_number_of_digits(number):
    return len(str(abs(number)))

run()
