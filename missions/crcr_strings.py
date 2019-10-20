#I've split all the strings into a separate file so that it's easier to localize in the future if someone wants to translate this.



def localize(path):
	with open(path+'localization.txt','r') as f:
		loc = f.read().strip()

	if loc=='en':
		return EnglishStrings()

class EnglishStrings():
	meta_alloy_intro_text="""So Commander what you have here is called a Meta-Alloy,
	these things are a sort of super metal that the Thargoids
	grow on a biologically altered plant we call a Barnacle... 
	Don't ask why it's called that, the reason is lost to time 
	and rumor.  If you can get a hold of some more of that, 
	and a few other spare parts I know a guy who can make it 
	worth your while. (You'll need 50 cargo space)"""

	meta_alloy_complete="""Ok so now you've got the hard part sorted out.  
	A few other odds and ends... Let's start with the micromaterials. 
	{}
	Good luck out there, and watch out for Thargoids! It's
	rumored that they sometimes visit you when you're carrying
	Meta-Alloys..."""
	meta_alloy_progress_1 = """Great job Commander! You just need 11 more
	of those things, for a total of 16, so keep your eyes peeled."""

	micro_iron="You'll just need 26 iron."
	micro_chem="You'll just need 18 Chemical Manipulators."
	micro_both="You'll need 26 iron and 18 Chemical Manipulators."
	micro_neither="You're in luck! Looks like you've got all the needed mats!"
	microarray=[micro_neither,micro_iron,micro_chem,micro_both]
	baffle_intro="""Alright, so the next part of this little adventure is a 
	straight forward milk run. head to Sopwith Arsenal in the 
	Taevaisa System, you're going to need to pick up 22 
	Radiation baffles on your way back to a friendly system 
	where you can find a tech broker."""

	chemmanip_complete="""You've got all the chemical manipulators you need, commander!"""

	iron_complete="""You've got all the iron you need, commander!"""

	neofabric_intro="""... And now is when it gets tricky the missions that are 
	likely to give you the final portion of our little scavenger 
	hunt. You're going to need 12 tons of Neofabric Insulation. 
	Land at Thompson Dock in Varati and start looking though the 
	missions available on offer at the local mission board.  Once 
	you have everything on our list meet me at Xiaoguan Station 
	in Krinda, and I'll introduce you to One Ton Jimmy.  Jimmy 
	loves coating things in Meta Alloy. Just don't stare at his
	leg, he kinda regrets that one."""

	neofabric_complete="""See you at Xiaoguan Station in Krinda, Commander."""

	broker_dock="""Welcome to Xiaoguan Station Commander, get yourself settled in 
	and when you're ready look up Jimmy from the station services, 
	contacts registry... He's under the oh so original heading of 
	"tech broker", I guess that works and all but it just doesn't 
	have the flare of "Guy who will infuse your ship with alien 
	tech for make better boom!"... Err right.."""

	mission_complete="""I told you not to stare at his leg! Well, at least he didn't
	seem too mad about it. Enjoy your Cargo Racks Commander, 
	there is a lot of money in your future if you can figure out 
	how to use those"""
