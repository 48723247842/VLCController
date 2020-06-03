from vlc_controller import VLCController
import time
from pprint import pprint

if __name__ == "__main__":
	vlc = VLCController()
	print( f"Connected = {vlc.connected}" )
	vlc.add("/media/187A29A07A297B9E/MEDIA_MANAGER/TVShows/TrailerParkBoys/12/Trailer.Park.Boys.S12E02.Godspeed.My.Muscular.Friend.1080p.NF.WEB-DL.DD5.1.H264-SiGMA.mkv")
	time.sleep( 3 )
	pprint( vlc.get_common_info() )