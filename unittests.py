import load
import random
from missions.crcr import CrcrMission
test = load.Mission('.\\')
test.add_module(CrcrMission('.\\'))

#doing everything from scratch
#collect meta alloys
load.this.status = {'text':''}


class Simulator():
	def __init__(self,mission):
		self.mission=mission
		self.last_text = ""
		self.state={'Cargo': {u'explosives': 1}, 'Raw': {u'yttrium': 64, u'nickel': 163, u'polonium': 43, u'ruthenium': 10, u'germanium': 46, u'cadmium': 109, u'manganese': 155, u'zinc': 116, u'tungsten': 50, u'carbon': 58, u'arsenic': 56, u'chromium': 9, u'sulphur': 99, u'phosphorus': 74, u'mercury': 24, u'antimony': 1, u'molybdenum': 22, u'vanadium': 69, u'selenium': 56, u'zirconium': 6, u'technetium': 24, u'niobium': 94, u'tin': 48, u'tellurium': 8}, 'Manufactured': {u'mechanicalequipment': 36, u'guardian_sentinel_weaponparts': 39, u'configurablecomponents': 39, u'wornshieldemitters': 29, u'focuscrystals': 6, u'filamentcomposites': 6, u'imperialshielding': 30, u'guardian_powerconduit': 33, u'refinedfocuscrystals': 40, u'salvagedalloys': 27, u'protoheatradiators': 45, u'mechanicalcomponents': 25, u'unknownenergysource': 10, u'shieldingsensors': 30, u'mechanicalscrap': 38, u'militarysupercapacitors': 1, u'heatvanes': 10, u'compoundshielding': 9, u'temperedalloys': 3, u'conductivepolymers': 19, u'guardian_techcomponent': 7, u'tg_biomechanicalconduits': 9, u'protoradiolicalloys': 13, u'tg_propulsionelement': 12, u'gridresistors': 16, u'heatexchangers': 51, u'chemicalprocessors': 46, u'conductivecomponents': 12, u'heatconductionwiring': 93, u'unknownenergycell': 6, u'uncutfocuscrystals': 9, u'highdensitycomposites': 31, u'fedcorecomposites': 12, u'basicconductors': 112, u'fedproprietarycomposites': 12, u'guardian_powercell': 18, u'conductiveceramics': 30, u'guardian_sentinel_wreckagecomponents': 6, u'precipitatedalloys': 5, u'protolightalloys': 36, u'heatdispersionplate': 6, u'galvanisingalloys': 31, u'phasealloys': 24, u'electrochemicalarrays': 16, u'pharmaceuticalisolators': 1, u'tg_weaponparts': 3, u'unknowncarapace': 10, u'crystalshards': 19, u'tg_wreckagecomponents': 3, u'chemicaldistillery': 24, u'shieldemitters': 48, u'hybridcapacitors': 22}, 'Loan': 0, 'Rank': {u'Federation': (4, 43), u'Combat': (4, 47), u'CQC': (1, 9), u'Trade': (6, 39), u'Explore': (7, 60), u'Empire': (1, 100)}, 'Credits': 305233364, 'ShipIdent': u'crv-42', 'Encoded': {u'wakesolutions': 12, u'archivedemissiondata': 19, u'disruptedwakeechoes': 25, u'consumerfirmware': 35, u'encodedscandata': 24, u'tg_residuedata': 48, u'decodedemissiondata': 23, u'emissiondata': 31, u'tg_shipflightdata': 30, u'adaptiveencryptors': 12, u'shieldpatternanalysis': 14, u'ancientbiologicaldata': 3, u'securityfirmware': 2, u'bulkscandata': 20, u'hyperspacetrajectories': 8, u'scandatabanks': 23, u'scanarchives': 22, u'symmetrickeys': 18, u'unknownwakedata': 75, u'dataminedwake': 10, u'shieldfrequencydata': 3, u'compactemissionsdata': 5, u'encryptedfiles': 33, u'fsdtelemetry': 18, u'shielddensityreports': 24, u'encryptionarchives': 14, u'tg_compositiondata': 26, u'tg_shipsystemsdata': 12, u'tg_structuraldata': 39, u'classifiedscandata': 3, u'industrialfirmware': 3, u'scrambledemissiondata': 10, u'shieldsoakanalysis': 28, u'shieldcyclerecordings': 18, u'legacyfirmware': 36, u'embeddedfirmware': 3, u'guardian_weaponblueprint': 2, u'unknownshipsignature': 15, u'encryptioncodes': 21}, 'Captain': None,}
	def simulate_entry(self,entrytype,category,item):
		if item.lower() in self.state[category]:
			self.state[category][item.lower()] += 1
		else:
			self.state[category][item.lower()]=1
		if entrytype == 'cargo':
			return { "timestamp":"2018-09-12T04:32:19Z", "event":"CollectCargo", "Type":item,"Type_Localised":"dontuse", "Stolen":False }
		else:
			return { "timestamp":"2018-09-19T01:01:05Z", "event":"MaterialCollected",
				"Category":category, "Name":item, "Name_Localised":"dontuse", "Count":3 }

	
	def printif(self,text):
		if text != self.last_text:
			print(text)
			self.last_text=text

	def loadup_meta(self):
		print("\n\nloading meta")
		for i in range(16):
			entry = self.simulate_entry('cargo','Cargo','MetaAlloys')
			test.update(entry,self.state)
			print(i)
			self.printif(load.this.status['text'])
	def loadup_chem(self):
		print("\n\nloading chem")
		for i in range(18):
			entry = self.simulate_entry('mat','Manufactured','chemicalmanipulators')
			test.update(entry,self.state)
			print(i)
			self.printif(load.this.status['text'])
	def loadup_iron(self):
		print("\n\nloading iron")
		for i in range(26):
			entry = self.simulate_entry('mat','Raw','iron')
			test.update(entry,self.state)
			print(i)
			self.printif(load.this.status['text'])
	def loadup_neofab(self):
		print("\n\nloading neofabricinsulation")
		for i in range(12):
			entry = self.simulate_entry('cargo','Cargo','neofabricinsulation')
			test.update(entry,self.state)
			print(i)
			self.printif(load.this.status['text'])
	def loadup_radbaf(self):
		print("\n\nloading radiationbaffle")
		for i in range(22):
			entry = self.simulate_entry('cargo','Cargo','radiationbaffle')
			test.update(entry,self.state)
			print(i)
			self.printif(load.this.status['text'])



	def run_test(self):
		tests = [self.loadup_meta,
				 self.loadup_chem,
				 self.loadup_iron]
		random.shuffle(tests)
		tests += [self.loadup_radbaf,
				 self.loadup_neofab]
		tests[0]()
		tests[1]()
		tests[2]()
		tests[3]()
		tests[4]()
		
		test.update({'event':'Docked','StationName':'Xiaoguan Station','StarSystem':'Krinda'},self.state)
		print(load.this.status['text'])
		test.update({ "timestamp":"2018-08-28T03:23:25Z", "event":"TechnologyBroker","BrokerType":"human", "MarketID":3226436608, "ItemsUnlocked":[ { "Name":"Int_CorrosionProofCargoRack_Size4_Class1","Name_Localised":"$Int_CorrosionProofCargoRack_Size1_Class1_Name;" } ], "Commodities":[ { "Name":"metaalloys","Name_Localised":"Meta-Alloys", "Count":16 }, { "Name":"radiationbaffle", "Name_Localised":"Radiation Baffle","Count":22 }, { "Name":"neofabricinsulation", "Name_Localised":"Neofabric Insulation", "Count":12 } ], "Materials":[ {"Name":"iron", "Count":26, "Category":"Raw" }, { "Name":"chemicalmanipulators", "Name_Localised":"Chemical Manipulators", "Count":18, "Category":"Manufactured" } ] },self.state)
		print(load.this.status['text'])

sim = Simulator(test)
sim.run_test()