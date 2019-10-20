from missions.basemission import MissionModule
from missions.fsdb_strings import localize

def atleast(x):
	return lambda y: y>= x
"""Note: this module introduces the idea of clicking on the text to advance.
I've put a permanent on-click handler on the text of the mission. It shouldn't do
anything unless you're waiting for a 'click' type of event."""

def lessthan(x):
	return lambda y: y<x
def sequential(y):
	return {x:[x+1] for x in range(y)}
class FsdbMission(MissionModule):
	def __init__(self,filepath):
		MissionModule.__init__(self,filepath)
		self.fileloc=filepath+"FsdbProgress"
		s=localize(filepath)
		self.strings=s
		self.stages=[
		('entry',{'event':'Docked','StarSystem':'Meene'},s.mission_intro),
		('complicated',self.find_fuel_scoop,s.fuel_scoop),
		('entry',{"event":"FSDJump", "StarSystem":"Synuefe NL-N c23-4"},s.enter_system),
		('entry',{"event":"Bounty", 
			"Target":"Skimmer", 
			"Reward":0, 
			"VictimFaction":"$faction_none;"},s.killed_sentinel),
		('state',["Manufactured","guardian_powercell"],atleast(21),""),
		('state',["Manufactured","guardian_techcomponent"],atleast(21),""),
		('stagescomplete',[4,5],s.guardian_mats_acquired),
		('click',s.pylons_charged),
		('entry',{'event':'CollectCargo','Type':'AncientRelic'},s.relic_acquired),
		('entry',{'event':'MaterialCollected','Name':'guardian_moduleblueprint'},self.check_focus),
		('state',['Cargo','hnshockmount'],atleast(8),s.shockmounts_acquired),
		('complicated',self.end_mission_handler,s.mission_complete)
		]
		self.stagesPath=sequential(len(self.stages)-1)

	def check_focus(self,state,entry):
		if 'focuscrystals' not in state['Manufactured'] or state['Manufactured']['focuscrystals']<24:
			return self.strings.blueprint_acquired + " " + self.strings.doesnt_have_focus
		else:
			return self.strings.blueprint_acquired
	def find_fuel_scoop(self,state,entry):
		if entry["event"]=="Undocked":
			fs=False
			disco=False
			srv=False
			for k,v in state['Modules'].items():
				if 'fuelscoop' in v['Item']:
					print("Match!FS")
					fs=True
				if 'stellarbodydiscoveryscanner' in v['Item']:
					disco=True
				if 'buggybay' in v['Item']:
					srv=True
			return fs and disco and srv

	def end_mission_handler(self,state,entry):
		if entry['event']=='TechnologyBroker' and 'ItemsUnlocked' in entry:
			for itemUnlocked in entry['ItemsUnlocked']:
				if 'Booster' in itemUnlocked['Name']:
					print(itemUnlocked['Name'])
					return True
