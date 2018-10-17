#!/usr/bin/env python3
# coding: utf-8


from Bondissant import Bondissant

class Tigre ( Bondissant ) :
	
	def __init__( self , couleur , position ) :
		
		Bondissant.__init__( self , couleur , 6 , position = None )
		
	
	def __str__( self ) :
		return 'Tigre >>> ' +  Bondissant.__str__( self )
		
		
if __name__ == '__main__':
	a = Tigre( 'blanc' )
	print( a )
