#!/usr/bin/env python3
# coding: utf-8

from Case import Case
from Direction import Direction
from Position import Position

class Plateau :

	NB_LIGNES = 9
	NB_COLONNES = 7
	
	
	def __init__( self ) :
		
		self.cases = []
		self.creer()
		self.etangs = ( Etang( 4 , 2 , 3 , 2 ) , Etang( 4 , 5 , 3 , 2 ) )
		
		
	def creer( self ) :
		
		for i in range( Plateau.NB_LIGNES ) :
			self.cases.append( [] )
			
			for j in range( Plateau.NB_COLONNES ) :
				self.cases[ -1 ].append( Case( Position( i + 1 , j + 1 ) ) )
				
		
				
		for i in range( 3 , 6 ) :
			self.cases[ i ][ 1 ].terrain = Case.EAU
			self.cases[ i ][ 2 ].terrain = Case.EAU
			self.cases[ i ][ 4 ].terrain = Case.EAU
			self.cases[ i ][ 5 ].terrain = Case.EAU
			
			self.cases[ 0 ][ 2 ].terrain = Case.PIEGE
			self.cases[ 0 ][ 4 ].terrain = Case.PIEGE
			self.cases[ 1 ][ 3 ].terrain = Case.PIEGE
			
			self.cases[ 8 ][ 2 ].terrain = Case.PIEGE
			self.cases[ 8 ][ 4 ].terrain = Case.PIEGE
			self.cases[ 7 ][ 3 ].terrain = Case.PIEGE
			
			self.cases[ 0 ][ 3 ].terrain = Case.TANIERE
			self.cases[ 8 ][ 3 ].terrain = Case.TANIERE
			

	
	def estBordEtang( self , case ) :
		for direction in ( Direction.NORD , Direction.EST , Direction.SUD , Direction.OUEST ) :
			if case.terrain = Case.TERRE :
				if case.getVoisine( direction ) != NULL and case.getVoisine( direction ).terrain == Case.EAU :
					return True
		else return False
		
	
	def getBordEtangOppose( self , case ) :
		pass
		
	
		
				
	def visualiser( self ) :
		
		for i in range( Plateau.NB_LIGNES ) :
			visu = ''
			for j in range( Plateau.NB_COLONNES ) :
				if self.cases[ i ][ j ].terrain == Case.TERRE :
					visu += '.'
				elif self.cases[ i ][ j ].terrain == Case.EAU :
					visu += '*'
				elif self.cases[ i ][ j ].terrain == Case.PIEGE :
					visu += 'X'
				elif self.cases[ i ][ j ].terrain == Case.TANIERE :
					visu += 'O'
					
			print( visu )
				
		
				

if __name__ == '__main__' :
	
		p = Plateau()
		print( p )
		p.visualiser()
		
		
		
		
	
