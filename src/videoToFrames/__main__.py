# __main__.py

import argparse
import videoToFrames as vf
from videoToFrames.breaker import VideoToFrames

def main():
   
    parser = argparse.ArgumentParser(prog="videoToFrames", usage="Use %(prog)s with option --help", 
                                     add_help=False, conflict_handler="error")
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-p", "--path", action="store", type=str, 
                        help="Directory of video files. Default is current directory.")
    parser.add_argument("-f", "--format", action="store", type=str,
                        help="The format you want to save frames. Default is jpg.")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--version", action="version", version=f"{vf.__name__} {vf.__version__}")
    args = parser.parse_args()

    if args.help:
        print("\n\tVideo to frames:\n",
        "\n\t[-h], [--help]".ljust(25) , "Help instructions." ,
        "\n\t[-p], [--path]".ljust(25) , "Path of a directory or file. Default is current directory.",
        "\n\t[-f], [--format]".ljust(25), "The format you want to save frames. Default is jpg.",
        "\n\t[-v], [--verbose]".ljust(25), "Verbose mode.",
        "\n\t[--version]".ljust(25), "Version.")
        exit()
    
    obj = VideoToFrames(path=args.path, image_format=args.format, verbose=args.verbose)
    obj.run_breaking()

if __name__ == "__main__":
    main()