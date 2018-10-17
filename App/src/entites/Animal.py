#!/usr/bin/env python3
# coding: utf-8


class Animal :
	
	def __init__( self , couleur , force ) :
		self.couleur = couleur
		self.force = force
		
	def __deplacer__( self ) :
		pass
		
	def __attaquer__( self ) :
		pass
		
		
	def __str__( self ) :
		return "Force = {0}\tCouleur = {1}" .format( self.force , self.couleur )


if __name__ == '__main__':
	a = Animal( 'blanc' , 1 )
	print( a )

