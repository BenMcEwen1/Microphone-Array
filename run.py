from lure import select_lure, play_lure
from record import filename, record
from pixel_ring import pixel_ring

def main():
    # Run program every hour
    pixel_ring.spin()
    # Select an audio lure
    lure_dir, lure_index = select_lure('bird', 'distress')

    # Play audio lure
    play_lure(lure_dir)

    # Record for 60 seconds (currently 5 sec) and upload data
    pixel_ring.listen()
    FILENAME, FILENAME_DATA = filename('location', lure_index)
    record(FILENAME, FILENAME_DATA)

    # Reset timer

main()