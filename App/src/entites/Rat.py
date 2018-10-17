#!/usr/bin/env python3
# coding: utf-8



from Animal import Animal

class Rat ( Animal ) :
	
	def __init__( self , couleur ) :
		
		Animal.__init__( self , couleur , 4 )
		
		
	def nager( self ) :
		pass
	
		
	def __str__( self ) :
		return 'Rat >>> ' +  Animal.__str__( self )
