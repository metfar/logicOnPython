#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lop_example.py
#  
#  Copyright 2020 William Martinez Bas <metfar@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  	Location: 	https://github.com/metfar/logicOnPython/blob/main/lop_example.py
#	Project:	Logic On Python
#	URL:		https://github.com/metfar/logicOnPython


from lop import *;
import os;

#os-compat clear screen

if ("ix" in os.name):
	def clrscr():
		print(chr(27)+"[2J\n");
else:
	def clrscr():
		os.system("cls | clear");

#print values
def printv(*args):
	vargs=list(args);
	out="";
	for f in vargs:
		x=str(f).strip().lower();
		if(x in ["true","false"]):			
			print("T" if ("true" in x) else "F",end="");
		else:
			print(f,end="");
	print();

# example of elementary logic gates
def main(args):
	clrscr();
	print(	"a\tb\t"+
			"¬a\t¬b\t"+
			"a∧b\t"+
			"a∨b\t"+
			"a⊼b\t"+
			"a⊽b\t"+
			"a⊻b\t"+
			"a⇒b\t"+
			"a⟺b".replace("\t","\t\r\r")); 
	for a in [1,0]:
		for b in [1,0]:
			printv(	a==true,"\t",
					b==true,"\t",
					Not(a),"\t",
					Not(b),"\t",
					And(a,b),"\t",
					Or(a,b),"\t",
					Nand(a,b),"\t",
					Nor(a,b),"\t",
					Xor(a,b),"\t",
					Imp(a,b),"\t",
					Iff(a,b));
					
	return(0);


if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));
