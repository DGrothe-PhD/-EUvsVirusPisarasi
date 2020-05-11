# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# Reminder: Be careful with Unicode, but the English file shouldn't cause any issue.
# 
# Script that extracts language fieldname from yml file
class lafi:
	infile= "en.yml"
	def __init__(self,fn):
		"""Parameter: the yml filename in ".." """
		self.SetFileName(fn)
	def SetFileName(self,fn):
		self.infile=fn
		self.outfile= "Fields_from_"+self.infile
	def GetAllFields(self):
		"""Gets all field names (expressions before ':') from a yml file"""
		self.fobj_in = open(self.infile, "r")
		self.fobj_out = open(self.outfile,"w")
		self.__c = 1
		self.FieldNames=[]
		for line in self.fobj_in:
			l = line.rstrip()
			lhs = (l.split(':'))[0]
			self.FieldNames.append(lhs)
			self.fobj_out.write("  "+lhs+"\n")
			self.__c += 1
		print("We've got ",str(self.__c)," fields in this file ",self.infile,".")
		self.fobj_in.close()
		self.fobj_out.close()
		
# Only modify down here and run the python script
def main():
	enfile = lafi("en.yml")
	enfile.GetAllFields()
	defile = lafi("de.yml")
	defile.GetAllFields()

if __name__=="__main__":
	main();