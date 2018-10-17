#!/usr/bin/env python3
# coding: utf-8



from Animal import Animal

class Elephant ( Animal ) :
	
	def __init__( self , couleur , position ) :
		
		Animal.__init__( self , couleur , 8 , position = None )
		
		
	def __str__( self ) :
		return 'Elephant >>> ' +  Animal.__str__( self )
