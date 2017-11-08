# -*- coding: utf-8 -*-

""" ^ SECTION 1:
    This should be at the top of your code to declare the type of text
    format you're using. Without this you may find some text editors save
    it in an incompatible format and this can make bug tracking extremely
    confusing! More info here: https://www.python.org/dev/peps/pep-0263/
"""

#----------------------------------------------------------------

"""
    SECTION 2:
    This is where you'd put your license details, the GPL3 license 
    is the most common to use as it makes it easy for others to fork
    and improve upon your code. If you're re-using others code ALWAYS
    check the license first, removal of licenses is NOT allowed and you
    generally have to keep to the same license used in the original work
    (check license details as some do differ).

    Although not all licenses require it (some do, some don't),
    you should always give credit to the original author(s). Someone may have spent
    months if not years on the code so really it's the very least you can do if
    you choose to use their work as a base for your own.
"""
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: My YouTube Add-on
# Author: Add your name here

#----------------------------------------------------------------

"""
    SECTION 3:
    This is your global imports, any modules you need to import code from
    are added here. You'll see a handful of the more common imports below.
"""
import os           # access operating system commands
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)

# The following are often used, we are not using them in this particular file so they are commented out

# import re           # allows use of regex commands, if you're intending on scraping you'll need this
# import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

#------------------------------------------------------------

"""
    SECTION 4:
    These are our global variables, anything we set here can be accessed by any of
    our functions later on. Please bare in mind though that if you change the value
    of a global variable from inside a function the value will revert back to the
    value set here once that function has completed.
"""
debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id

# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3 = "play/?video_id="

# Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "JdgjIebwD_0"
YOUTUBE_CHANNEL_ID_2 = "ZuasCv8b7UQ"
YOUTUBE_CHANNEL_ID_3 = "HNt1Ccg3y5Q"
YOUTUBE_CHANNEL_ID_4 = "Ti5-wah4eBA"
YOUTUBE_CHANNEL_ID_5 = "9eoTPxCcyHM"
YOUTUBE_CHANNEL_ID_6 = "yofu093bPkw"
YOUTUBE_CHANNEL_ID_7 = "HUrMrXbJIQk"
YOUTUBE_CHANNEL_ID_8 = "wixRxZ94dMc"
YOUTUBE_CHANNEL_ID_9 = "Epz4nJ9ut0I"
YOUTUBE_CHANNEL_ID_10 = "Rerxw9vloo"
YOUTUBE_CHANNEL_ID_11 = "MBEfujzRrh8"
YOUTUBE_CHANNEL_ID_12 = "CQEH3cbw5Yw"
YOUTUBE_CHANNEL_ID_13 = "Vft1EGTCFbw"
YOUTUBE_CHANNEL_ID_14 = "qi1p0yh4X3I"
YOUTUBE_CHANNEL_ID_15 = "klya9oEK57M"
YOUTUBE_CHANNEL_ID_16 ="SUN_AviJzZ4"
YOUTUBE_CHANNEL_ID_17 = "ns0yg90Ap3M"
YOUTUBE_CHANNEL_ID_18 = "WFlSCVOYi8"
YOUTUBE_CHANNEL_ID_19 = "Up_Oq_graC0"
YOUTUBE_CHANNEL_ID_20 = "ifZaUkXmIcY"
YOUTUBE_CHANNEL_ID_21 = "7Jo83LevWeE"
YOUTUBE_CHANNEL_ID_22 = "wJq76iri2CE"
YOUTUBE_CHANNEL_ID_23 = "86Gw16OuMTM"
YOUTUBE_CHANNEL_ID_24 = "29f3i-XXDuU"
YOUTUBE_CHANNEL_ID_25 = "AoX_qkXQi94"
YOUTUBE_CHANNEL_ID_26 = "V3eiuj37gJE"
YOUTUBE_CHANNEL_ID_27 = "Vm8c0mnhIRY"
YOUTUBE_CHANNEL_ID_28 = "vt8ZK8fI3W8"
YOUTUBE_CHANNEL_ID_29 = "4URaexb9uDw"
YOUTUBE_CHANNEL_ID_30 = "Ju1j5cxB9pg&t=39s"
YOUTUBE_CHANNEL_ID_31 = "EbWyHc7GDjY"
YOUTUBE_CHANNEL_ID_32 = "8pyW1hftvk4"
YOUTUBE_CHANNEL_ID_33 = "CHh1swq_BOs"
YOUTUBE_CHANNEL_ID_34 = "Yh2XTAiVXJs"
YOUTUBE_CHANNEL_ID_35 = "PU3hnwumbqg"
YOUTUBE_CHANNEL_ID_36 = "ZcH052nY7II"
YOUTUBE_CHANNEL_ID_37 = "kZyMuqV-l9Y"
YOUTUBE_CHANNEL_ID_38 = "ecJSoImIT2Y"
YOUTUBE_CHANNEL_ID_39 = "xYWF3raGwx4"
YOUTUBE_CHANNEL_ID_40 = "rjjNnfZn2mA"
YOUTUBE_CHANNEL_ID_41 = "puZId8bfAXU"
YOUTUBE_CHANNEL_ID_42 = "Petrels"
YOUTUBE_CHANNEL_ID_43 = "6SDxOy-F3gs"
YOUTUBE_CHANNEL_ID_44 = "bn6YN5Mb7mU"
YOUTUBE_CHANNEL_ID_45 = "yd30BlNsmeA"
YOUTUBE_CHANNEL_ID_46 = "I5TtiYKO9aI&t=14s"
YOUTUBE_CHANNEL_ID_47 = "KVhkl6rd6T4"
YOUTUBE_CHANNEL_ID_48 = "2wa0nFf9iug&spfreload=10"
YOUTUBE_CHANNEL_ID_49 = "PiqVkmqCOc0"
YOUTUBE_CHANNEL_ID_50 = "PZjAyurw_RQ"
YOUTUBE_CHANNEL_ID_51 = "S8K2rSlDaKU"
YOUTUBE_CHANNEL_ID_52 = "C5oN4Pc9Gw4"
YOUTUBE_CHANNEL_ID_53 = "zT5BYd3oj_Y&t=67s"
#YOUTUBE_CHANNEL_ID_54 = ""
#YOUTUBE_CHANNEL_ID_55 = ""




#----------------------------------------------------------------

"""
    SECTION 5:
    Add our custom functions in here, it's VERY important these go in this section
    as the code in section 6 relies on these functions. If that code tries to run
    before these functions are declared the add-on will fail.

    You'll notice each function in here has a decorator above it (an @route() line of code),
    this assigns a mode to the function so it can be called with Add_Dir and it also tells
    the code what paramaters to send through. For example you'll notice the Main_Menu() function
    we've assigned to the mode "main" - this means if we ever want to get Add_Dir to open that
    function we just use the mode "main". This particular function does not require any extra
    params to be sent through but if you look at the Simple_Dialog() function you'll see we send through
    2 different paramaters (title and msg), if you look at the Add_Dir function in Main_Menu()
    on line 106 you'll see we've sent these through as a dictionary. Using that same format you can send
    through as many different params as you wish.
"""

#----------------------------------------------------------------
# This is the main menu we open into
@route(mode='main_menu')
def Main_Menu():

# If debug mode is enabled show the koding tutorials
    #if debug == 'true':
        #Add_Dir ( '[COLOR=lime]Koding Tutorials[/COLOR]', '', "tutorials", True, '', '', '' )
    #else:
        #Add_Dir ( '[COLOR=lime]Enable debug mode for some cool dev tools![/COLOR]', '', "koding_settings", False, '', '', '' )
    
# An example title/message we're going to send through to a popup dialog in the first Add_Dir item
    my_message= "{'title' : 'Support & Suggestions', 'msg' : \"If you come across any online content you'd like to get added please use the support thread at noobsandnerds.com and I'll be happy to look into it for you.\"}"

    Add_Dir(
        name="Support/Suggestions", url=my_message, mode="simple_dialog", folder=False,
        icon="https://cdn2.iconfinder.com/data/icons/picons-basic-2/57/basic2-087_info-512.png")
        
# Add some YT Playlists (see we're using BASE as the url)
    Add_Dir(name="Chaffinch and Brambling", url=BASE3+YOUTUBE_CHANNEL_ID_1, folder=False, mode='play_yt',)
    Add_Dir(name="Green Finches", url=BASE3+YOUTUBE_CHANNEL_ID_2, folder=False, mode='play_yt',)
    Add_Dir(name="Linnet and Twite", url=BASE3+YOUTUBE_CHANNEL_ID_3, folder=False, mode='play_yt',)
    Add_Dir(name="Meadow Pipit, Tree Pipit and Skylark", url=BASE3+YOUTUBE_CHANNEL_ID_4, folder=False, mode='play_yt',)
    Add_Dir(name="Rock Pipit and Water Pipit", url=BASE3+YOUTUBE_CHANNEL_ID_5, folder=False, mode='play_yt',)
    Add_Dir(name="Goldcrest and Firecrest", url=BASE3+YOUTUBE_CHANNEL_ID_6, folder=False, mode='play_yt',)
    Add_Dir(name="Marsh and Willow Tits", url=BASE3+YOUTUBE_CHANNEL_ID_7, folder=False, mode='play_yt',)
    Add_Dir(name="Chiffchaff and Willow Warbler", url=BASE3+YOUTUBE_CHANNEL_ID_8, folder=False, mode='play_yt',)
    Add_Dir(name="Reed Warbler and Sedge Warbler", url=BASE3+YOUTUBE_CHANNEL_ID_9, folder=False, mode='play_yt',)
    Add_Dir(name="Whitethroat and Lesser Whitehroat", url=BASE3+YOUTUBE_CHANNEL_ID_10, folder=False, mode='play_yt',)
    Add_Dir(name="Blackcap and Garden Warbler", url=BASE3+YOUTUBE_CHANNEL_ID_11, folder=False, mode='play_yt',)
    Add_Dir(name="Pigeons", url=BASE3+YOUTUBE_CHANNEL_ID_12, folder=False, mode='play_yt',)
    Add_Dir(name="Collared Dove and Turtle Dove", url=BASE3+YOUTUBE_CHANNEL_ID_13, folder=False, mode='play_yt',)
    Add_Dir(name="Crow, Rook and Raven", url=BASE3+YOUTUBE_CHANNEL_ID_14, folder=False, mode='play_yt',)    #Add_Dir( 
    Add_Dir(name="Hirendines and Swifts", url=BASE3+YOUTUBE_CHANNEL_ID_15, folder=False, mode='play_yt',)
    Add_Dir(name="Nigthingales", url=BASE3+YOUTUBE_CHANNEL_ID_16, folder=False, mode='play_yt',)
    Add_Dir(name="Mandarin and Wood Ducks", url=BASE3+YOUTUBE_CHANNEL_ID_17, folder=False, mode='play_yt',)
    Add_Dir(name="Female Dabbling ducks", url=BASE3+YOUTUBE_CHANNEL_ID_18, folder=False, mode='play_yt',)
    Add_Dir(name="Garganey and Teal", url=BASE3+YOUTUBE_CHANNEL_ID_19, folder=False, mode='play_yt',)
    Add_Dir(name="Diving Ducks", url=BASE3+YOUTUBE_CHANNEL_ID_20, folder=False, mode='play_yt',)
    Add_Dir(name="Goosander and Red Breasted Merganser", url=BASE3+YOUTUBE_CHANNEL_ID_21, folder=False, mode='play_yt',)
    Add_Dir(name="Winter Grebes", url=BASE3+YOUTUBE_CHANNEL_ID_22, folder=False, mode='play_yt',)
    Add_Dir(name="Small Breeding Grebes", url=BASE3+YOUTUBE_CHANNEL_ID_23, folder=False, mode='play_yt',)
    Add_Dir(name="Winter Divers", url=BASE3+YOUTUBE_CHANNEL_ID_24, folder=False, mode='play_yt',)
    Add_Dir(name="Scoters", url=BASE3+YOUTUBE_CHANNEL_ID_25, folder=False, mode='play_yt',)
    Add_Dir(name="Sanderling and Curlew Sandpiper", url=BASE3+YOUTUBE_CHANNEL_ID_26, folder=False, mode='play_yt',)
    Add_Dir(name="Wood and Green Sandpiper", url=BASE3+YOUTUBE_CHANNEL_ID_27, folder=False, mode='play_yt',)
    Add_Dir(name="Curlew and Whimbrel", url=BASE3+YOUTUBE_CHANNEL_ID_28, folder=False, mode='play_yt',)
    Add_Dir(name="Knot and Dunlin", url=BASE3+YOUTUBE_CHANNEL_ID_29, folder=False, mode='play_yt',)
    Add_Dir(name="Common Shanks", url=BASE3+YOUTUBE_CHANNEL_ID_30, folder=False, mode='play_yt',)
    Add_Dir(name="Coot and Moorhen", url=BASE3+YOUTUBE_CHANNEL_ID_31, folder=False, mode='play_yt',)
    Add_Dir(name="Wild Swans", url=BASE3+YOUTUBE_CHANNEL_ID_32, folder=False, mode='play_yt',)
    Add_Dir(name="Grey Geese", url=BASE3+YOUTUBE_CHANNEL_ID_33, folder=False, mode='play_yt',)
    Add_Dir(name="Kittiwake and Other Small Gulls", url=BASE3+YOUTUBE_CHANNEL_ID_34, folder=False, mode='play_yt',)
    Add_Dir(name="Small black headed gulls", url=BASE3+YOUTUBE_CHANNEL_ID_35, folder=False, mode='play_yt',)
    Add_Dir(name="Iceland and Glaucous Gulls", url=BASE3+YOUTUBE_CHANNEL_ID_36, folder=False, mode='play_yt',)
    Add_Dir(name="Adult black backed gulls", url=BASE3+YOUTUBE_CHANNEL_ID_37, folder=False, mode='play_yt',)
    Add_Dir(name="Godwits", url=BASE3+YOUTUBE_CHANNEL_ID_38, folder=False, mode='play_yt',)
    Add_Dir(name="Grey and Golden Plovers", url=BASE3+YOUTUBE_CHANNEL_ID_39, folder=False, mode='play_yt',)
    Add_Dir(name="Ringed Plovers", url=BASE3+YOUTUBE_CHANNEL_ID_40, folder=False, mode='play_yt',)
    Add_Dir(name="Winter Auks", url=BASE3+YOUTUBE_CHANNEL_ID_41, folder=False, mode='play_yt',)
    Add_Dir(name="Petrels", url=BASE3+YOUTUBE_CHANNEL_ID_42, folder=False, mode='play_yt',)
    Add_Dir(name="Skuas", url=BASE3+YOUTUBE_CHANNEL_ID_43, folder=False, mode='play_yt',)
    Add_Dir(name="Little Egret and Great White Egret", url=BASE3+YOUTUBE_CHANNEL_ID_44, folder=False, mode='play_yt',)
    Add_Dir(name="Roseate, Sandwich and Little Tern", url=BASE3+YOUTUBE_CHANNEL_ID_45, folder=False, mode='play_yt',)
    Add_Dir(name="Common and Arctic Terns", url=BASE3+YOUTUBE_CHANNEL_ID_46, folder=False, mode='play_yt',)
    Add_Dir(name="Hobby and Kestrel", url=BASE3+YOUTUBE_CHANNEL_ID_47, folder=False, mode='play_yt',)
    Add_Dir(name="Grey Harriers", url=BASE3+YOUTUBE_CHANNEL_ID_48, folder=False, mode='play_yt',)
    Add_Dir(name="Peregrines", url=BASE3+YOUTUBE_CHANNEL_ID_49, folder=False, mode='play_yt',)
    Add_Dir(name="Eagles", url=BASE3+YOUTUBE_CHANNEL_ID_50, folder=False, mode='play_yt',)
    Add_Dir(name="Winter Buzzards: Common and Rough Legged Buzzards", url=BASE3+YOUTUBE_CHANNEL_ID_51, folder=False, mode='play_yt',)
    Add_Dir(name="Summer Buzzards: Common and Honey Buzzards", url=BASE3+YOUTUBE_CHANNEL_ID_52, folder=False, mode='play_yt',)
    Add_Dir(name="Goshawk and Sparrowhawk", url=BASE3+YOUTUBE_CHANNEL_ID_53, folder=False, mode='play_yt',)




# A basic OK Dialog
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#----------------------------------------------------------------
# Play a youtube video
@route(mode='play_yt',args=['url'])
def Play_YT(url):
    xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/%s)'%url)

"""
    SECTION 6:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this. In the run command you need to set default to
    whatever route you want to open into, in this example the 'main_menu' route which opens the
    Main_Menu() function up at the top.
"""
if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))