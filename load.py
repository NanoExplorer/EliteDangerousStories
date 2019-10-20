try:
	import Tkinter as tk
except ModuleNotFoundError:
	import tkinter as tk

import traceback
import sys
import json
this = sys.modules[__name__]#Not entirely sure what that's all about...
from missions.crcr import CrcrMission
from missions.fsdb import FsdbMission

def plugin_start(plugin_dir):
	print(sys.version)
	print("Loaded! {}".format(plugin_dir))
	plugin_dir = plugin_dir + '\\'
	this.mission=Mission(plugin_dir)
	this.mission.add_module(CrcrMission(plugin_dir))
	this.mission.add_module(FsdbMission(plugin_dir))
	return "Test"

def plugin_app(parent):
	label=tk.Label(parent,text="COBRA:")
	this.status = tk.Label(parent,anchor=tk.W,text="Welcome to the Canonn On BoaRd Assistant.\nStart a mission by collecting one of the following:\nMeta alloy or Thargoid Organic Circuitry\nOr by docking at Meene.")
	this.mission.load()
	this.status.bind("<Button-1>",onclick)
	return (label,this.status)

def journal_entry(cmdr,is_beta,system,station,entry,state):
	#text = ""
	#for key,value in entry.items():
	#	text = text + key + " " + value + '\n'
	#print(state)
	if entry['event']=='Scan' and 'Volcanism' in entry and 'major' in entry['Volcanism'].lower():
		this.status['text']='MAJOR VOLCANISM DETECTED!'
	elif entry['event']=='Scan':
		this.status['text']=''
	#print(state)
	this.mission.update(entry,state)

def onclick(*args):
	this.mission.update({},{},click=True)

def plugin_stop():
	this.mission.save()


class Mission():

	def __init__(self,locpath):
		self.modules = []
		self.fileloc = locpath

	def add_module(self,module):
		#A module is a python object with an update method that returns a string.
		#The string is what's displayed to the user.
		#update should return none *most* of the time.
		#A decent template can be found in missions\basemission.py
		#We also expect the module to have load and save methods.
		self.modules.append(module)

	def update(self,entry,state,click=False):
		changed=False
		totalResultText = ""
		for m in self.modules:
			u = m.update(entry,state,click)
			if u is not None:
				changed = True
				totalResultText += u + '\n\n'
		if changed:
			this.status['text'] = totalResultText.strip()
		#if click:
		#	this.status['text']="OW STOP HITTING ME"

	def load(self):
		try:
			with open(self.fileloc+'mission_globals','r') as savefile:
				this.status['text'] = savefile.read()
		except:
			print('global_savefile not found - if you think you should have a global save file, uncomment the following line.')
			#traceback.print_exc()
		for m in self.modules:
			m.load()

	def save(self):
		with open(self.fileloc+'mission_globals','w') as savefile:
			savefile.write(this.status['text'])
		for m in self.modules:
			m.save()


	
