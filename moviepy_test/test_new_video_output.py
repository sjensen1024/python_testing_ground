from moviepy import VideoFileClip, TextClip, CompositeVideoClip

clip = (
    VideoFileClip("test_input.mp4")
    .subclipped(1, 10)
    .with_volume_scaled(0.95)
)

txt_clip = TextClip(
    font="arial",
    text="This is a test.",
    font_size=50,
    color='white'
).with_duration(10).with_position('center')

final_video = CompositeVideoClip([clip, txt_clip])
final_video.write_videofile("test_output.mp4")