#!/usr/bin/env python3
# coding: utf-8



from Bondissant import Bondissant

class Lion ( Bondissant ) :
	
	def __init__( self , couleur ) :
		
		Bondissant.__init__( self , couleur , 7 )
		
	
	def __bondir__() :
		pass
		
	def __str__( self ) :
		return 'Lion >>> ' +  Bondissant.__str__( self )
