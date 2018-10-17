#!/usr/bin/env python3
# coding: utf-8



from Animal import Animal

class Panthere ( Animal ) :
	
	def __init__( self , couleur , position ) :
		
		Animal.__init__( self , couleur , 5 , position = None )
		
	
		
	def __str__( self ) :
		return 'Panthere >>> ' +  Animal.__str__( self )
