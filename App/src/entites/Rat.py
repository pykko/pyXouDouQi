#!/usr/bin/env python3
# coding: utf-8



from Animal import Animal

class Rat ( Animal ) :
	
	def __init__( self , couleur , position ) :
		
		Animal.__init__( self , couleur , 4 , position = None )
		
		
	def nager( self ) :
		pass
	
		
	def __str__( self ) :
		return 'Rat >>> ' +  Animal.__str__( self )
