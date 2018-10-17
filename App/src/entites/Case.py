#!/usr/bin/env python3
# coding: utf-8


from Joueur import Joueur
from Position import Position
from Direction import Direction

class Case :
	
	TERRE = 0
	EAU = 1
	PIEGE = 2
	TANIERE = 3
	
	
	def __init__( self , position , terrain = TERRE , joueur = None ) :
		self.position = position
		self.terrain = terrain
		self.joueur = joueur
		
		
	def getVoisine( self , direction ) :
		
		if direction == Direction.EST :
			return self.position.getEst()
		elif direction == Direction.OUEST :
			return self.position.getOuest()
		elif direction == Direction.NORD :
			return self.position.getNord()
		elif direction == Direction.SUD :
			return self.position.getSud()
		
	def __str__( self ) :
		return '{0}:{1}:{2}'.format( self.position , self.terrain , self.joueur)
		

