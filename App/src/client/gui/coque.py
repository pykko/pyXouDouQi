#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.insert( 0 , '../../entites' )


from colorama import Fore , Back , Style

from Plateau import Plateau
from Case import Case
from Joueur import Joueur



if __name__ == '__main__' :
	
	joueurBlanc = Joueur( 'Erwan' )
	joueurNoir = Joueur( 'Amal' )
	plateau = Plateau( joueurBlanc , joueurNoir )
	
	plateau.visualiser()
	
	print( Fore.RED + 'pyXouDouQi\n\n' ) 
	print( Style.RESET_ALL )
	
	for i in range( Plateau.NB_LIGNES ) :

		visu = Style.RESET_ALL
		for j in range( Plateau.NB_COLONNES ) :
			if plateau.cases[ i ][ j ].terrain == Case.TERRE :
				visu += Back.GREEN
			elif plateau.cases[ i ][ j ].terrain == Case.EAU :
				visu += Back.BLUE
			elif plateau.cases[ i ][ j ].terrain == Case.PIEGE :
				visu += Back.RED
			elif plateau.cases[ i ][ j ].terrain == Case.TANIERE :
				if plateau.cases[ i ][ j ].joueur == joueurBlanc :
					visu += Back.WHITE
				else : 
					visu += Back.BLACK
			
			visu += ' ' 
			
		print( visu + Style.RESET_ALL )
	
	print( Style.RESET_ALL + Back.BLACK + Fore.WHITE )
	

