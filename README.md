# Video To Frames

videoToFrames breaks a video to it's frames and saves them in a folder.

## Installation

You can install the videoToFrames from [PyPI](https://pypi.org/project/break-video-to-frames/):

        python -m pip install break-video-to-frames

## How to use

video to frames is a command line application, named `videoToFrames`. To check it's command-line options:

        $ python -m videoToFrames -h

To break all videos in a folder to frames:

        $ python -m videoToFrames -p your_folder_path

To break a specified video:

        $ python -m videoToFrames -p your_video_path

You can specify a format to save frames (default is `jpg`):

        $ python -m videoToFrames -f png

To see time and number of frames:

        $ python -m videoToFrames -v

To import to your program:

        >>> import videoToFrames
        >>> videoToFrames.__version__
        >>> from videoToFrames.breaker import VideoToFrames
        >>> obj = VideoToFrames(path="your_path", verbose=True, image_format="jpg")
        >>> obj.run_breaking()