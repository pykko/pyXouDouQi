#!/usr/bin/env python3
# coding: utf-8

from Direction import Direction

class Position :
	
	
	def __init__( self , ligne = None , colonne = None ) :
		self.ligne = ligne
		self.colonne = colonne
		
		
	def getNord( self ) :
		
		ligne = self.ligne - 1
		
		if ligne < 1 :
			return None
		else :
			return Position( ligne , self.colonne )
		
	
	def getOuest( self ) :
		
		colonne = self.colonne - 1
		
		if colonne < 1 :
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
		
	
		
	def __str__( self ) :
		return '({0},{1})'.format( self.ligne , self.colonne )
		
		
if __name__ == '__main__' :
	
	p = Position( 2 , 3 )
	print( p )
	print( p.getNord() )
	print( p.getEst() )
	print( p.getSud() )
	print( p.getOuest() )
	
	
