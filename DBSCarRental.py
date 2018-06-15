# Define classes
 
import os 
import random

################################################################################################################################
#
# Class files  
#
################################################################################################################################

class GeneralUtil(object):
    # This class contains general purpose fuctions 
  
    def __init__(self):
		self.__count = 0
		self.__MainMenu = [('Rent a Car', 'Rent'), ('Return a Car', 'Return'), ('Select a List', 'Lists')]
		self.__RentMenu = [('Rent Petrol', 'PetrolCar'), ('Rent ElectricCar', 'ElectricCar'), ('Rent HybridCar', 'HybridCar'), ('Rent DieselCar', 'DieselCar')] 
		self.__ListMenu = [('List all Cars',1), ('List rented Cars',2), ('List available Cars',3), ('List rented by a customer',4)] 

    def Menulist(self,option):
		# This generic menu function does
		# 1. accepts a list as input, this list is used to build the menu
		# 2. prompts a uses to make a selection 
		# 3. returns the selection number ( this is the position on the input list ) 
		# 
		# The option determines which menu list is displayed 
		# 'M' = main menu 
		# 'R' = rent menu  
		# 'L' = list menu 
		if option == 'M':
			menulist = self.__MainMenu
		elif option == 'R':
			menulist = self.__RentMenu
		elif option == 'L':
			menulist = self.__ListMenu
		else:
			print " Menu option not available"
			return ""
		while True:
			os.system('cls')
			print
			print "Enter Number to Select Option "
			print 
			for index,(menuitem,data) in enumerate(menulist):
				print "     %d to %s " % (index + 1,menuitem)
			print
			print "     Q to Quit"
			print
			selection = raw_input("Please enter options : ")
			if selection.lower() == 'q':
				return selection.lower()
			try:
				selection = int(selection) - 1
				result = menulist[selection][1]
				return result 
			except:
				raw_input("Invalid option selected, press return")

				
    def getNumberValue(self,ValueName):
		# This generic function gets  number of values and returns them in a list  
		# 1. accepts name of value and number of parameters required
		# 2. prompts user to enter parameter value  
		# 3. returns a values 
		# 
		selection = 0
		os.system('cls')
		while True:  
			selection = raw_input("Please enter %s  : " % (ValueName))
			try:
				selection = int(selection)
			except:
				print "Invalid value entered"
			else:
				return selection

#
# Define a class for my car
#
class Car(object):
    
    def __init__(self,colour = 'any' ,make = 'any'):
        self.__colour = colour
        self.__make = make
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

#
# Define a Car subclass ElectricCar
#
class ElectricCar(Car):

    def __init__(self,colour,make):
		Car.__init__(self,colour,make)
		self.__NumberFuelcells = 1
		self.__EngineType =	'Electric'
		
    def getEngineType(self):
        return self.__EngineType
		
    def getNumberfuelcells(self):
        return self.__NumberFuelcells

    def setNumberfuelcells(self,value):
        self.__NumberFuelcells = value
 
#
# Define a Car subclass PetrolCar
#
class PetrolCar(Car):

    def __init__(self,colour,make):
		Car.__init__(self,colour,make)
		self.__NumberCylinder =	1
		self.__EngineType =	'Petrol'

    def getEngineType(self):
        return self.__EngineType
		
    def getNumberCylinder(self):
        return self.__NumberCylinder

    def setNumberCylinder(self,value):
        self.__NumberCylinder = value		

#
# Define a Car subclass DieselCar
#		
class DieselCar(Car):

    def __init__(self,colour,make):
		Car.__init__(self,colour,make)
		self.__NumberCylinder =	1
		self.__EngineType =	'Diesel'

    def getEngineType(self):
        return self.__EngineType
	
    def getNumberCylinder(self):
        return self.__NumberCylinder 

    def setNumberCylinder(self,value):
        self.__NumberCylinder = value		
#
# Define a Car subclass DieselCar
#	
class HybridCar(Car):

    def __init__(self,colour,make):
		Car.__init__(self,colour,make)
		self.__NumberFuelcells = 1
		self.__NumberCylinder =	1
		self.__EngineType =	'HybridCar'

    def getEngineType(self):
        return self.__EngineType
		
    def getNumberfuelcells(self):
        return self.__NumberFuelcells

    def setNumberfuelcells(self,value):
        self.__NumberFuelcells = value
		
    def getNumberCylinder(self):
        return self.__NumberCylinder 

    def setNumberCylinder(self,value):
        self.__NumberCylinder = value
		
class DBSCarRentals(object):
    # This class contains the car rental functionality and properties

    def __init__(self):
		# Setup any variables required for carrental class
        self.__CarsInStock =  list()	
        self.__CarTypes = ('PetrolCar','ElectricCar','HybridCar','DieselCar')	
        self.__CustomerNo = 0
        self.createStock()

	def getCustomerNo(self):
		return self.__CustomerNo

    def addCustomerNo(self):
		self.__CustomerNo = self.__CustomerNo + 1
		return self.__CustomerNo

    def createStockitem(self,list1):
		self.__CarsInStock.insert(len(self.__CarsInStock),list1)

    def printreturn(self):
		print ""
		raw_input("Press return to continue")
		
    def printlines(self,msg):
		print ""
		print msg
		print ""

    def printlist(self,list1):
		# list all cars in stock
		print '\t' + 'CustNo' + '\t' +'Make' + '\t' + 'Colour' + '\t' + 'Type' 
		print '\t' + '======' + '\t' +'====' + '\t' + '======' + '\t' + '====' 
		for Item in list1:
			Dcar = Item[0]
 			print '\t' , Item[2], '\t'  + Dcar.getMake() + '\t' + Dcar.getColour() +  '\t' + Dcar.getEngineType()  

    def createStock(self):
		#  Create the Stock, a car type object for each of the amounts listed below, add car objects to a single list
		#  1. Petrol cars 24
		#  2. Diesel cars 8
		#  3. Electric cars 4
		#  4. hybrid cars 4
		#
		#  There is a nested list for each car in stock (record), it is in the following format  
		#         Car object    
		#         Car rented    values True/False		
 		#         Customer No   populated if car rented
		#         Cartype       type of car  e.g petrol          
		#
		color = ['green','blue','red','black','white']
		make  = ['BMW','Ford','VW','Volvo','Toyota']
		for i in range(24):
			list1 = [PetrolCar(random.choice(color) ,random.choice(make)),False,0,self.__CarTypes[0] ]
			self.createStockitem(list1)
		for i in range(4):
			list1 = [ElectricCar(random.choice(color) ,random.choice(make)),False,0,self.__CarTypes[1]  ] 	
			self.createStockitem(list1)
		for i in range(4):
			list1 = [HybridCar(random.choice(color) ,random.choice(make)),False,0,self.__CarTypes[2]  ] 	
			self.createStockitem(list1)
		for i in range(8):
			list1 = [DieselCar(random.choice(color) ,random.choice(make)),False,0,self.__CarTypes[3]  ] 	
			self.createStockitem(list1)
			
    def getCarsInStock(self):
		return self.__CarsInStock

	
    def lists(self,listtype,customerno = 0):
		# this function will create an extracted list of items selected from the CarsInStock list depending type of request
		# list types 
		# 1 = list all cars in stock
		# 2 = list all rented 
		# 3 = list all avalible 
		# 4 = list cars rented for a customer 
		list1 = list()
		os.system('cls')
		try:
			if listtype == 1:
				self.printlines(" list all cars in stock ")
				list1 = [ x for x in self.__CarsInStock ]
			elif listtype == 2:
				self.printlines(" list all cars rented  ")
				list1 = [ x for x in self.__CarsInStock if x[1] == True ]
			elif listtype == 3:
				self.printlines(" list all cars available  ")
				list1 = [ x for x in self.__CarsInStock if x[1] == False]
			elif listtype == 4:
				self.printlines(" list all cars rented to customer number  ")
				list1 = [ x for x in self.__CarsInStock if x[1] == True and x[2] == customerno]
			else: 
				print " Print option is not avalible "
		except:
 			print " There are no items for this option "
		else:
			if len(list1) > 0:
				self.printlist(list1)
			else:
	 			print " There are no items for for this option "
		self.printreturn()
		
    def rentacar(self,cartype,customerno):
   		# rent a car
		# there is a nested list for for each car, it is in format [carobj,rented true or false, customerNo if rented, cartype]
        try:
			carpos = next( i for i,x in enumerate(self.__CarsInStock) if x[1] == False and x[3] == cartype)
        except:
			print " No Cars avaliable for car type : " , cartype 
        else:
			self.__CarsInStock[carpos][1] = True
			self.__CarsInStock[carpos][2] = customerno
			print " A car of type %s has been rented for customer number %d " % (cartype,customerno) 
		self.printreturn()

    def returnacar(self,customerno):
 		# Return a car
		# this function will search the CarsInStock list for a customer number and sets rented flag to false when found (returned) 
		count = 0
		for i,x in enumerate(self.__CarsInStock):
			if x[2] == customerno:
				self.__CarsInStock[i][1] = False
				self.__CarsInStock[i][2] = 0 
				count = count + 1
		if count > 0 :
			print "%d cars have now been returned from customer %d " % (count,customerno) 
		else:
			print ""
			print "There are No cars currently rented for  customer %d " % (customerno) 
		self.printreturn()

if __name__ == '__main__':

	#  Create objects for generalutil and DBScarRentals classes
	general_util = GeneralUtil()
	Stock = DBSCarRentals()


	while True:
	#   This is the main process, it does the following steps 
	#
	#   1. Call a generic menu function to display a main menu,  
	#   2. Based on selection from main menu, process the requested option 
	#
	#   Repeat above steps until quit is choosen  (q)

	
	#   Call general menu function with option 'M' (main menu)
		menuoption = general_util.Menulist('M')
		if menuoption == "q":
			break

		#   Process the option take from the main menu 
		if menuoption == "Rent":
			customerno = Stock.addCustomerNo()
			# show the rent menu and process request
			while True:
				menuoption = general_util.Menulist('R')
				if menuoption == "q":
					break
				# Call the rentacar function
				Stock.rentacar(menuoption,customerno)
 		elif menuoption == "Return":	
			#   Get a customer number and reset any rented cars for the customer no
				customerno = general_util.getNumberValue("Customer Number")
				Stock.returnacar(customerno) 
		elif menuoption == "Lists":	
			while True:
				menuoption = general_util.Menulist('L')
				if menuoption == "q":
					break
				customerno = 0
				# if list selection is for customer (list option 4), get a customer number 
				if menuoption == 4:
					customerno = general_util.getNumberValue("Customer Number")
				Stock.lists(menuoption,customerno)
		else:
			print ""
			print " Selection unknown "
			print ""
			raw_input("press return")
		
