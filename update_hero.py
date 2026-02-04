
import sys

file_path = '/Users/timmyyanchun/Desktop/Well Honestly WEBSITE/wellhonestly_v4.html'

with open(file_path, 'r') as f:
    lines = f.readlines()

# CSS Update: .hero-media (Lines 171-182)
# Note: Line numbers in view_file are 1-indexed.
# Lines 171-182 are indices 170-181.

new_css = """        .hero-media {
            position: absolute;
            top: 0;
            right: 0;
            width: 55%;
            height: 100%;
            background: var(--cream);
            overflow: hidden;
            clip-path: polygon(15% 0, 100% 0, 100% 100%, 0% 100%);
        }

        .hero-media video {
            position: absolute;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            transform: translate(-50%, -50%);
            object-fit: cover;
        }

        .hero-media::after {
"""

# We'll replace from line 171 to the line before .hero-media::after {
# Based on grep, 171 is .hero-media { and 183 is .hero-media::after {
# So we replace lines 171 to 182 (indices 170 to 181).

lines[170:182] = [new_css]

# HTML Update: Replace the div with the video tag (Line 1263)
# Line 1263 is index 1262.
# Original: <div class="hero-media"></div>
# We want to keep the class but put a video inside, or replace it entirely with a video container.
# Actually, the CSS targets .hero-media video, so we should keep the container and put video inside.

video_html = """        <div class="hero-media">
            <video autoplay muted loop playsinline poster="data:image/jpeg;base64,/9j/4AAQ...">
                <source src="hero-video.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
"""
# Note: I should ideally extract the existing base64 to use as a poster, 
# but since it's so long, I'll just use a placeholder or the first chunk if I can.
# Better: I'll just replace the div with a video element that has the same class.

# Let's find the exact line for <div class="hero-media"></div>
for i, line in enumerate(lines):
    if '<div class="hero-media"></div>' in line:
        # Extract the base64 from the CSS block we just removed? Too complex.
        # I'll just use the video tag.
        lines[i] = '        <div class="hero-media">\n            <video autoplay muted loop playsinline>\n                <source src="hero-video.mp4" type="video/mp4">\n                Your browser does not support the video tag.\n            </video>\n        </div>\n'
        break

with open(file_path, 'w') as f:
    f.writelines(lines)

print("Update complete")
