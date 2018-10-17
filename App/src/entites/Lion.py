#!/usr/bin/env python3
# coding: utf-8



from Bondissant import Bondissant

class Lion ( Bondissant ) :
	
	def __init__( self , couleur , position ) :
		
		Bondissant.__init__( self , couleur , 7 , position = None )
		
			
	def __str__( self ) :
		return 'Lion >>> ' +  Bondissant.__str__( self )
