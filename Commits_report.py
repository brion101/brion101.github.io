#----------------------------------------------------------------------------------------------------------------------------  
# The following process will read an input file containing a sequence of commits and extract for reporting.  
# When the input file is processed, provide the following reports  
#  
# 1. Report on  each commit, userid, date time and a list of each file type with a count 
# 2. Report on the number of commits by author
# 3. Report on commits by the hour over a 24 hour period, provide visual representation
# 4. Provide general statistics  
#---------------------------------------------------------------------------------------------------------------------------- 

#----------------------------------------------------------------------------------------------------------------------------  
#  CLASSES
#---------------------------------------------------------------------------------------------------------------------------- 

class Commit:
	#----------------------------------------------------------------------------------------------------------------------------  
	#  	The commit class 
	#---------------------------------------------------------------------------------------------------------------------------- 
    def __init__(self, revision = None, author = None, date = None, filetypes = None):
        self.revision   = revision
        self.author     = author
        self.date       = date
        self.filetypes  = filetypes

    def getrevision(self):
        return self.revision

    def getauthor(self):
        return self.author

    def getdate(self):
        return self.date

    def getfiletypes(self):
        return self.filetypes

		
if __name__ == '__main__':
	#----------------------------------------------------------------------------------------------------------------------------  
	# Setup any initial varaibles 
	#---------------------------------------------------------------------------------------------------------------------------- 
	sep                   = 72*'-'
	commits               = list()
	filetypesTot          = dict() 
	author_commit_count   = dict()
	hour_commit_count     = dict()
	author                = dict()
	Change_details        = None
	index                 = 0

	#----------------------------------------------------------------------------------------------------------------------------  
	# Open the input file 
	#---------------------------------------------------------------------------------------------------------------------------- 
	changes_file = 'changes_python.txt'
	data = [line.strip() for line in open(changes_file, 'r')]
	 
	#----------------------------------------------------------------------------------------------------------------------------  
	# The following loop  will process all lines from the input file. The file contains information related to a commit process
	# Each commit process has a similar structure (as follows), parse and store data from each commit for later reporting   
	# Structure ( each commit block has a seperator line containing all '-', do detail what comes after )
	# 
	# Header line              (1) : contains a commit reference, userid, date and time of commit, save this data     
	# Detail header            (1) : ignore
	# Commit Details     (x times) : one line entry per file commited in this process, save and count file types 
	# blank  line              (1) : ignore
	# Commit Dexcription (x times) : a number of lines describing this commit (ignore)  
	#---------------------------------------------------------------------------------------------------------------------------- 
	while True:
		try:
			# parse each of the commits and put them into a list of commits
			Change_details                  = Commit()
			filetypesDict                   = dict() 
			details                         = data[index + 1].split('|')

			# Parse all the Header record info for reporting 
			Change_details.revision         = details[0].strip()
			Change_details.author           = details[1].strip()
			Change_details.date             = details[2].strip()
			
			# keep a count of commits by author 
			author_commit_count[Change_details.author] = author_commit_count.get(Change_details.author,0) + 1
			
			# keep a count of commits by Hour 
			Hour                            = (Change_details.date.split())[1][0:2]
			hour_commit_count[Hour]         = hour_commit_count.get(Hour,0) + 1
			
			# keep a count of each file type in the commit process  
			index2                          = index+3
			while len(data[index2]) > 0:
				filetype                    = data[index2].split('.')[-1]
				if len(filetype) < 15:
					filetypesTot[filetype]  = filetypesTot.get(filetype,0) + 1
					filetypesDict[filetype] = filetypesDict.get(filetype,0) + 1
				index2 = index2 + 1 
			Change_details.filetypes        = filetypesDict
			
			index                           = data.index(sep, index + 1)
			commits.append(Change_details)
		except IndexError:
			break

	#----------------------------------------------------------------------------------------------------------------------------  
	# Reverese the order of the commits, this will report the most recent first  
	#---------------------------------------------------------------------------------------------------------------------------- 
	commits.reverse()
			
	#----------------------------------------------------------------------------------------------------------------------------  
	# Prepare data for reporting 
	#---------------------------------------------------------------------------------------------------------------------------- 
	totalAuthors        = 0
	totalAuthorcommits  = 0 
	totalHour           = 0
	totalHourCommits    = 0
	author_commit_count = sorted([ (v,k) for k,v in author_commit_count.items()], reverse=True)
	filetypesTot        = sorted([ (v,k) for k,v in filetypesTot.items()], reverse=True)
	hour_commit_count   = sorted([ (k,v) for k,v in hour_commit_count.items()])
	totalsAuthorList    = list()
	totalsHourlist      = list()
	MaxHourCommit       = 0 
	maxcommit           = 0  

	#----------------------------------------------------------------------------------------------------------------------------  
	# Report  : General Details by Commit 
	#---------------------------------------------------------------------------------------------------------------------------- 	
	for  commit in commits:
		dateParts        = commit.date.split() 
		commit.filetypes = sorted([ (v,k) for k,v in commit.filetypes.items()], reverse=True)
		print " ---------------------------------------------------------------------------"
		print " Commit Author: \t %s" % (commit.author)
		print " Commit Ref:    \t %s" % (commit.revision )
		print " Commit Date:   \t %s at %s " % (dateParts[0], dateParts[1][0:5])
		print " "
		if len(commit.filetypes) > 0:
			print " Count \t Filetypes   " 
			print " ===== \t =========   " 
			for count,file in commit.filetypes:
				print  " %s \t %s  " % (count,file) 
		print " "

	#----------------------------------------------------------------------------------------------------------------------------  
	# Report  : Count Total commits by File Type 
	#---------------------------------------------------------------------------------------------------------------------------- 	
	print " "
	print " Count Total commits by File Type   "  
	print " "
	print " Count \t File Type  " 
	print " ===== \t =========  " 
	for count,file in filetypesTot:
		print  " %s \t %s  " % (count,file) 
		
	#----------------------------------------------------------------------------------------------------------------------------  
	# Report  : Count of commits by authors
	#---------------------------------------------------------------------------------------------------------------------------- 	
	print " "
	print " Count of commits by Authors   "  
	print " "
	print " Count \t Author   " 
	print " ===== \t =======   " 
	for count,author in author_commit_count:
		print  " %s \t %s  " % (count,author) 
		totalAuthors       = totalAuthors + 1
		totalAuthorcommits = totalAuthorcommits +  count

	#----------------------------------------------------------------------------------------------------------------------------  
	# Report  : Count of commits by Hour over a 24 hour period with graph 
	#---------------------------------------------------------------------------------------------------------------------------- 	
	print " "
	print " Count of commits by Hour over 24 hours Graphed "  
	print " "
	print " Hour \t Count   " 
	print " ==== \t =====   " 
	listInd = 0
	listLen = len(hour_commit_count)
	for i in range(24):
		count = 0
		#  as the list of commits by hour only contains actual hours with commits, a process is required to match with 24 hours 
		if listInd  < listLen: 
			if int(hour_commit_count[listInd][0]) == i:
				count                       = hour_commit_count[listInd][1] 
				if count > maxcommit:
					maxcommit               = count
					MaxHourCommit           = i 
				listInd                     = listInd + 1
		print  " %s \t %s \t %s " % (i,count, '-'*(count / 2)) 

	#----------------------------------------------------------------------------------------------------------------------------  
	# Do any Statistics calculations  
	#---------------------------------------------------------------------------------------------------------------------------- 
	if totalAuthors > 0:
		avgAuthorCommits = (totalAuthorcommits/totalAuthors) 

	#----------------------------------------------------------------------------------------------------------------------------  
	# Report  : General Statistics 
	#---------------------------------------------------------------------------------------------------------------------------- 	
	print " "
	print " Stats   "  
	print " ================"
	print " The Total Number of authors              \t %s " % (totalAuthors)
	print " The Total Number of commits              \t %s " % (totalAuthorcommits)
	print " The avg Number of commits By Author      \t %s " % (avgAuthorCommits)
	print " "
	print " The Hour with the most commits           \t %s  hundred Hours" % (MaxHourCommit) 