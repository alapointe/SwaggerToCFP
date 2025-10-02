import argparse
import logging

# class Logger():
#     def __init__(self):
#         self.args = None  # Placeholder for parsed arguments

#     def setup_argparse(self):
#         parser = argparse.ArgumentParser(
#             description="Description of your application."
#         )
#         parser.add_argument(
#             "--input",
#             type=str,
#             required=False,
#             help="Path to the input file."
#         )
#         parser.add_argument(
#             "--output",
#             type=str,
#             required=False,
#             default="output.txt",
#             help="Path to the output file (default: output.txt)."
#         )
#         parser.add_argument(
#             "--verbose",
#             action="store_true",
#             help="Enable verbose mode."
#         )
        
#         # Parse arguments and store them in the instance variable
#         self.args = parser.parse_args()

#     def run(self):
#         if self.args.verbose:
#             print("Verbose mode enabled.")
#             logger = logging.getLogger("logger")
#             logger.setLevel("DEBUG")




class Logger:
    def __init__(self):
        self.args = None  # Placeholder for parsed arguments

    def setup_argparse(self):
        parser = argparse.ArgumentParser(
            description="Description of your application."
        )
        parser.add_argument(
            "--input",
            type=str,
            required=False,
            help="Path to the input file."
        )
        parser.add_argument(
            "--output",
            type=str,
            required=False,
            default="output.txt",
            help="Path to the output file (default: output.txt)."
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Enable verbose mode."
        )
        
        # Parse arguments and store them in the instance variable
        self.args = parser.parse_args()

    def run(self):
        if self.args.verbose:
            print("Verbose mode enabled.")
            logger = logging.getLogger("logger")
            logger.setLevel(logging.DEBUG)
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.addHandler(ch)
            return logger
        else:
            logger = logging.getLogger("logger")
            logger.setLevel(logging.WARNING)
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.addHandler(ch)
            return logger
        