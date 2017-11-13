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
#debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
#addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id

# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3 = "play/?video_id="



# Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "9rJoB7y6Ncs"
YOUTUBE_CHANNEL_ID_2 = "xtLoaMfinbU"
YOUTUBE_CHANNEL_ID_3 = "g6eA4PjWhws"
YOUTUBE_CHANNEL_ID_5 = "Oni4iY-b1sg"
YOUTUBE_CHANNEL_ID_6 = "0qmZaP9hg5M"
YOUTUBE_CHANNEL_ID_7 = "6DbjJJbEamQ"
YOUTUBE_CHANNEL_ID_8 = "KNkjaoZpOdI"
YOUTUBE_CHANNEL_ID_9 = "GD8IT91Xy90"
YOUTUBE_CHANNEL_ID_10 = "b8U8B9AA8YA"
YOUTUBE_CHANNEL_ID_11 = "HlFVT_eZh9Y"
YOUTUBE_CHANNEL_ID_12 = "kBwn_9T7Zes"
YOUTUBE_CHANNEL_ID_13 = "aO3-5Y9jc2E"
YOUTUBE_CHANNEL_ID_14 = "-hM0B70F1YM"
YOUTUBE_CHANNEL_ID_15 = "SX_hN3_vQyo"
YOUTUBE_CHANNEL_ID_16 = "l7_PXqcJPmg"
YOUTUBE_CHANNEL_ID_17 = "s9jbn27wIew"
YOUTUBE_CHANNEL_ID_18 = "Lydw07UQ5GM"


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
    Add_Dir(name="Tchaikovsky", url=' ', mode="tchaikovsky_menu", folder=True,)
    Add_Dir(name="Prokofiev", url=' ', mode="prokofiev_menu", folder=True,)
    Add_Dir(name="Khachaturian", url=' ', mode="khachaturian_menu", folder=True,)
    Add_Dir(name="Grieg", url=' ', mode="grieg_menu", folder=True,)
    Add_Dir(name="London Childrens Ballet", url=' ', mode="london_childrens_ballet_menu", folder=True,)



@route(mode='tchaikovsky_menu')
def Tchaikovsky_Menu():
    Add_Dir(name="Swan Lake, Kirov Ballet", url=BASE3+YOUTUBE_CHANNEL_ID_1, folder=False, mode='play_yt',)
    Add_Dir(name="Nutcracker Suite", url=BASE3+YOUTUBE_CHANNEL_ID_2, folder=False, mode='play_yt',)
    Add_Dir(name="Sleeping Beauty", url=BASE3+YOUTUBE_CHANNEL_ID_3, folder=False, mode='play_yt',)
    Add_Dir(name="Iolanta", url=BASE3+YOUTUBE_CHANNEL_ID_5, folder=False, mode='play_yt',)

@route(mode='prokofiev_menu')
def Prokofiev_Menu():
    Add_Dir(name="Romeo and Juliet, Nureyev, Orchestra de L'opera de Paris", url=BASE3+YOUTUBE_CHANNEL_ID_1, folder=False, mode='play_yt',)
    Add_Dir(name="Romeo and Juliet, La Scala Ballet", url=BASE3+YOUTUBE_CHANNEL_ID_15, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)

@route(mode='khachaturian_menu')
def Khachaturian_Menu():
    Add_Dir(name="Spartacus, Bolshoi Ballet", url=BASE3+YOUTUBE_CHANNEL_ID_16, folder=False, mode='play_yt',)
    Add_Dir(name="Gayanee, Armenian Ballet", url=BASE3+YOUTUBE_CHANNEL_ID_17, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)

@route(mode='grieg_menu')
def Grieg_Menu():
    Add_Dir(name="Peer Gynt, Santiago Municipal Theatre", url=BASE3+YOUTUBE_CHANNEL_ID_18, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)


@route(mode='london_childrens_ballet_menu')
def London_Childrens_Ballet_Menu():
    Add_Dir(name="A Little Princess", url=BASE3+YOUTUBE_CHANNEL_ID_6, folder=False, mode='play_yt',)
    Add_Dir(name="Rumpelstiltskin", url=BASE3+YOUTUBE_CHANNEL_ID_7, folder=False, mode='play_yt',)
    Add_Dir(name="The Secret Garden", url=BASE3+YOUTUBE_CHANNEL_ID_8, folder=False, mode='play_yt',)
    Add_Dir(name="Snow White", url=BASE3+YOUTUBE_CHANNEL_ID_9, folder=False, mode='play_yt',)
    Add_Dir(name="The Canterville Ghosts", url=BASE3+YOUTUBE_CHANNEL_ID_10, folder=False, mode='play_yt',)
    Add_Dir(name="Jane Eyre", url=BASE3+YOUTUBE_CHANNEL_ID_11, folder=False, mode='play_yt',)
    Add_Dir(name="Nanny McPhee Act 1 ", url=BASE3+YOUTUBE_CHANNEL_ID_12, folder=False, mode='play_yt',)
    Add_Dir(name="Nanny McPhee Act 2 ", url=BASE3+YOUTUBE_CHANNEL_ID_13, folder=False, mode='play_yt',)





#----------------------------------------------------------------
# Open add-on settings
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
@route(mode='play_yt', args=['url'])
def Play_YT(url):
    xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/%s)'%url)       

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