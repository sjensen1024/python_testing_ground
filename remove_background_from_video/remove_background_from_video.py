from rembg import remove
from moviepy import VideoFileClip
from PIL import Image 
import numpy
import yaml

def run():
    config = setup_config()
    extract_frames_and_remove_backgrounds(
        config.get('input_file'), 
        config.get('original_frames_directory'), 
        config.get('output_file'), 
        config.get('transparent_frames_directory')
    )
    # TODO: Refactor and make the code do the following:
    #       1) Allow to optionally write both transparent and non-transparent versions instead of just transparent.
    #       2) Combine the frames into a result .mp4

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

def extract_frames_and_remove_backgrounds(input_video_path, original_frame_dir, output_video_path, transparent_frame_dir):
    original_video =  VideoFileClip(input_video_path) 
    count = 0
    for frame in original_video.iter_frames():
        count += 1
        #input_file_name = get_frame_file_name(count, original_video.n_frames, original_frame_dir)
        transparent_file_name = get_frame_file_name(count, original_video.n_frames, transparent_frame_dir)
        #current_time_in_seconds = count/original_video.fps
        #original_video.save_frame(frame_file_name, t = current_time_in_seconds)
        frame_as_image = Image.fromarray(numpy.uint8(frame))
        transparent_frame = remove(frame_as_image)
        transparent_frame.save(transparent_file_name)

def get_number_of_digits(number):
    return len(str(abs(number)))

def get_frame_file_name(current_frame, number_of_frames, output_directory):
    file_name = output_directory + '_'
    duration_digits = get_number_of_digits(number_of_frames)
    frame_digits = get_number_of_digits(current_frame)
    if duration_digits == frame_digits:
        return file_name + str(current_frame) + '.png'
    prefix = '0' * (duration_digits - frame_digits)
    return file_name + prefix + str(current_frame) + '.png'

run()
