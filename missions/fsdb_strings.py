#I've split all the strings into a separate file so that it's easier to localize in the future if someone wants to translate this.



def localize(path):
	with open(path+'localization.txt','r') as f:
		loc = f.read().strip()

	if loc=='en':
		return EnglishStrings()

class EnglishStrings():
	mission_intro="""let's see what we can dig with a visit to the 
	local graveyard of an ancient civilization. 
	You might have heard of the Guardians, really who names
	 these things, anyways the Knife Armed Pr0N Elves, 
	were alive millions of years ago and amazingly their tech has
	 held up pretty well.  And what we've learned 
	from it over the couple years we've been playing 
	with it is damn fine too..  Break out your fuel scoop your disco scanner and your SRV, 
	we're going out past the edge of the bubble for this one, and no one likes any part of the 'fuel scoop speech'"""

	fuel_scoop="""We've learned a lot about the Guardians in a few years, especially the best places to loo.... 
	err 'Recover Valuable Historical Artifacts From the Ravages of Time'.
	We're sending the coordinates to your nav computer: SYNUEFE NL-N C23-4 Planet B3.  You'll need to confirm the 
	coordinates with your computer as well, safety protocols... can't just have some crazed operator flinging
	people off into the black by remote.... not that that's ever happened before.... Happy jumping Commander
	I'll be in touch when you get closer to your target."""

	enter_system="""
	*KRHSSSH* Hello commander. I see *KZZHKK*ing the structure. Remem*BZZZZZTTTTT* B 3.
	Try to pick up *ssshHHHHPOP* cells and technology
	componen*KRZZZ* while I *HHHZZZZZZ* signal.
	"""

	killed_sentinel=""" Sorry about the signal. This transmitter wasn't built for long range broadcasts.
	I mostly use it for the Canonn Radio... Anyway, Well if you've made it this far you've run into a few 
	sentinels and you've gathered up a fair bit of scrap off those little bastards...  
	Makes you wish for some grappling arms or some rope, grappling rope? Anyways, as I was trying to
	say earlier, you'll need to pick up 21 Guardian Power Cells and 21 Guardian Technology Components."""


	guardian_mats_acquired=""" hmmm... right anyways, now that 
	you've got the parts let's talk about the important bit, the blueprint... you've probably seen the Pylons 
	by now, rise up out of the ground and look all ominous yet temptingly shoot able... well when all 6 of those 
	guys are up and visible that's just what you want to do.  Move to to a Pylon and get ready to start going around 
	the site untill you've blasted those pretty little pillars into life.... 
	Shooting it for Science is what we're all about after all... You'll have to pull this off quick, 
	so get a feel for the site first and watch out for sentinels as you activate Pylons, get to it. 
	CLICK here when you've charged all the pylons.
	"""

	pylons_charged="""Alright you're doing good commander one more thing to do here (other than continue to survive, 
	watch your SRVs modules keep them refilled and refueled. )  Now you'll have seen another curious piece of Guardian 
	ephemera around, hell you might even have one in your hold, they are shiney and worthy of a pick up. 
	The Ancient Relic is what i'm talking about here, go blast one free in the pillars that hold them.
	"""

	relic_acquired="""Ok now take that relic up to the strange half domed portion of the ruins here
	(possibly include exact lat/lon of relic recepticle), there should be a glowing light where there 
	wasn't before coming out of the ground infront of this, park yourself on top of it and eject that 
	relic from your cargo, the new hole in the ground will do its job and pull that relic in, and boom, 
	you've activated a millennias old data bank... imagine what they could have done with all that time 
	to miniturize this whole thing ehh?  Get a scan off on that blue light show there in front of you 
	before the juice runs out on that battery, otherwise you've wasted a bit of time here."""

	blueprint_acquired="""That's it Commander. Unless you want to stock up on a few of these blueprints while you're here,
	get back to your ship and set your course for Thompson Dock in Varati, 
	you need to pick up 8 HN Shock Mounts and you may want to refit upon returning to the bubble before heading 
	to the final stop. """

	doesnt_have_focus="""Wait just a sec... I almost forgot, you'll need 24 focus crystals as well. 
	They shouldn't be too hard to find, but of course as soon as I said that I've ruined your luck.
	You might be able to find some at Dav's Hope, signal sources, or murd.... uhh... finding already broken
	ships whose destruction isn't on your conscience."""


	shockmounts_acquired="""Ok, last step here, bring that glittering pile of weirdness over to Coney Enterprise in Bactrimpox, 
	really the system isn't named after a horribly hemorrhagic fever reguardless of what they say in the news....  You're gonna
	meet one of Ram Tahs old disciples, he really just snagged a copy of the decryption codex and ran off but we don't talk
	about that in polite company.  Look him up on the contacts board under the tech brokers, *stupid name...*  His name's
	Dave Wang.... well I call him 3 Foot Wang, but he really doesn't like the short jokes....either way he'll get you setup
	with blueprints for Guardian FSD Boosters. """

	mission_complete="""You can tie these babies into your systems through your internals and woooo... you're results may
	vary of course depending on how you install them and what not but, most often you're gonna want the biggest one of 
	these you can afford to carry.  
	Good luck Commander, I'll let you know if you come across anything else that might be worth your time

	"""




	incase_I_cantFigureoutButton="""Hey there! I'm looking through the guardian FSD booster mission. We get notifications in the following situations when the player is at the Guardian ruins:
Player approaches ruins
Player lands/deploys SRV
Player picks up micromaterial
player kills a sentinel
player picks up cargo (like ancient relic)
player ejects cargo
player collects the blueprint
We don't get notified when they charge a pylon or finish charging all the pylons.
so i'm not sure how to break up the mission once the player reaches the ruins. I can try to put a button on the widget so that they can manually tell the mission system that they've done something. """
