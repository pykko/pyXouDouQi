#!/usr/bin/env python3
# coding: utf-8

from Case import Case
from Position import Position

class Plateau :

	NB_LIGNES = 9
	NB_COLONNES = 7
	
	
	def __init__( self ) :
		
		self.cases = []
		self.creer()
		
		
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
		
		
		
		
	
