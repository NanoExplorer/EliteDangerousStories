#import traceback
import json
import textwrap

def fancyfmt(s):
	t = s.replace('\t','')
	u = t.replace(' \n',' ')
	v = u.replace('\n',' ')

	return textwrap.fill(v,width=60)

class MissionModule():
	def __init__(self,filepath):
		self.fileloc = filepath + "" #Override this by adding a filename to the filepath
		self.stages = []
		self.stagesPath = {}
		self.stagesInitActive = [0] 
		self.stagesActive = self.stagesInitActive
		self.stagesComplete=[]
		self.click=False
		#When you implement this class, you are encouraged to change the default values above.
		#Keep in mind though that stagescomplete and stagesactive will be overwritten by save and load methods.
	def update(self,entry,state,click):
		if click:
			self.click=True
		stagescompleted = []
		changed=False
		totalResultText = ""
		for stage in self.stagesActive:
			#print(stage,self.stagesActive)
			outcome = self.handle_mission_stage_tuple(self.stages[stage],entry,state)
			if outcome is not None:
				self.stagesComplete.append(stage)
				stagescompleted.append(stage)
				if stage in self.stagesPath:
					self.stagesActive += self.stagesPath[stage]
				if type(outcome) != str:
					#I know it's bad practice to have the same variable being multiple
					#types, but I'm going to do it anyway :P
					outcome = outcome(state,entry)
				if outcome.strip() != "":
					changed=True
				totalResultText += fancyfmt(outcome) + '\n\n'
		for stage in stagescompleted:
			self.stagesActive.remove(stage)
		if changed:
			return totalResultText.strip()
		self.click=False

	def load(self):
		try:
			with open(self.fileloc,'r') as savefile:
				dic = json.loads(savefile.read())
				self.stagesComplete = dic['complete']
				self.stagesActive = dic['active']
		except:
			print('savefilenotfound - if you think you should have a save file, uncomment the following line.')
			#traceback.print_exc()
			#Uncomment import traceback at the top too

	def save(self):
		with open(self.fileloc,'w') as savefile:
			savefile.write(json.dumps({'complete':self.stagesComplete,
				'active':self.stagesActive}))

	def handle_mission_stage_tuple(self,t,entry,state):
		if t[0]=='state':
			if self.compare_state(state,t[1],t[2]):
				return t[3]
		elif t[0]=='stagescomplete':
			if self.compare_stages(t[1]):
				return t[2]
		elif t[0]=='entry':
			#print(entry,t[1])
			if self.compare_entry(entry,t[1]):
				return t[2]
		elif t[0]=='complicated':
			if t[1](state,entry):
				return t[2]
		elif t[0]=='click':
			if self.click:
				return t[1]

	def compare_entry(self,entry,compareto):
		#print('got that far')
		for k,v in compareto.items():
			if k not in entry or entry[k] != v:
				return False
		return True

	def compare_stages(self,stagestocompare):
		complete=True
		for stage in stagestocompare:
			if stage not in self.stagesComplete:
				complete=False
		return complete

	
	def compare_state(self,state,compareto,func):
		if compareto[0] in state and compareto[1] in state[compareto[0]]:
			return func(state[compareto[0]][compareto[1]])
		else:
			return False

