#!/usr/bin/env python3
# coding: utf-8


from Joueur import Joueur
from Position import Position

class Case :
	
	TERRE = 0
	EAU = 1
	PIEGE = 2
	TANIERE = 3
	
	
	def __init__( self , position , terrain = TERRE , joueur = None ) :
		self.position = position
		self.terrain = terrain
		self.joueur = joueur
		
	
		
		
	def __str__( self ) :
		return '{0}:{1}:{2}'.format( self.position , self.terrain , self.joueur)
		

