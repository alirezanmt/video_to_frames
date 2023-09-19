import cv2
import os
import logging
import sys
import argparse
import time


class VideoToFrames:
    """A class for breaking a video to it's frames."""

    def __init__(self, path=None, verbose=True ,image_format="jpg") -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.DEBUG)
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')
        handler_s = logging.StreamHandler(stream=sys.stdout)
        handler_s.setLevel(level=logging.DEBUG)
        handler_s.setFormatter(formatter)
        self.logger.addHandler(handler_s)

        self.verbose = verbose

        self.video_format_list = ["avi", "mp4", "mov", "flv", "wmv", "mkv"]
        self.image_format = image_format
        if image_format == None:
            self.image_format = "jpg"

        if path:
            self.base_dir = path
            if os.path.isdir(self.base_dir):
                self.video_names = []
                self.logger.debug("All videos:")
                for index, p in enumerate(os.listdir(self.base_dir)):
                    if os.path.isfile(os.path.join(self.base_dir, p)) and self._check_format(p):
                        self.video_names.append(os.path.join(self.base_dir, p))
                        self.logger.debug(f"{index}-  {p}")
            elif os.path.isfile(self.base_dir):
                self.video_names = [self.base_dir]
                self.logger.debug(f"Video: {os.path.basename(self.base_dir)}")
            else:
                self.logger.warning(f"'{self.base_dir}' is a wrong path!")
                exit()
        else:
            self.base_dir = os.getcwd()
            self.video_names = []
            self.logger.debug("All videos:")
            for index, p in enumerate(os.listdir(self.base_dir)):
                if os.path.isfile(os.path.join(self.base_dir, p)) and self._check_format(p):
                    self.video_names.append(os.path.join(self.base_dir, p))
                    self.logger.debug(f"{index}-  {p}") 

    def _check_format(self, file_name) -> bool:
        file_name = file_name.lower()
        file_format = file_name.split(".")[-1]
        for format in self.video_format_list:
            if format == file_format:
                return True
        return False

    def _make_folder(self, path) -> bool:
        try:
            os.mkdir(path)
            return True
        except:
            return False

    def run_breaking(self):
        self.logger.debug("Processing:")
        err = False
        for video_name in self.video_names:
            
            if self._make_folder(path=video_name[0:-4]):
                tic = time.process_time()
                self.logger.debug(f"Breaking {os.path.basename(video_name)} to frames...")
                cap = cv2.VideoCapture(video_name)
                if not cap.isOpened():
                    continue
                frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                counter = 1
                max_shift = len(str(frame_number))+1
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    try:
                        cv2.imwrite(f"{video_name[0:-4]}/_{counter}.{self.image_format}", frame)
                        if self.verbose:
                            print(f"({counter}".ljust(max_shift), f"/ {frame_number})", end="\r", flush=True)
                            counter += 1
                    except Exception as e:
                        self.logger.error(f"Can not save frames with format {self.image_format}.", exc_info=False)
                        err = True
                        break
                if self.verbose:
                    print(f"\nTotal time: {int((time.process_time()-tic)*1000)} ms", end="\n", flush=False)
                cap.release()
                cv2.destroyAllWindows()
                if err:
                    break
            else:
                self.logger.debug(f"There is a folder for {video_name} already.")
