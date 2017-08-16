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
# Addon:  Toms Classical Music Collection - My YouTube Add-on
# Author: Bromerzz

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
YOUTUBE_CHANNEL_ID_1 = "PL-IXdkJ4LY4khPG5tLx_1JSb2cfsU9mKq"
YOUTUBE_CHANNEL_ID_2 = "PL-IXdkJ4LY4lzDPcyv-lCjrCIR0hgIbFL"
YOUTUBE_CHANNEL_ID_3 = "PL-IXdkJ4LY4mbSNXjhVdm3weCw-Evf8rj"
YOUTUBE_CHANNEL_ID_4 = "PL-IXdkJ4LY4k_0zFylkrXAA3sTQ6cmVg-"
YOUTUBE_CHANNEL_ID_5 = "PL-IXdkJ4LY4lboFVpod8_3ajG58_X576-"
YOUTUBE_CHANNEL_ID_6 = "PL1mZeR4wTBoyFZMFCUsPqpgGO2tPd4eAe"
YOUTUBE_CHANNEL_ID_7 = "PLS6C4jHVZhO5xlfh8IZYzbgJaKZt8XNDZ"
YOUTUBE_CHANNEL_ID_8 = "PLS6C4jHVZhO6fV14M7M0kuSfIf5dqx5oz"
YOUTUBE_CHANNEL_ID_9 = "PLS6C4jHVZhO7mdvWazKgf3aHo4rryrnbW"
YOUTUBE_CHANNEL_ID_10 = "PL2788304DC59DBEB4"
YOUTUBE_CHANNEL_ID_11 = "PLc87N-d3x2CpUxoF7DRaHbCjFMbg286d3"
YOUTUBE_CHANNEL_ID_12 = "PLcGkkXtask_c_iDYwGpTkK0i--J8iafgH"
YOUTUBE_CHANNEL_ID_13 = "PL3E85427E7F6E6C28"
YOUTUBE_CHANNEL_ID_14 = "PL_qM1lclHDwUPGV9v5tJzTv1X5e8fAJRu"
YOUTUBE_CHANNEL_ID_15 = "ZeBljzppZsM"
YOUTUBE_CHANNEL_ID_16 = "4g4UZOedczs"
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
    
    #my_message= "{'title' : 'Support & Suggestions', 'msg' : \"If you come across any online content you'd like to get added please use the support thread at noobsandnerds.com and I'll be happy to look into it for you.\"}"
        # An example title/message we're going to send through to a popup dialog in the first Add_Dir item

# Add some YT Playlists (see we're using BASE as the url)
    Add_Dir( 
        name="Wagner Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="a")

    Add_Dir( 
        name="Schubert Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="a")

    Add_Dir( 
        name="Debussy Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="a")

    Add_Dir( 
        name="Karajan Legacy Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="a")
    
    Add_Dir( 
        name="Elgar Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="a")

    Add_Dir(
        name=" Variety of Composers", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="a")

    Add_Dir(
        name="Tchaikovsky Symphonies 1 to 5",url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="a")

    Add_Dir(
        name="Nielsen Symphonies",url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="a")

    Add_Dir(
        name="Brahms",url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="a")

    Add_Dir(
        name="Classical Short Clips",url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="a")

    Add_Dir(
        name="Just Instrumental",url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="a")

    Add_Dir(
        name="Bach and Debussy",url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="a")

    Add_Dir(
        name="Czech Composers Plus",url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="a")

    Add_Dir(
        name="Baroque Music ",url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="a")


        # Add some YT channels (see we're using BASE2 as the url for this one)
    Add_Dir( 
        name="Royal Philharmonic, The Symphonic Beatles", url=BASE3+YOUTUBE_CHANNEL_ID_15"/", folder=False,
        icon="a", mode='play_yt')

    Add_Dir( 
        name="Royal Philharmonic, Queen", url=BASE3+YOUTUBE_CHANNEL_ID_16"/", folder=False,
        con="a", mode='play_yt')

    #Add_Dir( 
        #name="", url=BASE2+YOUTUBE_CHANNEL_ID_+"/", folder=True,
        #icon="")
#----------------------------------------------------------------
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