import unittest

from DBSCarRental import *

class DBSCarRentalsTest(unittest.TestCase):

	#################################################################################################################################
	#       N O T E   !!!!!  N O T E   !!!!!  N O T E    !!!!!  N O T E   !!!!!  N O T E   !!!!!  N O T E
	#
	#	When running the tests below there is some user interaction required (namely: after some actions execute, the return key is requested)
	#
	#
	#################################################################################################################################
	
    def setUp(self):
        self.Stock =  DBSCarRentals()
        print "ok"

    def test_DBSCarRentals(self):
		print "ok1"
		# 40 car objects should already on list, check
		self.assertEquals(40, len(self.Stock.getCarsInStock()))
		# Call add customer no 2 times, check number is 3
		custno = self.Stock.addCustomerNo()
		custno = self.Stock.addCustomerNo()
		self.assertEquals(3 , self.Stock.addCustomerNo())
		# Rent 4 cars for a customer , then check count for cars rented for the customer   
		self.Stock.rentacar('PetrolCar',4)
		self.Stock.rentacar('PetrolCar',4)
		self.Stock.rentacar('PetrolCar',4)
		self.Stock.rentacar('PetrolCar',4)
		self.assertEquals(4 , len([ x for x in self.Stock.getCarsInStock() if x[1] == True and x[2] == 4]))  # check for rented flag true and customerno of 4 
		#  rent car for cust 5, return the cars rented to customer no 4, then check the list again for cust4 (there shoould be no cars rented)
		self.Stock.rentacar('PetrolCar',5)
		self.Stock.returnacar(4)
		self.assertEquals(0, len([ x for x in self.Stock.getCarsInStock() if x[1] == True and x[2] == 4]))  # check for rented flag true and customerno of 4 
        # Now check 1 car still rented for customer no 5
		self.assertEquals(1, len([ x for x in self.Stock.getCarsInStock() if x[1] == True and x[2] == 5]))  # check for rented flag true and customerno of 5 
		# now rent various other cars for customer no 5   (bring total to 5), then check for 5 rented
		self.Stock.rentacar('ElectricCar',5)
		self.Stock.rentacar('HybridCar',5)
		self.Stock.rentacar('DieselCar',5)
		self.Stock.rentacar('ElectricCar',5)
 		self.assertEquals(5, len([ x for x in self.Stock.getCarsInStock() if x[1] == True and x[2] == 5]))  # check for rented flag true and customerno of 5 
		# check number of cars available for rest should be 36 (5 currently rented for customer 5)
		self.assertEquals(35, len([ x for x in self.Stock.getCarsInStock() if x[1] == False 	]))  # check for rented flag false
		# return all cars for customer 5, then check list for 0 for the customer 
		self.Stock.returnacar(5)
		self.assertEquals(0, len([ x for x in self.Stock.getCarsInStock() if x[1] == True and x[2] == 5]))  # check for rented flag true and customerno of 5 
		
	
if __name__ == '__main__':
    unittest.main()
