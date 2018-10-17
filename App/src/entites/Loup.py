#!/usr/bin/env python3
# coding: utf-8



from Animal import Animal

class Loup ( Animal ) :
	
	def __init__( self , couleur ) :
		
		Animal.__init__( self , couleur , 4 )
		
	
		
	def __str__( self ) :
		return 'Loup >>> ' +  Animal.__str__( self )
