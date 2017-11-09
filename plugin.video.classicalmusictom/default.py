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
#debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
#addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id

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
YOUTUBE_CHANNEL_ID_17 = "HuoOxF9U0C4"
YOUTUBE_CHANNEL_ID_18 = "PL76dJku6jw7GSGh3S-5uPCDPJZDY7ngzr"
YOUTUBE_CHANNEL_ID_21 = "SQNymNaTr-Y"
YOUTUBE_CHANNEL_ID_22 = "rOjHhS5MtvA"
YOUTUBE_CHANNEL_ID_23 = "neDnpgZPPvY"
YOUTUBE_CHANNEL_ID_24 = "EQH0C5yB6JI"
YOUTUBE_CHANNEL_ID_25 = "s68W8KDp5eM"
YOUTUBE_CHANNEL_ID_26 = "RDs68W8KDp5eM"
YOUTUBE_CHANNEL_ID_27 = "RDs68W8KDp5eM&index=13"
YOUTUBE_CHANNEL_ID_28 = "m18gDXZP9Hk"
YOUTUBE_CHANNEL_ID_31 = "fNU-XAZjhzA"
YOUTUBE_CHANNEL_ID_32 = "ETXPKHPPov8"
YOUTUBE_CHANNEL_ID_33 = "5OjLKhmzQTA"
YOUTUBE_CHANNEL_ID_36 = "nFFxFhf2aS8"
YOUTUBE_CHANNEL_ID_37 = "nzB1_2G_QX0"
YOUTUBE_CHANNEL_ID_38 = "5uiVoZTBN0"
YOUTUBE_CHANNEL_ID_39 = "DsLoe5LaKqU"
YOUTUBE_CHANNEL_ID_40 = "4i0TnNI6U-w"
YOUTUBE_CHANNEL_ID_41 = "EWgYg5Iicqk"
YOUTUBE_CHANNEL_ID_42 = "9AmxZnlRa6Q"
YOUTUBE_CHANNEL_ID_43 = "K55d9a8j8WE"
YOUTUBE_CHANNEL_ID_44 = "9qfsBgMK7s0"
YOUTUBE_CHANNEL_ID_45 = "UCGoVPaw4yHmSR6OGaRHvd_g"
YOUTUBE_CHANNEL_ID_46 = "cQFjDBFXN58"
YOUTUBE_CHANNEL_ID_47 = "sHsFIv8VA7w"
YOUTUBE_CHANNEL_ID_48 = "vOvXhyldUko"
YOUTUBE_CHANNEL_ID_49 = "HClX2s8A9IE"
YOUTUBE_CHANNEL_ID_50 = "_9RT2nHD6CQ"
YOUTUBE_CHANNEL_ID_51 = "SvuitFzDxDg"
YOUTUBE_CHANNEL_ID_52 = "rEGOihjqO9w"
YOUTUBE_CHANNEL_ID_53 = "4MPuoOj5TIw"
YOUTUBE_CHANNEL_ID_54 = "1AwFutIcnrU"
YOUTUBE_CHANNEL_ID_55 = "YMN_DWY9RX8"
YOUTUBE_CHANNEL_ID_56 = "YsEo1PsSmbg"
YOUTUBE_CHANNEL_ID_57 = "NSYEOLwVfU8"
YOUTUBE_CHANNEL_ID_58 = "RlGe8bsdpB8"
YOUTUBE_CHANNEL_ID_59 = "iHlJhuS_3TA"
YOUTUBE_CHANNEL_ID_60 = "OCiKqIsF2IQ"
YOUTUBE_CHANNEL_ID_61 = "-nPtijc0HBc"
YOUTUBE_CHANNEL_ID_62 = "USEM1Ju1his"
YOUTUBE_CHANNEL_ID_63 = "PLRhAdIodfVA-IG2QxN1BPumH68riW3XDD"
YOUTUBE_CHANNEL_ID_64 = "nheif2BuFz0"
YOUTUBE_CHANNEL_ID_65 = "4oj_2Lmb23A"
YOUTUBE_CHANNEL_ID_66 = "YT_63UntRJE"
YOUTUBE_CHANNEL_ID_67 = "PLRhAdIodfVA9TQ1QL76zx1vxRt9ppBJ0E"
YOUTUBE_CHANNEL_ID_68 = "LHmWoAj4al0"
YOUTUBE_CHANNEL_ID_69 = "-Tm0Phjiouk"
YOUTUBE_CHANNEL_ID_70 = "1lHOYvIhLxo"
#YOUTUBE_CHANNEL_ID_71 = ""
#YOUTUBE_CHANNEL_ID_72 = ""
#YOUTUBE_CHANNEL_ID_73 = ""
#YOUTUBE_CHANNEL_ID_74 = ""
#YOUTUBE_CHANNEL_ID_75 = ""
#YOUTUBE_CHANNEL_ID_77 = ""
#YOUTUBE_CHANNEL_ID_78 = ""
#YOUTUBE_CHANNEL_ID_79 = ""







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
    
    Add_Dir(name="Wagner", url=' ', mode="wagner_menu", folder=True,)
    Add_Dir(name="Schubert", url=' ', mode="schubert_menu", folder=True,)
    Add_Dir(name="Strauss", url=' ', mode="strauss_menu", folder=True,)
    Add_Dir(name="Elgar", url=' ', mode="elgar_menu", folder=True,)
    Add_Dir(name="Brahms", url=' ', mode="brahms_menu", folder=True,)
    Add_Dir(name="Bach", url=' ', mode="bach_menu", folder=True,)
    Add_Dir(name="Tchaikovsky", url=' ', mode="tchaikovsky_menu", folder=True,)
    Add_Dir(name="Beethoven", url=' ', mode="beethoven_menu", folder=True,)
    Add_Dir(name="Mozart", url=' ', mode="mozart_menu", folder=True,)
    Add_Dir(name="BBC Proms", url=' ', mode="bbc_proms_menu", folder=True,)
    Add_Dir(name="Royal Philharmonic", url=' ', mode="royal_philharmonic_menu", folder=True,)
    Add_Dir(name="Compilations", url=' ', mode="compilations_menu", folder=True,)
    Add_Dir(name="Sibelius", url=' ', mode="sibelius_menu", folder=True,)
    Add_Dir(name="Rachmaninoff", url=' ',mode="rachmaninoff_menu", folder=True,)
    Add_Dir(name="Mahler", url=' ',mode="mahler_menu", folder=True,)
    Add_Dir(name="Dvorak", url=' ',mode="dvorak_menu", folder=True,)
    Add_Dir(name="Wetz", url=' ',mode="wetz_menu", folder=True,)
    Add_Dir(name="Schumann", url=' ',mode="schumann_menu", folder=True,)
    Add_Dir(name="Mendelsohn", url=' ',mode="mendelsohn_menu", folder=True,)
    #Add_Dir(name="", url='',mode="_menu", folder=True,)





@route(mode='wagner_menu')
def Wagner_Menu():
    Add_Dir(name="Wagner Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,)
    Add_Dir(name="The Best of Wagner", url=BASE3+YOUTUBE_CHANNEL_ID_40, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='mahler_menu')
def Mahler_Menu():
    Add_Dir(name="Symphony No 1 The Titan - Bernstein Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_46, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 2 Auferstehung - Rotal Concertgebouw Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_47, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 2 Abbado - Resurrection Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_53, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 3 Bernstein- Vienna Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_54, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 4 Bernstein- Vienna Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_59, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 5 Abbado - Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_48, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 6 Abbado - Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_56, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 7 Bernstein - Vienna Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_60, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 8 Bernstein Vienna Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_57, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 9 Barenbolm- Berlin State Opera", url=BASE3+YOUTUBE_CHANNEL_ID_58, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 10 Rotterdam Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_55, folder=False,mode='play_yt',)


@route(mode='schubert_menu')
def Schubert_Menu():
    Add_Dir(name="Schubert Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,)

@route(mode='dvorak_menu')
def Dvorak_Menu():
    Add_Dir(name="New World Symphony No 9 - New York Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_49, folder=False,mode='play_yt',)
    Add_Dir(name="New World Symphony No 9- Munich Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_49, folder=False,mode='play_yt',)

@route(mode='strauss_menu')
def Strauss_Menu():
    Add_Dir(name="Strauss, Horn Certo No1, Okayama Symphony", url=BASE3+YOUTUBE_CHANNEL_ID_24, folder=False, mode='play_yt',)
    Add_Dir(name="Strauss, French Horn No 1, Munich Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_25, folder=False, mode='play_yt',)
    Add_Dir(name="Horn Lesson, Berlin Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_26, folder=False, mode='play_yt')
    Add_Dir(name="Strauss, Concerto No 1, French Horn, Monila Nemcova", url=BASE3+YOUTUBE_CHANNEL_ID_28, folder=False, mode='play_yt',)


@route(mode='elgar_menu')
def Elgar_Menu():
    Add_Dir(name="Elgar Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,)
    Add_Dir(name="The Dream of Gerontius", url=BASE3+YOUTUBE_CHANNEL_ID_43, folder=False,mode='play_yt',)
    Add_Dir(name="Organ Music", url=BASE3+YOUTUBE_CHANNEL_ID_44, folder=False,mode='play_yt',)
    Add_Dir(name="Elgar Playlist", url=BASE+YOUTUBE_CHANNEL_ID_45+"/", folder=True,)

@route(mode='brahms_menu')
def Brahms_Menu():
    Add_Dir(name="Brahms",url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,)
    Add_Dir(name="Brahms and Sibelius, Double Concerto for Violin and Viola", url=BASE3+YOUTUBE_CHANNEL_ID_33, folder=False, mode='play_yt',)   


@route(mode='bach_menu')
def Bach_Menu():
    Add_Dir(name="Bach and Debussy",url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,)

@route(mode='wetz_menu')
def Wetz_Menu():
    Add_Dir(name="Violin Concerto B Minor Op 57", url=BASE+YOUTUBE_CHANNEL_ID_61+"/", folder=True,)
    Add_Dir(name="kleist Overture Staatsphilharmonie Rheinland-Pfalz ", url=BASE+YOUTUBE_CHANNEL_ID_62+"/", folder=True,)

@route(mode='tchaikovsky_menu')
def Tchaikovsky_Menu():
    Add_Dir(name="Tchaikovsky Symphonies 1 to 6", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,)


@route(mode='beethoven_menu')
def Beethoven_Menu():
    Add_Dir(name="Symphony No 6 - Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_68, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No 3 - Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_69, folder=False, mode='play_yt',)
    Add_Dir(name="Symphony No 5 - Bernstein", url=BASE3+YOUTUBE_CHANNEL_ID_70, folder=False, mode='play_yt',)
    Add_Dir(name="All 9 Symphonies", url=BASE3+YOUTUBE_CHANNEL_ID_37, folder=False, mode='play_yt',)   
    Add_Dir(name="Symphony No 9, Chicago Symphony Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_22, folder=False, mode='play_yt',)

@route(mode='mozart_menu')
def Mozart_Menu():
    Add_Dir(name="Horn Concerto No 2", url=BASE3+YOUTUBE_CHANNEL_ID_27, folder=False, mode='play_yt',)
    Add_Dir(name="Requiem", url=BASE3+YOUTUBE_CHANNEL_ID_23, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No 21", url=BASE3+YOUTUBE_CHANNEL_ID_31, folder=False, mode='play_yt',)
    Add_Dir(name="Various Wind Concerto",url=BASE+YOUTUBE_CHANNEL_ID_18+"/", folder=True,)
    Add_Dir(name="Violin Concerto No 5, Salzburg", url=BASE3+YOUTUBE_CHANNEL_ID_32, folder=False, mode='play_yt',)
    Add_Dir(name="Flute & Harp - Mehta -Israel Philharmonic Orcestra", url=BASE3+YOUTUBE_CHANNEL_ID_65, folder=False, mode='play_yt',)
    Add_Dir(name="Clarinet Concerto - Iceland Symphony Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_66, folder=False, mode='play_yt',)
    Add_Dir(name="Playlist",url=BASE+YOUTUBE_CHANNEL_ID_67"/", folder=True,)

@route(mode='rachmaninoff_menu')
def Rachmaninoff_Menu():
    Add_Dir(name="Piano Concerto No2, Yuja Wang", url=BASE3+YOUTUBE_CHANNEL_ID_41, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No2 Op 18, Anna Fedorova", url=BASE3+YOUTUBE_CHANNEL_ID_52, folder=False, mode='play_yt')
    Add_Dir(name="Piano Concerto No3, Olga Kern", url=BASE3+YOUTUBE_CHANNEL_ID_42, folder=False, mode='play_yt',)
    Add_Dir(name="Symphony No 2 Op 27, NL Radio Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_51, folder=False, mode='play_yt',)

@route(mode='schumann_menu')
def Schumann_Menu():
    Add_Dir(name="R Schumann",url=BASE+YOUTUBE_CHANNEL_ID_63+"/", folder=True,)

@route(mode='mendelsohn_menu')
def Mendelsohn_Menu():
    Add_Dir(name="Concerto for Flute, Harp C Major", url=BASE3+YOUTUBE_CHANNEL_ID_64, folder=False, mode='play_yt',)

@route(mode='sibelius_menu')
def Sibelius_Menu():
    Add_Dir(name="The Best of Sibelius", url=BASE3+YOUTUBE_CHANNEL_ID_39, folder=False, mode='play_yt',)


@route(mode='bbc_proms_menu')
def BBC_Proms_Menu():
    Add_Dir(name="Last Night at the Proms 2015", url=BASE3+YOUTUBE_CHANNEL_ID_38, folder=False, mode='play_yt',) 
    Add_Dir(name="Birtwistles Deep Time and Elgar 2nd Symphony", url=BASE3+YOUTUBE_CHANNEL_ID_36, folder=False, mode='play_yt',)


@route(mode='royal_philharmonic_menu') 
def Royal_Philharmonic_Menu(): 
    Add_Dir(name="The Symphonic Beatles", url=BASE3+YOUTUBE_CHANNEL_ID_15, folder=False, mode='play_yt',)
    Add_Dir(name="Queen", url=BASE3+YOUTUBE_CHANNEL_ID_16, folder=False, mode='play_yt',)
    Add_Dir(name="Pink Floyd", url=BASE3+YOUTUBE_CHANNEL_ID_17, folder=False, mode='play_yt',)


@route(mode='compilations_menu')
def Compilations_Menu():
    Add_Dir(name="Various", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,)
    Add_Dir(name="Nielsen Symphonies",url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,)
    Add_Dir(name="Classical Short Clips",url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,)
    Add_Dir(name="Just Instrumental",url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,)
    Add_Dir(name="Czech Composers Plus",url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,)
    Add_Dir(name="Baroque Music ",url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,)
    Add_Dir(name="Debussy Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,)
    Add_Dir(name="Karajan Legacy Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,)    
    Add_Dir(name="Rimsky Korsakov, Scheherazade, Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_21, folder=False, mode='play_yt',)


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
# Play a youtube video
@route(mode='play_yt', args=['url'])
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