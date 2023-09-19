# Video To Frames

videoToFrames breaks a video to it's frames and save them in a folder.

## Installation

You can install the videoToFrames from [PyPI](https://pypi.org/project/video_to_frames/):

        python -m pip install video-to-frames

## How to use

video to frames is a command line application, named `videoToFrames`. To check it's command-line options:

        $ videoToFrames -h

To break all videos in a folder to frames:

        $ videoToFrames -p your_folder_path

To break a specified video:

        $ videoToFrames -p your_video_path

You can specify a format to save frames (default is `jpg`):

        $ videoToFrames -f png

To see time and number of frames:

        $ videoToFrames -v

To import to your program:

        >>> import videoToFrames
        >>> videoToFrames.__version__
        >>> from videoToFrames.breaker import VideoToFrames
        >>> obj = VideoToFrames(path="your_path", verbose=True, image_format="jpg")
        >>> obj.run_breaking()