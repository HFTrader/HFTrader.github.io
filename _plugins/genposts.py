#!/usr/bin/python
import datetime
import yaml
import os
import sys
from subprocess import Popen, PIPE


def runcmd( cmd ):
    p = Popen( cmd, shell=True )
    p.communicate()

post_tpl = """
---
layout: post
title: {title}
category: {category}
excerpt: {excerpt}
---
<img src="images/{image}" />
"""
today = datetime.datetime.now()
todaystr = today.strftime( '%Y-%m-%d' )
script_path = os.path.dirname( os.path.realpath( __file__ ) )
path = os.path.realpath( os.path.join( script_path, '..' ) )
print path, todaystr

ymlpath = os.path.join( path, "AllPosts.yml" )

def process_entry( reg ):
        dt = reg.get( 'date', todaystr )
        ex = reg.get( 'excerpt', dt )
        ex = '-'.join( ex.split() )[:25]
        categ = reg.get( 'category', 'Juicy' )
        fname = os.path.join( path, '_posts/%s-generated-%s.md' % (dt,ex) )
        post = post_tpl.format( **reg )

        with open( fname, 'w' ) as fout:
            fout.write( post )
            #print fname, post
            print "Wrote...", fname


with open( ymlpath, 'r' ) as f:
    data = f.read()
    yml = yaml.load( data )
    for reg in yml:
        process_entry( reg )

os.chdir( os.path.join( path, "_posts" ) )
runcmd( 'git add .' )
runcmd( 'git commit -a -m "Scheduled update" ' )
runcmd( 'git push' )
