# charlist.py
"""List summary infor for the test files in the charset directory"""
# Copyright (c) 2008 Darcy Mason
# This file is part of pydicom, relased under an MIT license.
#    See the file license.txt included with this distribution, also
#    available at http://pydicom.googlecode.com

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(message)s')

if __name__ == "__main__":
    from glob import glob
    import dicom
    
    # Get list of all DICOM files
    names = glob("*.dcm")
    
    # Collect summary information from the files
    files_info = []
    for name in names:
        ds = dicom.ReadFile(name)
        files_info.append((name, ds.SpecificCharacterSet, ds.PatientsName))
    
    # Show the information
    format = "%-13s %-40s %-r" # r in Python >=2.0, uses repr()
    logging.info(format % ("Filename", "Character Sets", "Patient's Name"))
    logging.info(format % ("--------", "--------------", "--------------"))
    for file_info in files_info:
        logging.info(format % file_info)