from rembg import remove
from moviepy import VideoFileClip
from PIL import Image 

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

def extract_original_frames_as_png(input_video_path, original_frame_dir):
    original_video =  VideoFileClip(input_video_path) 
    count = 0
    for frame in original_video.iter_frames():
        count += 1
        frame_file_name = get_frame_file_name(count, original_video.n_frames, original_frame_dir)
        current_time_in_seconds = count/original_video.fps
        original_video.save_frame(frame_file_name, t = current_time_in_seconds)

def run():
    input_video_path =  'test_input.mp4' 
    output_video_path = 'test_output.mp4' 
    original_frame_dir = './original_frames/'
    transparent_frame_dir = './transparent_frames/'
    extract_original_frames_as_png(input_video_path, original_frame_dir)
    # TODO: Implement the removal of the background of each extracted image.

run()
