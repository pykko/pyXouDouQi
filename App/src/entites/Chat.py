#!/usr/bin/env python3
# coding: utf-8



from Animal import Animal

class Chat ( Animal ) :
	
	def __init__( self , couleur ) :
		
		Animal.__init__( self , couleur , 2 )
		
	
		
	def __str__( self ) :
		return 'Chat >>> ' +  Animal.__str__( self )
