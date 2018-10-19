#!/usr/bin/env python3
# coding: utf-8

from Position import Position

class Etang :


	def __init__( self , ligne , colonne , hauteur , largeur ) :
		self.ligne = ligne
		self.colonne = colonne
		self.hauteur = hauteur
		self.largeur = largeur
		
		
	def getBords( self ) :
		bords = []
		
		for l in range( self.ligne , self.ligne + self.hauteur ) :
			bords.append( Position( l , self.colonne - 1 ) )
			bords.append( Position( l , self.colonne + self.largeur ) )
			
		for c in range( self.colonne , self.colonne + self.largeur ) :
			bords.append( Position( self.ligne - 1 , c ) )
			bords.append( Position( self.ligne + self.hauteur , c ) )
			
		return bords
		
		
	def getBordOppose( self , position ) :
		if self.estAuBord( position ) :
			if position.colonne == self.colonne - 1 :
				return Position( position.ligne , self.colonne + self.largeur )
			elif position.colonne == self.colonne + self.largeur :
				return Position( position.ligne , self.colonne - 1 )
			elif position.ligne == self.ligne - 1 :
				return Position( self.ligne + self.hauteur , position.colonne )
			elif position.ligne == self.ligne + self.hauteur :
				return Position( self.ligne - 1 , position.colonne )
		else :
			return None
		
		
	def estDansEtang( self , position ) :
		if position.ligne >= self.ligne and position.ligne < self.ligne + self.hauteur :
			if position.colonne >= self.colonne and position.colonne < self.colonne + self.largeur :
				return True
		return False
		
		
	def estAuBord( self , position ) :
		if position in self.getBords() :
			return True
		else :
			return False
		
	def getPositions( self ) :
		positions = []
		
		for l in range( self.ligne , self.ligne + self.hauteur ) :
			positions.append( [] )
		
		
		
if __name__ == '__main__' :
	e = Etang( 4 , 2 , 3 , 2 )
	for p in e.getBords() :
		print( str( p ) )
		
	print( 'Dans' )
	for l in range( 1 , 8 ) :
		for c in range( 1 , 10 ) :
			p = Position( l , c )
			print( str( p ) , ' ' , e.estDansEtang( p ) )
			
	print( 'Au bord' )
	for l in range( 1 , 8 ) :
		for c in range( 1 , 10 ) :
			p = Position( l , c )
			print( str( p ) , ' ' , e.estAuBord( p ) )
			
	print( 'Bord opposé' )
	for l in range( 1 , 8 ) :
		for c in range( 1 , 10 ) :
			p = Position( l , c )
			print( str( p ) , ' ' , e.getBordOppose( p ) )
		
		
		
		
	
	
	
