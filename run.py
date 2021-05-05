from lure import select_lure, play_lure
from record import filename, record
from pixel_ring import pixel_ring
from upload import upload_recording


def main():
    # Run program every hour
    pixel_ring.spin() # Set pixel_ring.brightness(0x00) for field testing
    # Select an audio lure
    lure_dir, lure_index = select_lure('bird', 'distress') # Can remove if lure player not required

    # Play audio lure
    play_lure(lure_dir) # Can remove if lure player not required

    # Record for 60 seconds (currently 5 sec) and upload data
    pixel_ring.listen()
    
    FILENAME, FILENAME_DATA = filename('location', lure_index)
    DOA = record(FILENAME, FILENAME_DATA)
    
    # change filename to FILENAME
    upload_recording(_filename, DOA)

main()