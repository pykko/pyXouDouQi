#!/usr/bin/env python3
# coding: utf-8



from Animal import Animal

class Chien ( Animal ) :
	
	def __init__( self , couleur , position ) :
		
		Animal.__init__( self , couleur , 3 , position = None )
		
	
		
	def __str__( self ) :
		return 'Chien >>> ' +  Animal.__str__( self )
