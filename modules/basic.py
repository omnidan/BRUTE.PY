# Simple Bruteforcer by Daniel0108 #TheBlackMatrix			  #
# Disclaimer: This script is for educational purposes only.		  #
#		I am not responsible for how you use this program	  #
# .########..########..##.....##.########.########.....########..##....## #
# .##.....##.##.....##.##.....##....##....##...........##.....##..##..##. #
# .##.....##.##.....##.##.....##....##....##...........##.....##...####.. #
# .########..########..##.....##....##....######.......########.....##... #
# .##.....##.##...##...##.....##....##....##...........##...........##... #
# .##.....##.##....##..##.....##....##....##.......###.##...........##... #
# .########..##.....##..#######.....##....########.###.##...........##... #
###########################################################################
# Copyright (c) 2011, Daniel Bugl
# All rights reserved.
# 
# This program is licensed under the BSD license.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#    This product includes software developed by Daniel Bugl.
# 4. Neither the name of BRUTE.PY nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY Daniel Bugl ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Daniel Bugl BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###########################################################################
# Author:
#	Copyright (c) 2011 Daniel Bugl (Daniel0108)
###########################################################################
# ./modules/main.py: The main modes for BRUTE.PY
###########################################################################

def mode_h(hashmethod):
	global hashing, customhash
	hashmethod = hashmethod.lower()
	if hashmethod[0] == "c" and hashmethod[1] == ":":
		hashing = "custom"
		customhash = ':'.join(hashmethod.split(":")[1:])
	else: hashing = hashmethod

def mode_D():
	global debug
	debug = True

def mode_P():
	global use_post
	use_post = True

def mode_p(proxy):
	global proxies
	proxies = {'http': proxy}

def mode_c(charlimit):
	global chars
	chars = charlimit

def mode_l(lfile):
	global logfile
	logfile = str(lfile)

def mode_f(failstring):
	global fail
	fail = str(failstring)

def mode_L(rainbow):
	global rainbows
	rainbow_on = True
	f = open("./passwords/" + rainbow, "r")
	for r in f.readlines():
		rainbows.append(r[:-1])

def mode_t():
	global text_instead_url
	text_instead_url = True

def mode_d():
	global display_invalid
	display_invalid = False

def __init__(self):
	self.addMode("h", mode_h, 1)
	self.addMode("D", mode_D, 0)
	self.addMode("P", mode_P, 0)
	self.addMode("p", mode_p, 1)
	self.addMode("c", mode_c, 1)
	self.addMode("l", mode_l, 1)
	self.addMode("f", mode_f, 1)
	self.addMode("L", mode_L, 1)
	self.addMode("t", mode_t, 0)
	self.addMode("d", mode_d, 0)
