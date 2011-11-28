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
# ./modules/example.py: An example module.
###########################################################################

def mode_E(): # If arguments are defined, put them into the brackets!
	log(":)", "Using the example module!") # Logging function

def __init__(self):
	#self.addMode(MODE, FUNCTION, ARGUMENTS)
	self.addMode("E", mode_E, 0)
