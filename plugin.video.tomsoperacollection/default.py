
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
# Addon:  Toms Opera Collection - My YouTube Add-on
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
#debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
#addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id

# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3 = "play/?video_id="

# Set each of your YouTube playlist id's

YOUTUBE_CHANNEL_ID_1 = "PLTwpcgYYM-zwDTu1TAVhGz9QEG88aeToQ"
YOUTUBE_CHANNEL_ID_2 = "PLDBt7LIJrBCVjfCZnQxBqnMtQ74IJW0uT"
YOUTUBE_CHANNEL_ID_3 = "PLIn0resN3fmCohhLwAwVs5KRl-DCb1kB2"
YOUTUBE_CHANNEL_ID_4 = "PLE1DB862865A96BAE"
YOUTUBE_CHANNEL_ID_5 = "p2U4Eyd856o"
YOUTUBE_CHANNEL_ID_6 = "jLGkXg3j49s"
YOUTUBE_CHANNEL_ID_7 = "Drce8uXvyHg"
YOUTUBE_CHANNEL_ID_8 = "fmAKntaxACY&t"
YOUTUBE_CHANNEL_ID_9 = "PL4D3890AB7A589B44"
YOUTUBE_CHANNEL_ID_10 = "PLCCD3F9F3A9431965"
YOUTUBE_CHANNEL_ID_11 = "PL5017B9281C38ED4A"
YOUTUBE_CHANNEL_ID_12 = "PL46A47F536529049F"
YOUTUBE_CHANNEL_ID_13 = "PL3Y5ENAJSPRo5s36cu7QW7Y1b93gw7uie"
YOUTUBE_CHANNEL_ID_14 = "PL494BBD335363B5DE "
YOUTUBE_CHANNEL_ID_15 = "PL7ShuxblyYmG8XMIaPN9AkSxDIGbDedfg"
YOUTUBE_CHANNEL_ID_16 = "-fbSqOY8z_4"
YOUTUBE_CHANNEL_ID_17 = "2Q-8QhMAnAU"
YOUTUBE_CHANNEL_ID_18 = "oRy_qhHcnTs"
YOUTUBE_CHANNEL_ID_19 = "tempDM_-LKc"
YOUTUBE_CHANNEL_ID_20 = "UAmxb21bqUU"
YOUTUBE_CHANNEL_ID_21 = "dkXcvzMVQj0"
YOUTUBE_CHANNEL_ID_22 = "Oni4iY-b1sg"


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
    Add_Dir(name="Welsh National Opera", url=' ', mode="welsh_national_opera_menu", folder=True,)
    Add_Dir(name="English National Opera", url=' ', mode="english_national_opera_menu", folder=True,)
    Add_Dir(name="Compilations", url=' ', mode="compilations_menu", folder=True,)
    Add_Dir(name="Tosca", url=' ', mode="tosca_menu", folder=True,)
    Add_Dir(name="Gilbert and Sullivan", url=' ', mode="gilbert_and_sullivan_menu", folder=True,)
    Add_Dir(name="Tchaikovsky Operas", url=' ',mode="tchaikovsky_operas_menu", folder=True,)
 
@route(mode='welsh_national_opera_menu')
def Welsh_National_Opera_Menu(): 
    Add_Dir(name="La Boheme", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,)



@route(mode='english_national_opera_menu')
def English_National_Opera_Menu(): 
    Add_Dir(name="Rigoletto", url=BASE+YOUTUBE_CHANNEL_ID_15+"/", folder=True,)
    
@route(mode='gilbert_and_sullivan_menu')
def Gilbert_And_Sullivan_Menu():
    Add_Dir(name="HMS Pinafore", url=BASE3+YOUTUBE_CHANNEL_ID_17+"/", folder=False, mode='play_yt',)
    Add_Dir(name="The Mikado", url=BASE3+YOUTUBE_CHANNEL_ID_16+"/", folder=False, mode='play_yt',)
    Add_Dir(name="The Pirates Of Penzance", url=BASE3+YOUTUBE_CHANNEL_ID_18+"/", folder=False, mode='play_yt',)
    Add_Dir(name="Iolanthe", url=BASE3+YOUTUBE_CHANNEL_ID_19+"/", folder=False, mode='play_yt',)

@route(mode='compilations_menu')
def Various_Menu():   
    Add_Dir(name="Puccini", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,)
    Add_Dir(name="Classical Opera extracts", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,)
    Add_Dir(name="Richard Wagner", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,)
    Add_Dir(name="Glyndebourne Festival plus Others", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,)
    Add_Dir(name="Placido Domingo", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,)
    Add_Dir(name="Bryn Terfel", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,)
    Add_Dir(name="Juan Diego Florez", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,)
    Add_Dir(name="Mezzo Sporanos", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,)
    Add_Dir(name="Jose Carrera Zarzuela", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,)

@route(mode='tosca_menu')
def Tosca_Menu(): 
    Add_Dir(name="Madame Butterfly", url=BASE3+YOUTUBE_CHANNEL_ID_5+"/", folder=False, mode='play_yt',)
    Add_Dir(name="Tosca Arena di Verona", url=BASE3+YOUTUBE_CHANNEL_ID_6+"/", folder=False, mode='play_yt',)
    Add_Dir(name="La Traviata", url=BASE3+YOUTUBE_CHANNEL_ID_7+"/", folder=False, mode='play_yt',)
    Add_Dir(name="Bizet,Carmen,Jonas Kaufman", url=BASE3+YOUTUBE_CHANNEL_ID_8+"/", folder=False, mode='play_yt',)

@route(mode='tchaikovsky_operas_menu')
def Tchaikovsky_Operas_menu():
    Add_Dir(name="La Belle Durmiente, Opera Paris", url=BASE3+YOUTUBE_CHANNEL_ID_20+"/", folder=False, mode='play_yt',)
    Add_Dir(name="The Nutcracker Suite, Royal Swedish Opera", url=BASE3+YOUTUBE_CHANNEL_ID_21+"/", folder=False, mode='play_yt',)
    Add_Dir(name="Iolanthe, Black Sea Music Festival", url=BASE3+YOUTUBE_CHANNEL_ID_22+"/", folder=False, mode='play_yt',)


#------------------------------------------------------------
# A basic OK Dialog
@route(mode='koding_settings')
def Koding_settings():
    Open_Settings()
#---------------------------------------------------------
# A basic OK Dialog
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)     
#----------------------------------------------------------
# Play a youtube video
@route(mode='play_yt', args=['url'])
def Play_YT(url):
    xbmc.Player().play('plugin://plugin.video.youtube/'+url)

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