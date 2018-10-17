#!/usr/bin/env python3
# coding: utf-8



from Animal import Animal

class Bondissant ( Animal ) :
	
	def __init__( self , couleur , force ) :
		
		Animal.__init__( self , couleur , force )
		
	def bondir( self ) :
		pass
	
	
