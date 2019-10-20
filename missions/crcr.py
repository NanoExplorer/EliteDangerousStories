from missions.basemission import MissionModule
from missions.crcr_strings import localize

def atleast(x):
	return lambda y: y >= x

class CrcrMission(MissionModule):
	def __init__(self,filepath):
		MissionModule.__init__(self,filepath)
		self.fileloc=filepath+"CrcrProgress"
		s = localize(filepath)
		self.strings = s
		self.stages=[('entry',{'event':'CollectCargo',"Type":"MetaAlloys"},s.meta_alloy_intro_text), 
						#counterintuitively, that partially applied function
						#returns true when the number is greater than 0
					 ('state',['Cargo','metaalloys'],atleast(5),s.meta_alloy_progress_1),
					 ('state',['Cargo','metaalloys'],atleast(16),self.meta_alloy_complete_handler),
					 ('state',['Manufactured','chemicalmanipulators'],atleast(18),s.chemmanip_complete),
					 ('state',['Raw','iron'],atleast(26),s.iron_complete),
					 ('stagescomplete',[2,3,4],s.baffle_intro),
					 ('state',['Cargo','radiationbaffle'],atleast(22),s.neofabric_intro),
					 ('state',['Cargo','neofabricinsulation'],atleast(12),s.neofabric_complete),
					 ('stagescomplete',[5,6,7],""),
					 ('stagescomplete',[5,8],""),
					 ('entry',{'event':'Docked','StationName':'Xiaoguan Station','StarSystem':'Krinda'},s.broker_dock),
					 ('complicated',self.end_mission_handler,s.mission_complete)]
		self.stagesPath={0:[1,6,7,8,9],
						 1:[2],
						 2:[3,4,5],
						 #5:[6,7,8],
						 9:[10,11]}

	def end_mission_handler(self,state,entry):
		if entry['event']=='TechnologyBroker' and 'ItemsUnlocked' in entry:
			for itemUnlocked in entry['ItemsUnlocked']:
				if itemUnlocked['Name']=='Int_CorrosionProofCargoRack_Size4_Class1':
					return True

	def meta_alloy_complete_handler(self,state,entry):
		index = 3
		if 'chemicalmanipulators' in state['Manufactured'] and state['Manufactured']['chemicalmanipulators']>17:
			index -=2
		if 'iron' in state['Raw'] and state['Raw']['iron']>25:
			index -=1
		return  self.strings.meta_alloy_complete.format(self.strings.microarray[index])