import os
from moviepy.editor import *
import random


input_path = "input"
file_names = os.listdir(input_path)
print(file_names)
clips = []
for name in file_names:
    if random.choice([True, True, False]):
        clips.append(VideoFileClip("input/" + name))

# Create a base clip with black background
base_clip = ColorClip(size=(1080, 1920), color=(0,0,0), duration=max(clip.duration for clip in clips))

# Function to generate random position
def random_position(clip, base_size):
    center_x = base_size[0] // 2
    center_y = base_size[1] // 2
    x = random.randint(max(0, center_x - 150 - clip.w//2), min(base_size[0] - clip.w, center_x + 150 - clip.w//2))
    y = random.randint(max(0, center_y - 200 - clip.h//2), min(base_size[1] - clip.h, center_y + 200 - clip.h//2))
    return lambda t: (x, y)

# Function to apply a random filter
def random_filter(clip):
    filters = [
        lambda c: c.fx(vfx.colorx, 1.5),  # Increase brightness
        lambda c: c.fx(vfx.invert_colors),  # Invert colors
        lambda c: c.fx(vfx.blackwhite),  # Black and white
        lambda c: c.fx(vfx.mirror_x),  # Mirror horizontally
        lambda c: c.fx(vfx.mirror_y),  # Mirror vertically
    ]
    return random.choice(filters)(clip)

# Add clips at random times and positions with random filters
video_clips = []
for clip in clips:
    start_time = random.uniform(0, base_clip.duration - clip.duration)
    pos = random_position(clip, base_clip.size)
    
    # Apply random filter for a random duration
    filter_start = random.uniform(0, clip.duration)
    filter_duration = random.uniform(0, clip.duration - filter_start)
    
    filtered_clip = clip.subclip(filter_start, filter_start + filter_duration)
    filtered_clip = random_filter(filtered_clip)
    
    # Combine the original and filtered parts
    final_clip = CompositeVideoClip([
        clip,
        filtered_clip.set_start(filter_start)
    ]).set_duration(clip.duration)
    
    video_clips.append(final_clip.set_start(start_time).set_position(pos))

# Create the final composite video
video = CompositeVideoClip([base_clip] + video_clips)

video.write_videofile("output.mp4", codec="libx264")
