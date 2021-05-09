from record import filename, record
from upload import upload_recording


def main():
   
    FILENAME, FILENAME_DATA = filename('location', 'lure_index')
    DOA = record(FILENAME, FILENAME_DATA)
    
    # change filename to FILENAME
    upload_recording(FILENAME, DOA)

main()