from rembg import remove
import moviepy
from PIL import Image 
import numpy
import yaml
import os

def run():
    config = setup_config()
    remove_existing_outputs_if_should(config)
    original_video = moviepy.VideoFileClip(config.get('input_file')) 
    transparent_frame_images = extract_frames_and_remove_backgrounds(config, original_video)
    transparent_sequence = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(transparent_frame_images, int(original_video.fps))
    transparent_sequence.write_videofile(config.get('output_file'))
    # TODO: Refactor. This could be a LOT cleaner.

def setup_config():
    with open("./config.yml", 'r') as stream:
        config = yaml.safe_load(stream)
    return {
      'original_frames_directory': config.get('original_frames_directory'),
      'transparent_frames_directory': config.get('transparent_frames_directory'),
      'input_file': config.get('input_file'),
      'output_file': config.get('output_file'),
      'save_original_frames': config.get('save_original_frames'),
      'save_transparent_frames': config.get('save_transparent_frames'),
      'verbose_output': config.get('verbose_output')
    }

def remove_existing_outputs_if_should(config):
    print('Starting the process of removing existing output files based on what is in config.yml.')
    remove_current_output_file_if_exists(config)
    remove_original_frames_if_should(config)
    remove_transparent_frames_if_should(config)

def remove_current_output_file_if_exists(config):
    output_file = config.get('output_file')
    if not os.path.exists(output_file):
        print('The output file - ' + output_file + ' - does not exist. No need to remove it.')
        return
    os.remove(output_file)
    print('Output file ' + output_file + ' removed.')

def remove_original_frames_if_should(config):
    if not config.get('save_original_frames'):
        print('We are not saving original frames, so we will not delete the existing ones, if any.')
        return
    remove_files_from_directory_if_exists(config.get('original_frames_directory'))

def remove_transparent_frames_if_should(config):
    if not config.get('save_transparent_frames'):
        print('We are not saving transparent frames, so we will not delete the existing ones, if any.')
        return
    remove_files_from_directory_if_exists(config.get('transparent_frames_directory'))

def remove_files_from_directory_if_exists(directory):
    print('Deleting files in ' + directory)
    if not os.path.exists(directory):
        print('Directory does not exist. Nothing to delete here.')
        return
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print(file_name + ' deleted.')
    
def extract_frames_and_remove_backgrounds(config, original_video):
    count = 0
    transparent_frame_images = []
    for frame in original_video.iter_frames():
        count += 1
        frame_file_name = get_frame_file_name(count, original_video.n_frames)
        original_image = get_frame_as_image(frame)
        save_original_image_if_should(original_image, config, config.get('original_frames_directory') + frame_file_name)
        image_without_background = remove(original_image)
        save_transparent_image_if_should(image_without_background, config, config.get('transparent_frames_directory') + frame_file_name)
        transparent_frame_images.append(numpy.array(image_without_background))
        print('Finished processing frame ' + str(count) + ' of ' + str(original_video.n_frames))
    return transparent_frame_images


def get_frame_file_name(current_frame, number_of_frames):
    file_name = '_'
    duration_digits = get_number_of_digits(number_of_frames)
    frame_digits = get_number_of_digits(current_frame)
    if duration_digits == frame_digits:
        return file_name + str(current_frame) + '.png'
    prefix = '0' * (duration_digits - frame_digits)
    return file_name + prefix + str(current_frame) + '.png'

def get_frame_as_image(frame):
    return Image.fromarray(numpy.uint8(frame))

def get_number_of_digits(number):
    return len(str(abs(number)))

def save_original_image_if_should(image, config, save_path):
    if config.get('save_original_frames'):
        image.save(save_path)
        print('Saved original frame as ' + save_path)

def save_transparent_image_if_should(image, config, save_path):
    if config.get('save_transparent_frames'):
        image.save(save_path)
        print('Saved transparent frame as ' + save_path)

run()
