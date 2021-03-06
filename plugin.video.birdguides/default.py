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
YOUTUBE_CHANNEL_ID_1 = "PLE3B611F475AA00AF"
YOUTUBE_CHANNEL_ID_2 = "PL852BE01ADF00B358"
YOUTUBE_CHANNEL_ID_3 = "PLBFD1CF77548B0291"
YOUTUBE_CHANNEL_ID_4 = "PL4F31319F0022ECF8"
YOUTUBE_CHANNEL_ID_5 = "PLgSpqOFj1Ta6oK7v-UJSGDlsYp1eJwTxu"
YOUTUBE_CHANNEL_ID_6 = "PLE02AF25046CE2E69"
YOUTUBE_CHANNEL_ID_7 = "3nYgs69Q9FQ"
YOUTUBE_CHANNEL_ID_8 = "ABJxTvC_jao"





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
    my_message= "{'title' : 'Thankyou for watching - please read this first', 'msg' : \"The content on here has been pulled from freely available YouTube Videos produced by birding organisations such as the British Trust for Ornithology and Petersens Field Guides. As I include additional content from Youtube I would like to record in advance my appreciation for the work those individuals and organisations will have put into their projects.\"}"

    Add_Dir(
        name="Thankyou for watching - please read this first", url=my_message, mode="simple_dialog", folder=False,
        icon="https://cdn2.iconfinder.com/data/icons/picons-basic-2/57/basic2-087_info-512.png")
        
# Add some YT Playlists (see we're using BASE as the url)
    Add_Dir(name="Bird ID Workshops", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,)
    Add_Dir(name="Peterson Field Guides:Identyfing Birds By Family", url=BASE+YOUTUBE_CHANNEL_ID_2+"/",folder=True,)
    Add_Dir(name="Peterson Field Guides:Species Profiles", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,)
    Add_Dir(name="Peterson Field Guides:Birding Tutorials", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,)
    Add_Dir(name="Cornell lab of Ornithology: The 39 Species of The Birds of Paradise", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,)
    Add_Dir(name="Cornell lab of Ornithology: The World of Birds", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,)
    Add_Dir(name="National Geographic Guide to Birding in N America", url=BASE3+YOUTUBE_CHANNEL_ID_7, folder=False, mode='play_yt',)
    Add_Dir(name="Audobon Society Guide to Birds of N America, Vol 3", url=BASE3+YOUTUBE_CHANNEL_ID_8, folder=False, mode='play_yt',)




    #BASE2 for channel lists
    #Add_Dir(name="whatever", url=BASE2+YOUTUBE_CHANNEL_ID_99+"/", folder=True,)
    #BASE3 for watch or play tv 
    #Add_Dir(name="whatever", url=BASE3+YOUTUBE_CHANNEL_ID_99, folder=False, mode='play_yt',)


    #To add a dircetory in which to add links create a route menu
#@route(mode='round_the_world_menu')
#def Round_The_World_Menu():


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