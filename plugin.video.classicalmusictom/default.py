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
YOUTUBE_CHANNEL_ID_6 = "v0xypy7JCF4"
YOUTUBE_CHANNEL_ID_7 = "PLS6C4jHVZhO5xlfh8IZYzbgJaKZt8XNDZ"
YOUTUBE_CHANNEL_ID_8 = "PLS6C4jHVZhO6fV14M7M0kuSfIf5dqx5oz"
YOUTUBE_CHANNEL_ID_9 = "PLS6C4jHVZhO7mdvWazKgf3aHo4rryrnbW"
YOUTUBE_CHANNEL_ID_12 = "PLcGkkXtask_c_iDYwGpTkK0i--J8iafgH"
YOUTUBE_CHANNEL_ID_14 = "PL_qM1lclHDwUPGV9v5tJzTv1X5e8fAJRu"
YOUTUBE_CHANNEL_ID_15 = "ZeBljzppZsM"
YOUTUBE_CHANNEL_ID_16 = "4g4UZOedczs"
YOUTUBE_CHANNEL_ID_17 = "HuoOxF9U0C4"
YOUTUBE_CHANNEL_ID_18 = "PL76dJku6jw7GSGh3S-5uPCDPJZDY7ngzr"
YOUTUBE_CHANNEL_ID_19 = "4Yzessr6cE0"
YOUTUBE_CHANNEL_ID_20 = "E2c93ku590I"
YOUTUBE_CHANNEL_ID_21 = "SQNymNaTr-Y"
YOUTUBE_CHANNEL_ID_22 = "rOjHhS5MtvA"
YOUTUBE_CHANNEL_ID_23 = "neDnpgZPPvY"
YOUTUBE_CHANNEL_ID_24 = "EQH0C5yB6JI"
YOUTUBE_CHANNEL_ID_25 = "s68W8KDp5eM"
YOUTUBE_CHANNEL_ID_26 = "yM8CFR01KwQ"
YOUTUBE_CHANNEL_ID_27 = "s68kHOnpiE"
YOUTUBE_CHANNEL_ID_28 = "m18gDXZP9Hk"
YOUTUBE_CHANNEL_ID_31 = "fNU-XAZjhzA"
YOUTUBE_CHANNEL_ID_32 = "ETXPKHPPov8"
YOUTUBE_CHANNEL_ID_33 = "5OjLKhmzQTA"
YOUTUBE_CHANNEL_ID_34 = "PvrPGO7ja3k"
YOUTUBE_CHANNEL_ID_36 = "DXeBFhqViYg"
YOUTUBE_CHANNEL_ID_37 = "nzB1_2G_QX0"
YOUTUBE_CHANNEL_ID_38 = "yDqCIcsUtPI"
YOUTUBE_CHANNEL_ID_39 = "DsLoe5LaKqU"
YOUTUBE_CHANNEL_ID_40 = "4i0TnNI6U-w"
YOUTUBE_CHANNEL_ID_41 = "EWgYg5Iicqk"
YOUTUBE_CHANNEL_ID_42 = "9AmxZnlRa6Q"
YOUTUBE_CHANNEL_ID_43 = "K55d9a8j8WE"
YOUTUBE_CHANNEL_ID_44 = "9qfsBgMK7s0"
YOUTUBE_CHANNEL_ID_45 = "pEYajsa8NeM"
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
YOUTUBE_CHANNEL_ID_61 = "ZMjzPJacd6g"
YOUTUBE_CHANNEL_ID_62 = "o1dBg__wsuo"
YOUTUBE_CHANNEL_ID_63 = "PLRhAdIodfVA-IG2QxN1BPumH68riW3XDD"
YOUTUBE_CHANNEL_ID_64 = "nheif2BuFz0"
YOUTUBE_CHANNEL_ID_65 = "4oj_2Lmb23A"
YOUTUBE_CHANNEL_ID_66 = "YT_63UntRJE"
YOUTUBE_CHANNEL_ID_67 = "zns6-njnqB8"
YOUTUBE_CHANNEL_ID_68 = "LHmWoAj4al0"
YOUTUBE_CHANNEL_ID_69 = "-Tm0Phjiouk"
YOUTUBE_CHANNEL_ID_70 = "1lHOYvIhLxo"
YOUTUBE_CHANNEL_ID_71 = "dZDiaRZy0Ak"
YOUTUBE_CHANNEL_ID_72 = "1syDCEn_XOw"
YOUTUBE_CHANNEL_ID_73 = "N8jP3o22HGw"
YOUTUBE_CHANNEL_ID_74 = "eT6SuXdytzU"
YOUTUBE_CHANNEL_ID_75 = "8sSFVvF7-W0"
YOUTUBE_CHANNEL_ID_76 = "U_yxtaeFuEQ"
YOUTUBE_CHANNEL_ID_77 = "s68W8KDp5eM"
YOUTUBE_CHANNEL_ID_78 = "KTM7E4-DN0o"
YOUTUBE_CHANNEL_ID_79 = "hcjDr0PB8Wk"
YOUTUBE_CHANNEL_ID_80 = "3NG0WGARfwY"
YOUTUBE_CHANNEL_ID_81 = "Pl3LN9l9SXg"
YOUTUBE_CHANNEL_ID_82 = "83aR2T9AQ7E"
YOUTUBE_CHANNEL_ID_83 = "zsTo7QxxgYg"
YOUTUBE_CHANNEL_ID_84 = "FU5Hpx7JSaA"
YOUTUBE_CHANNEL_ID_85 = "8pmdlgKalyQ"
YOUTUBE_CHANNEL_ID_86 = "wHAfvUFtCIY"
YOUTUBE_CHANNEL_ID_87 = "4XbHLFkg_Mw"
YOUTUBE_CHANNEL_ID_88 = "SgSNgzA37To"
YOUTUBE_CHANNEL_ID_89 = "Xplx64LVENg"
YOUTUBE_CHANNEL_ID_90 = "oG8T8twoVhg"
YOUTUBE_CHANNEL_ID_91 = "Lh6mDL-VwYw"
YOUTUBE_CHANNEL_ID_92 = "fB0IHPGuTFo"
YOUTUBE_CHANNEL_ID_93 = "MW8asBxO4oI"
YOUTUBE_CHANNEL_ID_94 = "4wvpdBnfiZo"
YOUTUBE_CHANNEL_ID_95 = "96ZQFXmtNNU"
YOUTUBE_CHANNEL_ID_96 = "Ynky7qoPnUU"
YOUTUBE_CHANNEL_ID_97 = "3jbHbDena_U"
YOUTUBE_CHANNEL_ID_98 = "sfH5c93kqgw"
YOUTUBE_CHANNEL_ID_99 = "Vtyod61mB6A"
YOUTUBE_CHANNEL_ID_100 = "fnpVu8Eihj4"
YOUTUBE_CHANNEL_ID_101 = "O52r9_bXWBw"
YOUTUBE_CHANNEL_ID_102 = "7rVW4Z70TfE"
YOUTUBE_CHANNEL_ID_103 = "z921INvMVPM"
YOUTUBE_CHANNEL_ID_104 = "OOlc2PAiWUU"
YOUTUBE_CHANNEL_ID_105 = "KE93NdTBBvc"
YOUTUBE_CHANNEL_ID_106 = "GHNgfF19CTY"
YOUTUBE_CHANNEL_ID_107 = "625WOYzdvFw"
YOUTUBE_CHANNEL_ID_108 = "lD7gjmvM66M"
YOUTUBE_CHANNEL_ID_109 = 'IEuxKCB6o8'
YOUTUBE_CHANNEL_ID_110 = "ZuGSOkYWfDQ"
YOUTUBE_CHANNEL_ID_111 = "9JoDAOSKUu4"
YOUTUBE_CHANNEL_ID_112 = "o_gm0NCabPs"
YOUTUBE_CHANNEL_ID_113 = "UfkyR6Nfeo0"
YOUTUBE_CHANNEL_ID_114 = "RxDCgFFBk20"
YOUTUBE_CHANNEL_ID_115 = "oWWeL8YvS2g"
YOUTUBE_CHANNEL_ID_116 = "IARUa3l5Hxg"
YOUTUBE_CHANNEL_ID_117 = "FpK1tjbeeA0"
YOUTUBE_CHANNEL_ID_118 = "UFl9xuYP5T8"
YOUTUBE_CHANNEL_ID_119 = "weTtT4tb9bE"
YOUTUBE_CHANNEL_ID_120 = "pjRt-o0XwZ4"
YOUTUBE_CHANNEL_ID_121 = "K94ePzs14Nc"
YOUTUBE_CHANNEL_ID_122 = "fvy0nN5t0Po"
YOUTUBE_CHANNEL_ID_123 = "98UjjwzJBFE"
YOUTUBE_CHANNEL_ID_124 = "X6s6YKlTpfw"
YOUTUBE_CHANNEL_ID_125 = "JH3T6YwwU9s"
YOUTUBE_CHANNEL_ID_126 = "dS65-ZvUSSM"
YOUTUBE_CHANNEL_ID_127 = "uoiXvQhWrKY"
YOUTUBE_CHANNEL_ID_128 = "EVAB2z1RPu4"
YOUTUBE_CHANNEL_ID_129 = "cAcXRHN8uWw"
YOUTUBE_CHANNEL_ID_130 = "onDXSnrcL9s"
YOUTUBE_CHANNEL_ID_131 = "Xba1Fpv6GM4&feature=em-subs_digest-vrecs"
YOUTUBE_CHANNEL_ID_132 = "OPlK5HwFxcw"
YOUTUBE_CHANNEL_ID_133 = "Dyf2MWHnwOU"
YOUTUBE_CHANNEL_ID_134 = "akrn3t0FL64&feature=em-subs_digest-vrecs"
YOUTUBE_CHANNEL_ID_135 = "Y5MJDd8zEOM"
YOUTUBE_CHANNEL_ID_136 = "AgXW-57UDMc"
YOUTUBE_CHANNEL_ID_137 = "zhqg4U32p9w"
YOUTUBE_CHANNEL_ID_138 = "yIJ3wCqaScQ"
YOUTUBE_CHANNEL_ID_139 = "NnLIMWLs0b8"
YOUTUBE_CHANNEL_ID_140 = "y3K5oLg-Fq4"
YOUTUBE_CHANNEL_ID_141 = "Ehbar90jHz8"
YOUTUBE_CHANNEL_ID_142 = "jm1os4VzTgA"
YOUTUBE_CHANNEL_ID_143 = "dfLNM7tlSF8"
YOUTUBE_CHANNEL_ID_144 = "fT1y0_9qpeY"
YOUTUBE_CHANNEL_ID_145 = "ZnIDTOR9EkM"
YOUTUBE_CHANNEL_ID_146 = "ivaZWGcq5Ic"
YOUTUBE_CHANNEL_ID_147 = "xlmXSVmsdR8"
YOUTUBE_CHANNEL_ID_148 = "alm_TjQT76U"
YOUTUBE_CHANNEL_ID_149 = "QQAWqqaUTHE"
YOUTUBE_CHANNEL_ID_150 = "7F7TVM8m95Y"
YOUTUBE_CHANNEL_ID_151 = "BnjqGhAlFzs"
YOUTUBE_CHANNEL_ID_152 = "tk5Uturacx8"
YOUTUBE_CHANNEL_ID_153 = "yDqCIcsUtPI&t=189s"
YOUTUBE_CHANNEL_ID_154 = "VbxgYlcNxE8"
YOUTUBE_CHANNEL_ID_155 = "FqZfoK25lnY"
YOUTUBE_CHANNEL_ID_156 = "tSJ_woWnmk"
YOUTUBE_CHANNEL_ID_157 = "w2JBT0HC98I"
YOUTUBE_CHANNEL_ID_158 = "8vHL0UNCa1Q"
YOUTUBE_CHANNEL_ID_159 = "nMViOrqBzPk"
YOUTUBE_CHANNEL_ID_160 = "in_HCO9FlSk"
YOUTUBE_CHANNEL_ID_161 = "1KzF1KgaREo"
YOUTUBE_CHANNEL_ID_162 = "ozq-XfBv3Y8"
YOUTUBE_CHANNEL_ID_163 = "KX29pHsEeqQ"
YOUTUBE_CHANNEL_ID_164 = "EGRqIGOAPcE"
YOUTUBE_CHANNEL_ID_165 = "ckuUq7im8H4"
YOUTUBE_CHANNEL_ID_166 = "XHmkl7GM_es"
YOUTUBE_CHANNEL_ID_167 = "4L0MqnAoEJM"
YOUTUBE_CHANNEL_ID_168 = "fxsJ9qSsBpw"
YOUTUBE_CHANNEL_ID_169 = "YOayoH9YRWk"
YOUTUBE_CHANNEL_ID_170 = "cvsbFQk_WpQ"
YOUTUBE_CHANNEL_ID_171 = "oFdzAbc-cmw"
YOUTUBE_CHANNEL_ID_172 = "pj_2Xoyoy8Y"
YOUTUBE_CHANNEL_ID_173 = "ozq-XfBv3Y8"
YOUTUBE_CHANNEL_ID_174 = "A3aulUgdQyM"
YOUTUBE_CHANNEL_ID_175 = "rN1o90rtflE"
YOUTUBE_CHANNEL_ID_176 = "ETveS23djXM"
YOUTUBE_CHANNEL_ID_177 = "ZRXdfKHVjVY"
YOUTUBE_CHANNEL_ID_178 = "LAVvBF7m260"
YOUTUBE_CHANNEL_ID_179 = "FHFf7NIwOHQ"
YOUTUBE_CHANNEL_ID_180 = "GGnD-JkvWaA"
YOUTUBE_CHANNEL_ID_181 = "eDrVtXPpuRI"
YOUTUBE_CHANNEL_ID_182 = "IOwqkJvuj20"
YOUTUBE_CHANNEL_ID_183 = "OitPLIowJ70"
YOUTUBE_CHANNEL_ID_184 = "eVXalu0p1wo"
YOUTUBE_CHANNEL_ID_185 = "VDKIeyAnCBc"
YOUTUBE_CHANNEL_ID_186 = "kaI8x-saprI"
YOUTUBE_CHANNEL_ID_187 = "l3O2K-LyJ9o"
YOUTUBE_CHANNEL_ID_188 = "32Xq7Tcj428"
YOUTUBE_CHANNEL_ID_189 = "3OD_HzdZwKk"



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

    Add_Dir(name="Bach", url=' ', mode="bach_menu", folder=True,)
    Add_Dir(name="Baroque", url='',mode='baroque_menu', folder=True,)
    Add_Dir(name="Benjamin Britten", url='', mode="benjamin_britten_menu", folder=True,)
    Add_Dir(name="Berlioz", url='', mode="berlioz_menu", folder=True,)
    Add_Dir(name="Beethoven", url=' ', mode="beethoven_menu", folder=True,)
    Add_Dir(name="Brahms", url=' ', mode="brahms_menu", folder=True,)
    Add_Dir(name="Chopin", url='', mode="chopin_menu", folder=True,)
    Add_Dir(name="Compilations", url=' ', mode="compilations_menu", folder=True,)
    Add_Dir(name="Debussy", url=' ',mode="debussy_menu", folder=True,)
    Add_Dir(name="Dvorak", url=' ',mode="dvorak_menu", folder=True,)
    Add_Dir(name="Elgar", url=' ', mode="elgar_menu", folder=True,)
    Add_Dir(name="Handel", url='', mode="handel_menu", folder=True,)
    Add_Dir(name="Haydn", url='', mode="haydn_menu", folder=True,)
    Add_Dir(name="Holtz", url='',mode="holtz_menu", folder=True,)
    Add_Dir(name="Mahler", url=' ',mode="mahler_menu", folder=True,)
    Add_Dir(name="Mendelsohn", url=' ',mode="mendelsohn_menu", folder=True,)
    Add_Dir(name="Mozart", url=' ', mode="mozart_menu", folder=True,)
    Add_Dir(name="Nielsen", url=' ',mode="nielsen_menu", folder=True,)
    Add_Dir(name="Rachmaninoff", url=' ',mode="rachmaninoff_menu", folder=True,)
    Add_Dir(name="Ravel", url='', mode="ravel_menu", folder=True,)
    Add_Dir(name="Rimsky Korsakhov", url=' ',mode="rimsky_korsakhov_menu", folder=True,)
    Add_Dir(name="Schubert", url=' ', mode="schubert_menu", folder=True,)
    Add_Dir(name="Schumann", url=' ',mode="schumann_menu", folder=True,)
    Add_Dir(name="Strauss", url=' ', mode="strauss_menu", folder=True,)
    Add_Dir(name="Sibelius", url=' ', mode="sibelius_menu", folder=True,)
    Add_Dir(name="Tchaikovsky", url=' ', mode="tchaikovsky_menu", folder=True,)
    Add_Dir(name="Wagner", url=' ', mode="wagner_menu", folder=True,)


@route(mode='wagner_menu')
def Wagner_Menu():
    Add_Dir(name="Tannhauser Overture, Thielemann, Munich Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_78, folder=False,mode='play_yt',)
    Add_Dir(name="Tristan und Isole, Thielemann, Munich Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_79, folder=False,mode='play_yt',)
    Add_Dir(name="Der Ring des Nibelungen, Dudamel, Paris Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_80, folder=False,mode='play_yt',)
    Add_Dir(name="Tod Und Verlarung, Dudamel, Salzburg", url=BASE3+YOUTUBE_CHANNEL_ID_81, folder=False,mode='play_yt',)
    Add_Dir(name="Short Video extracts by the Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)


@route(mode='mahler_menu')
def Mahler_Menu():
    Add_Dir(name="Symphony No 1,Titan, Bernstein, Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_46, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 1,Titan, Abbado, Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_87, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 2 Auferstehung, Royal Concertgebouw Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_47, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 2,Resurrection, Abbado,Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_53, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 3 Bernstein, Vienna Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_54, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 4 Bernstein,Vienna Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_59, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 5 Abbado, Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_48, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 6 Abbado, Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_56, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 7 Bernstein, Vienna Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_60, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 8 Bernstein, Vienna Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_57, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 9 Barenbolm, Berlin State Opera", url=BASE3+YOUTUBE_CHANNEL_ID_58, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 10 Rotterdam Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_55, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='schubert_menu')
def Schubert_Menu():
    Add_Dir(name="Symphony No 1, Maazel, Bavarian Radio SO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_175, folder=False,mode='play_yt',)
    Add_Dir(name="Octet in F major, Hochrhein Musikfestival", url=BASE3+YOUTUBE_CHANNEL_ID_100, folder=False,mode='play_yt',)
    Add_Dir(name="Octete in F Major, J Jansen", url=BASE3+YOUTUBE_CHANNEL_ID_101, folder=False,mode='play_yt',)
    Add_Dir(name="Short video extracts by the Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)



@route(mode='dvorak_menu')
def Dvorak_Menu():
    Add_Dir(name="Symphony No 9 - New York Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_49, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 9 in E Minor, Abbado, New World", url=BASE3+YOUTUBE_CHANNEL_ID_74, folder=False,mode='play_yt',)
    Add_Dir(name="Cello Concerto in B minor, Barenboim, Jacqueline du Pre, LSO", url=BASE3+YOUTUBE_CHANNEL_ID_76, folder=False,mode='play_yt',)
    Add_Dir(name="Cello Concerto, Yo Yo Ma, Kyoto Symphony", url=BASE3+YOUTUBE_CHANNEL_ID_103, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='strauss_menu')
def Strauss_Menu():
    Add_Dir(name="Also sprach Zarathustra and Tod und Verklarung, Dudamel, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_176, folder=False,mode='play_yt',)
    Add_Dir(name="Blue Danube Waltz, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_177, folder=False,mode='play_yt',)
    Add_Dir(name="Emperor Waltz, Berlin PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_178, folder=False,mode='play_yt',)
    Add_Dir(name="Radetzky March, Karajan, Vienna PO, added jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_179, folder=False,mode='play_yt',)
    Add_Dir(name="Elektra, BBC promenade Concert, added jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_180, folder=False,mode='play_yt',)
    Add_Dir(name="Horn Certo No1, Okayama Symphony", url=BASE3+YOUTUBE_CHANNEL_ID_24, folder=False, mode='play_yt',)
    Add_Dir(name="French Horn No 1, Munich Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_25, folder=False, mode='play_yt',)
    Add_Dir(name="Concerto No 1, French Horn, Monila Nemcova", url=BASE3+YOUTUBE_CHANNEL_ID_28, folder=False, mode='play_yt',)
    Add_Dir(name="Concerto No 1, French Horn, Munich SO", url=BASE3+YOUTUBE_CHANNEL_ID_77, folder=False, mode='play_yt',)
    Add_Dir(name="Alpensinfonie, Jansons,", url=BASE3+YOUTUBE_CHANNEL_ID_82, folder=False,mode='play_yt',)
    Add_Dir(name="Alpensinfonie, Estrada, Frankfurt Radio Orchestra,", url=BASE3+YOUTUBE_CHANNEL_ID_83, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)



@route(mode='elgar_menu')
def Elgar_Menu():
    Add_Dir(name="Cello Concerto in E major, Yo Yo Ma, Baltimore Symphony", url=BASE3+YOUTUBE_CHANNEL_ID_102, folder=False,mode='play_yt',)
    Add_Dir(name="Short video clips by the Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,)
    Add_Dir(name="Soundtrack only - The Dream of Gerontius", url=BASE3+YOUTUBE_CHANNEL_ID_43, folder=False,mode='play_yt',)
    Add_Dir(name="Soundtrack only - Organ Music", url=BASE3+YOUTUBE_CHANNEL_ID_44, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)



@route(mode='brahms_menu')
def Brahms_Menu():
    Add_Dir(name="Symphony No 1, Bernstein, Vienna PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_164, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 2, Kleiber, Vienna PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_166, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 3, Bernstein, Vienna PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_167, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 4, Slatkin, detroit SO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_168, folder=False,mode='play_yt',)
    Add_Dir(name="Trio in A minor op 114, International Chamber Music festival, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_169, folder=False,mode='play_yt',)
    Add_Dir(name="Double Concerto for Violin and Viola", url=BASE3+YOUTUBE_CHANNEL_ID_33, folder=False, mode='play_yt',)   
    Add_Dir(name="Piano Concerto No 1 Helene Grimaud", url=BASE3+YOUTUBE_CHANNEL_ID_104, folder=False,mode='play_yt',)
    Add_Dir(name="Piano Concerto No 1, Barenboim, Celibidache, Munich Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_105, folder=False,mode='play_yt',)
    Add_Dir(name="Violin Concerto, Hilary Hahn, Frankfurt RO, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_118, folder=False,mode='play_yt',)
    Add_Dir(name="Soundtracks only - Symphonies 1 to 4",url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,)
    Add_Dir(name="Soundtrack only - Symphony No 4, Bernstein, Vienna PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_165, folder=False,mode='play_yt',)


@route(mode='bach_menu')
def Bach_Menu():
    Add_Dir(name="Christmas Oratorio, aded Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_123, folder=False,mode='play_yt',)
    Add_Dir(name="Concerto 1-6, Munich Baci Orchestra, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_141, folder=False,mode='play_yt',)
    Add_Dir(name="Maththaus Passion, Herneweghe, Koln Philharmonic, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_142, folder=False,mode='play_yt',)
    Add_Dir(name="Maththaus Passion, Richter, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_143, folder=False,mode='play_yt',)
    Add_Dir(name="St Johnannes Passion, Richter, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_144, folder=False,mode='play_yt',)
    Add_Dir(name="Holy Mass, Richter, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_145, folder=False,mode='play_yt',)
    Add_Dir(name="Holy Mass, T Strauus, Spartenburg Orchetsra, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_146, folder=False,mode='play_yt',)
    Add_Dir(name="Christmas Oratorium, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_147, folder=False,mode='play_yt',)
    Add_Dir(name="Christmas Oratorium, Rilling, Krakow, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_148, folder=False,mode='play_yt',)
    Add_Dir(name="Magnificant, Monterverdi Choir, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_149, folder=False,mode='play_yt',)
    Add_Dir(name="Mass in B Major, Proms, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_150, folder=False,mode='play_yt',)
    Add_Dir(name="Brandenburg Concerto, Croation Baroque Ensemble, added Jan 18 ", url=BASE3+YOUTUBE_CHANNEL_ID_151, folder=False,mode='play_yt',)
    Add_Dir(name="Soundtracks only - Bach and Debussy, added Jan 18",url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)


@route(mode='tchaikovsky_menu')
def Tchaikovsky_Menu():
    Add_Dir(name="Symphony No 1, WInter daydreams, Jansons, BBC Orchestra of Wales, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_170, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 2, Little Russian, Slatkin, Detroit SO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_160, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 3, Jansons, BBC Orchestra of Wales, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_171, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 3, Fedoseyev, Moscow Radio SO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_172, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 4, Von Karajan, Vienna PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_159, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 5, Shani, Radio Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_84, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 5, Petrenko, Russian State Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_85, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 5, Bernstein, Boston SO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_157, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 6, Von Karajan, Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_86, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 6, Chung Myung-Whun, Seoul PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_153, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 7, Kutsenko, Sloboda Virtuosi, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_173, folder=False,mode='play_yt',)
    Add_Dir(name="Symphony No 7, Manfred Symphony in B Minoir, Zhang, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_174, folder=False,mode='play_yt',)
    Add_Dir(name="1812 Overture, Pappano,Koninkliijk Concertgebouw, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_161, folder=False,mode='play_yt',)
    Add_Dir(name="1812 Overture, Leningrad Military Band, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_162, folder=False,mode='play_yt',)
    Add_Dir(name="Piano Concerto No1, Argerich, Dutoit, Orcehstra de la Suisse, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_156, folder=False,mode='play_yt',)
    Add_Dir(name="Piano Concerto No2, Yuja Wang, Simonov, Moscow PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_163, folder=False,mode='play_yt',)
    Add_Dir(name="Piano Concerto,Khatia Buniatishvili, Israel Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_19, folder=False,mode='play_yt',)
    Add_Dir(name="Nutcracker Suite, Rotterdam PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_152, folder=False,mode='play_yt',)
    Add_Dir(name="Violin Concerto in D Major, Sayka Shoji, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_158, folder=False,mode='play_yt',)
    Add_Dir(name="Viloin Concerto In D Major, Arabella Steinbacher", url=BASE3+YOUTUBE_CHANNEL_ID_98, folder=False,mode='play_yt',)
    Add_Dir(name="Soundtracks only - Symphonies 1 to 6", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,)
    Add_Dir(name="Soundtrack only - Hymn of the Cherubim, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_132, folder=False,mode='play_yt',)
    Add_Dir(name="Soundtrack only - 1812 Overture, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_154, folder=False,mode='play_yt',)
    Add_Dir(name="Soundtrack only - Swan Lake, Moscow Radio SO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_155, folder=False,mode='play_yt',)






@route(mode='beethoven_menu')
def Beethoven_Menu():
    Add_Dir(name="Symphony No 6 - Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_68, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No 3 - Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_69, folder=False, mode='play_yt',)
    Add_Dir(name="Symphony No 5 - Bernstein", url=BASE3+YOUTUBE_CHANNEL_ID_70, folder=False, mode='play_yt',)
    Add_Dir(name="Symphony No 9, Muti, Chicago Symphony Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_22, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No 5, Barenboim, Staatskapelle Berlin Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_45, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto N0 1 in C major, Barenboim, Klavierfestival Ruhr", url=BASE3+YOUTUBE_CHANNEL_ID_67, folder=False, mode='play_yt',)
    Add_Dir(name="Sinfonia No 3, Heroica, Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_73, folder=False, mode='play_yt',)
    Add_Dir(name="Concerto for Piano No 1, Khatia Buniatishvili, Israel Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_20, folder=False,mode='play_yt',)
    Add_Dir(name="Violin Concerto, Arabella Steinbacher, Orcehstra RTVE", url=BASE3+YOUTUBE_CHANNEL_ID_34, folder=False,mode='play_yt',)
    Add_Dir(name="Concerto for Violin, Cello and Piano in C Major, Tel Aviv", url=BASE3+YOUTUBE_CHANNEL_ID_99, folder=False,mode='play_yt',)
    Add_Dir(name="Ode To Joy, Japanese Choirs, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_124, folder=False,mode='play_yt',)
    Add_Dir(name="Violin Concerto D Major, Christina Bauey, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_131, folder=False,mode='play_yt',)
    Add_Dir(name="Soundtrack only - All 9 Symphonies", url=BASE3+YOUTUBE_CHANNEL_ID_37, folder=False, mode='play_yt',)   
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)





@route(mode='mozart_menu')
def Mozart_Menu():
    Add_Dir(name="Oboe Konzertr, Estrada, Frankfurt RS, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_181, folder=False, mode='play_yt',)
    Add_Dir(name="Requiem", url=BASE3+YOUTUBE_CHANNEL_ID_23, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No 21", url=BASE3+YOUTUBE_CHANNEL_ID_31, folder=False, mode='play_yt',)
    Add_Dir(name="Violin Concerto No 5, Salzburg", url=BASE3+YOUTUBE_CHANNEL_ID_32, folder=False, mode='play_yt',)
    Add_Dir(name="Flute & Harp - Mehta -Israel Philharmonic Orcestra", url=BASE3+YOUTUBE_CHANNEL_ID_65, folder=False, mode='play_yt',)
    Add_Dir(name="Clarinet Concerto - Iceland Symphony Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_66, folder=False, mode='play_yt',)
    Add_Dir(name="Flute Concerto No1 in G Major- Iceland Symphony Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_72, folder=False, mode='play_yt')
    Add_Dir(name="Sinfonia Concertetante for Violin, Viola and Orcehstra Eflat Major, Concergebouw Amsterdam", url=BASE3+YOUTUBE_CHANNEL_ID_6, folder=False, mode='play_yt')
    Add_Dir(name="Concert for Piano and Orchestra,d-major, Uchida, Salzburg Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_26, folder=False, mode='play_yt')
    Add_Dir(name="Concert No 23 in A major, Trifonov, Israel Camerata Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_27, folder=False, mode='play_yt')
    Add_Dir(name="Piano Concerto No 23 A Major Pollini & Bohm, Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_36, folder=False, mode='play_yt')
    Add_Dir(name="Piano Concert No 26, Munich Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_61, folder=False, mode='play_yt')
    Add_Dir(name="Flute and Harp Concerto, Academy in the Fields", url=BASE3+YOUTUBE_CHANNEL_ID_111, folder=False, mode='play_yt')
    Add_Dir(name="Soundtracks and some Video content - Wind Concertos ",url=BASE+YOUTUBE_CHANNEL_ID_18+"/", folder=True,)
    Add_Dir(name="Clarinet Concerto, Czech Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_112, folder=False, mode='play_yt')
    Add_Dir(name="La Santa Messa, Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_113, folder=False,mode='play_yt',)
    Add_Dir(name="Coronation Mass in C major, equilbey", url=BASE3+YOUTUBE_CHANNEL_ID_114, folder=False,mode='play_yt',)
    Add_Dir(name="Great Mass, Stutzmann", url=BASE3+YOUTUBE_CHANNEL_ID_115, folder=False,mode='play_yt',)
    Add_Dir(name="Concert for Clarinet and Orchestra Nr 12, Bayern Symphony", url=BASE3+YOUTUBE_CHANNEL_ID_116, folder=False,mode='play_yt',)
    Add_Dir(name="Piano Concerto Nr 1, Solsbaerg Festival", url=BASE3+YOUTUBE_CHANNEL_ID_117, folder=False,mode='play_yt',)




@route(mode='rachmaninoff_menu')
def Rachmaninoff_Menu():
    Add_Dir(name="Piano Concerto No2, Yuja Wang", url=BASE3+YOUTUBE_CHANNEL_ID_41, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No2 Op 18, Anna Fedorova", url=BASE3+YOUTUBE_CHANNEL_ID_52, folder=False, mode='play_yt')
    Add_Dir(name="Piano Concerto No3, Olga Kern", url=BASE3+YOUTUBE_CHANNEL_ID_42, folder=False, mode='play_yt',)
    Add_Dir(name="Symphony No 2 Op 27, NL Radio Philharmonic Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_51, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No3, Martha Argerich, Berlin RSO, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_119, folder=False,mode='play_yt',)
    Add_Dir(name="Vespers, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_120, folder=False,mode='play_yt',) 
    Add_Dir(name="Liturgie van St Johannes Chystostomous, Klava, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_121, folder=False,mode='play_yt',)
    Add_Dir(name="The Bells, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_122, folder=False,mode='play_yt',)


@route(mode='schumann_menu')
def Schumann_Menu():
    Add_Dir(name="Piano Conerto in A Minor, Martha Argerich", url=BASE3+YOUTUBE_CHANNEL_ID_96, folder=False,mode='play_yt',)
    Add_Dir(name="Soundtracks only - R Schumann",url=BASE+YOUTUBE_CHANNEL_ID_63+"/", folder=True,)
    Add_Dir(name="Khatia Buniatishvili, Frankfurt Radio Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_97, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)





@route(mode='mendelsohn_menu')
def Mendelsohn_Menu():
    Add_Dir(name="Concerto for Flute, Harp C Major, Croatian Chamber Music", url=BASE3+YOUTUBE_CHANNEL_ID_64, folder=False, mode='play_yt',)
    Add_Dir(name="Violin Concerto E Minor, H Hahn,frankfurt RSO,", url=BASE3+YOUTUBE_CHANNEL_ID_62, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='haydn_menu')
def Haydn_Menu():
    Add_Dir(name="Oboe Concerto, Hartrmann, OSUCS, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_182, folder=False, mode='play_yt',)
    Add_Dir(name="Symphony No 104, Proms, London PO, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_183, folder=False, mode='play_yt',)
    Add_Dir(name="Symphony No 94, Bernstein, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_184, folder=False,mode='play_yt',)
    Add_Dir(name="Piano Concerto No 11, Pletnev, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_185, folder=False,mode='play_yt',)
    Add_Dir(name="The Creation, Lawrence Symphony Orchetra, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_186, folder=False,mode='play_yt',)
    Add_Dir(name="The Seasons, Harnoncourt, Salzburg, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_187, folder=False,mode='play_yt',)
    Add_Dir(name="The Creation, Bernstein, Benedictine Abbey, added Jan 18", url=BASE3+YOUTUBE_CHANNEL_ID_188, folder=False,mode='play_yt',)

@route(mode='sibelius_menu')
def Sibelius_Menu():
    Add_Dir(name="Symphony No 2 in D Major, Jansons, Bavaria State Orcehstra", url=BASE3+YOUTUBE_CHANNEL_ID_75, folder=False, mode='play_yt',)
    Add_Dir(name="Soundtrack only - The Best of Sibelius", url=BASE3+YOUTUBE_CHANNEL_ID_39, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)




@route(mode='debussy_menu')
def Debussy_Menu():
    Add_Dir(name="La Mer,Abbado, Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_88, folder=False,mode='play_yt',)
    Add_Dir(name="Short video clips by the Berlin Philharmonic", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,)
    Add_Dir(name="The Martyr of St Sebastian, Abbado, Lucerne Festival Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_90, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='handel_menu')
def Handel_Menu():
    Add_Dir(name="A Sacred Oratorio, Sir Colin Davis", url=BASE3+YOUTUBE_CHANNEL_ID_110, folder=False,mode='play_yt',)
    Add_Dir(name="Messiah, V Luks, added Dec17", url=BASE3+YOUTUBE_CHANNEL_ID_125, folder=False,mode='play_yt',)
    Add_Dir(name="Dixit Dominus, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_126, folder=False,mode='play_yt',)
    Add_Dir(name="Organ Concertos, Munich Bach Orchestra, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_127, folder=False,mode='play_yt',)
    Add_Dir(name="Water Music, Berlin, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_128, folder=False,mode='play_yt',)
    Add_Dir(name="Water Music, Jordi Savall, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_129, folder=False,mode='play_yt',)
    Add_Dir(name="Fireworks Music, Jordi Savall, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_130, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='holtz_menu')
def Holtz_Menu():
    Add_Dir(name="The Planets, Op.32, Warsaw Philharmonic, added Apr 18", url=BASE3+YOUTUBE_CHANNEL_ID_189, folder=False,mode='play_yt',)
    #Add_Dir(name="Fire, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_130, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='rimsky_korsakhov_menu')
def Rimsky_Korsakhov_Menu():
    Add_Dir(name="Scheherazade, Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_21, folder=False, mode='play_yt',)
    Add_Dir(name="Fantasy on Russian Themes Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_21, folder=False, mode='play_yt',)
    Add_Dir(name="Flight of the Bumblebee, Russian National Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_93, folder=False, mode='play_yt',)
    Add_Dir(name="The Imperial March, Vienna Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_94, folder=False, mode='play_yt',)
    Add_Dir(name="Capriccio Espagnol, Berlin Philharmonic", url=BASE3+YOUTUBE_CHANNEL_ID_91, folder=False,mode='play_yt',)
    Add_Dir(name="Scheherazade, Kuerti, Frankfurt RS, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_133, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='chopin_menu')
def Chopin_Menu():
    Add_Dir(name="Concertos 1 and 2, trifanov-Pletnev, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_134, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='berlioz_menu')
def Berlioz_Menu():
    Add_Dir(name="Romeo and Juliette, RFO, added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_135, folder=False,mode='play_yt',)
    Add_Dir(name="Symphonie Fantastiqes, Estrada, Added Dec 17", url=BASE3+YOUTUBE_CHANNEL_ID_136, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)

@route(mode='nielsen_menu')
def Nielsen_Menu():
    Add_Dir(name="Soundtracks only - Symphonies 1 to 6", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)


@route(mode='benjamin_britten_menu')
def Benjamin_Britten_Menu():
    Add_Dir(name="War Requiem, German Orchstra", url=BASE3+YOUTUBE_CHANNEL_ID_106, folder=False, mode='play_yt',)
    Add_Dir(name="War Requiem, Marin Alsop", url=BASE3+YOUTUBE_CHANNEL_ID_107, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto, BBC Proms", url=BASE3+YOUTUBE_CHANNEL_ID_108, folder=False, mode='play_yt',)
    Add_Dir(name="A Ceremony of Carols, St Jacobs Vokalensemble", url=BASE3+YOUTUBE_CHANNEL_ID_109, folder=False, mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)


@route(mode='ravel_menu')
def Ravel_Menu():
    Add_Dir(name="Bolero, Gergiev, London Symphony Orchestra", url=BASE3+YOUTUBE_CHANNEL_ID_71, folder=False, mode='play_yt',)
    Add_Dir(name="Piano Concerto No 6 in G Major, Yuja wang, Camerata Salzburg", url=BASE3+YOUTUBE_CHANNEL_ID_95, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)



@route(mode='baroque_menu')
def Baroque_Menu():
    Add_Dir(name="Baroque Music ", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)
    #Add_Dir(name="", url=BASE3+YOUTUBE_CHANNEL_ID_, folder=False,mode='play_yt',)


@route(mode='compilations_menu')
def Compilations_Menu():
    Add_Dir(name="XMAS in Vienna 2015, Ortner, added Dec 17",url=BASE3+YOUTUBE_CHANNEL_ID_137, folder=False,mode='play_yt',)
    Add_Dir(name="XMAS in Vienna 2016, Ortner, added Dec 17",url=BASE3+YOUTUBE_CHANNEL_ID_138, folder=False,mode='play_yt',)
    Add_Dir(name="XMAS in Vienna 2008, Chichon, added Dec 17",url=BASE3+YOUTUBE_CHANNEL_ID_139, folder=False,mode='play_yt',)
    Add_Dir(name="XMAS in Vienna 1999, The Three Tenors, added Dec 17",url=BASE3+YOUTUBE_CHANNEL_ID_140, folder=False,mode='play_yt',)




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