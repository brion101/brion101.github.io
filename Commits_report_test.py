import unittest

from  Commits_report import *

class Commits(unittest.TestCase):

	#################################################################################################################################
	#       
	#  Test the Commits report process 
	#	
	#################################################################################################################################
	
	def setUp(self):
		self.commit =  Commit()
		print "ok"
 
	def test_Commits_report(self):
		print "ok1"
		# Populate the commit object with data 
		self.commit.revision = 'r12345'
		self.commit.author = 'user.name'
		self.commit.date = '2015-11-27 09:46:32 +0000 (Fri, 27 Nov 2015)'
		self.commit.filetypes = dict()
		self.commit.filetypes["xml"] = 4
		self.commit.filetypes["java"] = 4
		self.commit.filetypes["properties"] = 20
		self.commit.filetypes["gradle"] = 1
		# Check for a length of 4 in the file types dict 
		commitData = self.commit
		self.assertEquals(4, len(commitData.filetypes))
		dateParts = commitData.date.split() 
		self.assertEquals('2015-11-27',dateParts[0])
		self.assertEquals('09:46',dateParts[1][0:5])
		self.assertEquals('user.name',commitData.author)
if __name__ == '__main__':
    unittest.main()
