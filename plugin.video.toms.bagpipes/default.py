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
YOUTUBE_CHANNEL_ID_1 = "bsbu4_A5BuU"
YOUTUBE_CHANNEL_ID_2 = "oBYVmnMFMtA"
YOUTUBE_CHANNEL_ID_3 = "OhI3_FABzVI"
YOUTUBE_CHANNEL_ID_4 = "KuQ7JpL2eCc"
YOUTUBE_CHANNEL_ID_5 = "kJTuRfAo2eU"
YOUTUBE_CHANNEL_ID_6 = "RBHJJ8-rVfoYO"
YOUTUBE_CHANNEL_ID_7 = "lL45xrqEbL8"
#YOUTUBE_CHANNEL_ID_8 = "mlypMpQ5X7A"
YOUTUBE_CHANNEL_ID_9 = "6Y5mcLxlSgU"
YOUTUBE_CHANNEL_ID_10 = "P2gDkcpYnMc&t"
YOUTUBE_CHANNEL_ID_11 = "RDQut2getKFT4"
#YOUTUBE_CHANNEL_ID_12 = "8DohLjFAuLk"
YOUTUBE_CHANNEL_ID_13 = "4BNE_Z_EDgE"
YOUTUBE_CHANNEL_ID_14 = "wR6D7744cgk"
YOUTUBE_CHANNEL_ID_15 = "RsxjXArvdXU"
YOUTUBE_CHANNEL_ID_16 = "Qut2getKFT4"
YOUTUBE_CHANNEL_ID_17 = "hCtBXLWkTMM"
YOUTUBE_CHANNEL_ID_18 = "2h4xyq-ChCc"
YOUTUBE_CHANNEL_ID_19 = "e82budbYTlE&t=93s"
YOUTUBE_CHANNEL_ID_20 = "tgso9Sk2B6U"
YOUTUBE_CHANNEL_ID_21 = "cjDXWPW9f9s"
YOUTUBE_CHANNEL_ID_22 = "_1JsSckijLE"
YOUTUBE_CHANNEL_ID_23 = "lIFamj22RqU"
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


    Add_Dir(name="Edinburgh Military Tattoo", url=' ', mode="edinburgh_military_tattoo_menu", folder=True,)
    Add_Dir(name="Regimental Bands", url=' ', mode="regimental_bands_menu", folder=True,)
    Add_Dir(name="Other Military Tattoos", url=' ', mode="other_military_tattoos_menu", folder=True,) 
    Add_Dir(name="General Piping Content", url=' ', mode="general_piping_content_menu", folder=True,)
    Add_Dir(name="Gurkha Pipes and Drums", url=' ', mode="gurkha_pipes_and_drums_menu", folder=True,)


# If debug mode is enabled show the koding tutorials
   #if debug == 'true':
        #Add_Dir ( '[COLOR=lime]Koding Tutorials[/COLOR]', '', "tutorials", True, '', '', '' )
    #else:
        #Add_Dir ( '[COLOR=lime]Enable debug mode for some cool dev tools![/COLOR]', '', "koding_settings", False, '', '', '' )
    
# An example title/message we're going to send through to a popup dialog in the first Add_Dir item
    #my_message= "{'title' : 'Support & Suggestions', 'msg' : \"If you come across any online content you'd like to get added please use the support thread at noobsandnerds.com and I'll be happy to look into it for you.\"}"

    #Add_Dir(
        #name="Support/Suggestions", url=my_message, mode="simple_dialog", folder=False,
        #icon="https://cdn2.iconfinder.com/data/icons/picons-basic-2/57/basic2-087_info-512.png")
        
# Add some YT Playlists (see we're using BASE as the url)

@route(mode='edinburgh_military_tattoo_menu')
def Edinburgh_Military_Tattoo_Menu():
    Add_Dir(name="2002", url=BASE3+YOUTUBE_CHANNEL_ID_4, folder=False, mode='play_yt',)
    Add_Dir(name="2010", url=BASE3+YOUTUBE_CHANNEL_ID_6, folder=False, mode='play_yt',)
    Add_Dir(name="2011", url=BASE3+YOUTUBE_CHANNEL_ID_14, folder=False, mode='play_yt',)
    Add_Dir(name="2012", url=BASE3+YOUTUBE_CHANNEL_ID_1, folder=False, mode='play_yt',)
    Add_Dir(name="2013", url=BASE3+YOUTUBE_CHANNEL_ID_2, folder=False, mode='play_yt',)
    Add_Dir(name="2014", url=BASE3+YOUTUBE_CHANNEL_ID_23, folder=False, mode='play_yt',)
    Add_Dir(name="2015", url=BASE3+YOUTUBE_CHANNEL_ID_5, folder=False, mode='play_yt',)
    Add_Dir(name="2016", url=BASE3+YOUTUBE_CHANNEL_ID_7, folder=False, mode='play_yt',)
    Add_Dir(name="2017", url=BASE3+YOUTUBE_CHANNEL_ID_19, folder=False, mode='play_yt',)


@route(mode='regimental_bands_menu')
def Regimental_Bands_Menu():
    Add_Dir(name="Black Watch", url=BASE3+YOUTUBE_CHANNEL_ID_10, folder=False, mode='play_yt',)
    Add_Dir(name="Royal Irish Regiment", url=BASE3+YOUTUBE_CHANNEL_ID_21, folder=False, mode='play_yt',)
    Add_Dir(name="RAF Pipes and Drums", url=BASE3+YOUTUBE_CHANNEL_ID_22, folder=False, mode='play_yt',)
	#Add_Dir(name="Royal Regiment of Scotland", url=BASE3+YOUTUBE_CHANNEL_ID_8, folder=False, mode='play_yt',)
	#Add_Dir(name="Royal Scots Dragoon Guards", url=BASE3+YOUTUBE_CHANNEL_ID_12, folder=False, mode='play_yt',)
	#Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)

@route(mode='gurkha_pipes_and_drums_menu')
def Gurkha_Pipes_And_Drums_Menu():
    Add_Dir(name="1/3 GR", url=BASE3+YOUTUBE_CHANNEL_ID_17, folder=False, mode='play_yt',)
    Add_Dir(name="Indian Army 14th Gorkha Regt, Trg  Centre Display", url=BASE3+YOUTUBE_CHANNEL_ID_18, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)


@route(mode='other_military_tattoos_menu')
def Other_Military_Tattoos_Menu():
	Add_Dir(name="Australian Military Tattoo 2005", url=BASE3+YOUTUBE_CHANNEL_ID_3, folder=False, mode='play_yt',)
    #Add_Dir(name="Berlin Military Tattoo 2011", url=BASE3+YOUTUBE_CHANNEL_ID_12, folder=False, mode='play_yt',)
    #Add_Dir(name="Basel Tattoo 2016", url=BASE3+YOUTUBE_CHANNEL_ID_20, folder=False, mode='play_yt',)
    #Add_Dir(name="Basel Tattoo 2017", url=BASE3+YOUTUBE_CHANNEL_ID_13, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False, mode='play_yt',)


@route(mode='general_piping_content_menu')
def General_Piping_Content_Menu():
	Add_Dir(name="Mixed Selection", url=BASE3+YOUTUBE_CHANNEL_ID_15, folder=False, mode='play_yt',)
	Add_Dir(name="Mixed Selection 2", url=BASE3+YOUTUBE_CHANNEL_ID_16, folder=False, mode='play_yt',)    

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
#_________________________________________________________________      
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