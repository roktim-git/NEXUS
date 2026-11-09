
import argparse
import platform
import os
from pypdf import PdfWriter

# to show system information
def system_info():

    print("Operating System:", platform.system())
    print("Architecture:", platform.machine())

# to merge pdf files in a directory
def pdf_merger(directory):

    merger = PdfWriter()

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            print("Processing:", filename, flush=True)
            merger.append(os.path.join(directory, filename))

    merger.write("final_merge.pdf")
    merger.close()

def main():
    parser = argparse.ArgumentParser(
        prog = "NEXUS",
        description = "Custom CLI Tool!"
    )
    
    subparsers = parser.add_subparsers(dest="subcommand")
    
    #system-info subcommand
    system_parser = subparsers.add_parser(
        "system",
        help="Show system information"
    )
    
    system_subparsers = system_parser.add_subparsers(
    dest="system_command"
    )
    
    system_subparsers.add_parser(
    "info",
    help="Show system information"
    )
    
    # pdf-merger subcommand
    pdf_parser = subparsers.add_parser(
        "pdf-merger",
        help="Merge PDF files in a directory"
    )
    
    pdf_parser_subparsers = pdf_parser.add_subparsers(
        dest="file_command"
    )
    
    merge_parser = pdf_parser_subparsers.add_parser(
        "merge",
        help="Merge PDF files"
    )
    merge_parser.add_argument(
        "merge_pdfs",
        type=str,
        help="Directory containing PDF files to merge"
    )
     

    args = parser.parse_args()

    if args.subcommand == "system" and args.system_command == "info":
        system_info()
    elif args.subcommand == "pdf-merger" and args.file_command == "merge":
        pdf_merger(args.merge_pdfs)
        
if __name__ == "__main__":
    main()
