import discord
from discord.ext import commands
import asyncio
import random
import pickle
import os

description = """ This bot is for helping people find collabs
more efficiently. 
"""

bot = commands.Bot(command_prefix='~', description=description)

class profile():

    def __init__( self, name ):
        self.name           = name
        self.hiatus         = True
        self.yt_link        = None
        self.sc_link        = None
        self.deviant_link   = None
        self.subscriptions  = []
        # self.subscribers    = []
        self.collabs        = []
        self.artist         = False
        self.animate        = False
        self.mix            = False
        self.vocals         = False
        self.tune           = False
        self.available      = { "art": False, "animate": False, "mix": False, "vocal": False, "tune": False }
     
    def set_availability( self, key, val ):
        if( key in self.available ):
            if( val.lower() == "false" ):
                self.available[ key ] = False
            elif ( val.lower() == "true" ):
                self.available[ key ] = True
            else:
                return( "ERROR, unable to set availability for {0} to value {1}".format( key, val ) )
        
            return( "availability of {0} updated to {1}".format( key, val ) )
        else:
            return( "Invalid availability key {0}".format( key ) )
     
     
    def set_artist( self, val ):
        if( val.lower() == "false" ):
            self.artist = False
        elif ( val.lower() == "true" ):
            self.artist = True
        else:
            return( "ERROR, unable to set artist to value {0}".format( val ) )
        
        return( "artist updated to {0}".format( self.artist ) )
        
    def set_animate( self, val ):
        if( val.lower() == "false" ):
            self.animate = False
        elif ( val.lower() == "true" ):
            self.animate = True
        else:
            return( "ERROR, unable to set animate to value {0}".format( val ) )
        
        return( "animate updated to {0}".format( self.animate ) )
        
    def set_mix( self, val ):
        if( val.lower() == "false" ):
            self.mix = False
        elif ( val.lower() == "true" ):
            self.mix = True
        else:
            return( "ERROR, unable to set mix to value {0}".format( val ) )
        
        return( "mix updated to {0}".format( self.mix ) )
        
    def set_vocals( self, val ):
        if( val.lower() == "false" ):
            self.vocals = False
        elif ( val.lower() == "true" ):
            self.vocals = True
        else:
            return( "ERROR, unable to set vocals to value {0}".format( val ) )
        
        return( "vocals updated to {0}".format( self.vocals ) )
        
    def set_tune( self, val ):
        if( val.lower() == "false" ):
            self.tune = False
        elif ( val.lower() == "true" ):
            self.tune = True
        else:
            return( "ERROR, unable to set tune to value {0}".format( val ) )
        
        return( "tune updated to {0}".format( self.tune ) )
        



class collaborator():

    def __init__():
        pass

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.group(pass_context=True)
async def awesome(ctx): 
    if ctx.invoked_subcommand is None:
        await bot.say( "Of course {0.subcommand_passed} is cool!".format(ctx))
        
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))
      
        
        
        
        
        
        
        
bot.run('MzY3NDE5NDc1ODAyMzI1MDIz.DL7Tcg.9XiuryVqkQ_-wu9ozMH7FyVSxOM')