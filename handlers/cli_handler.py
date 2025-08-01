import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate math takss from a setup file and opetionally open the results"
    )
    
    parser.add_argument(
        "--setup", "-s",
        type=str,
        required=True,
        help="Name of the JSON setup file (e.g., basic_operations.json)"
    )
    
    parser.add_argument(
        "--open", "-o",
        action="store_true",
        help="Open PDF file after creation"
    )
    
    parser.add_argument(
        "--file", "-f",
        action="store_true",
        help="Reveal PDF file in Finder"
    )
    
    return parser.parse_args()