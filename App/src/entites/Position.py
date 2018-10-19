#!/usr/bin/env python3
# coding: utf-8

from Direction import Direction

class Position :
	
	
	def __init__( self , ligne = None , colonne = None ) :
		self.ligne = ligne
		self.colonne = colonne
		
		
	def getNord( self , limite = 1 ) :
		
		ligne = self.ligne - 1
		
		if ligne < limite :
			return None
		else :
			return Position( ligne , self.colonne )
		
	
	def getOuest( self , limite = 1) :
		
		colonne = self.colonne - 1
		
		if colonne < limite :
			return None
		else :
			return Position( self.ligne , colonne )
			
	
	def getSud( self , limite = None ) :
		
		ligne = self.ligne + 1
		
		if limite != None and ligne > limite :
			return None
		else :
			return Position( ligne , self.colonne )
		
		
	def getEst( self , limite = None) :
		
		colonne = self.colonne + 1
		
		if limite != None and colonne > limite :
			return None
		else :
			return Position( self.ligne , colonne )
		
			
	def __eq__( self , autre ) :
		if self.ligne == autre.ligne and self.colonne == autre.colonne :
			return True
		else :
			return False
		
		
	def __str__( self ) :
		return '({0},{1})'.format( self.ligne , self.colonne )
		
		
if __name__ == '__main__' :
	
	p = Position( 2 , 3 )
	print( p )
	print( p.getNord() )
	print( p.getEst() )
	print( p.getSud() )
	print( p.getOuest() )
	
	p1 = Position( 4 , 5 )
	p2 = Position( 3 , 5 )
	p3 = Position( 4 , 5 )
	
	print( p1 == p2 )
	print( p1 == p3 )
	
	
