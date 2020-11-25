#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  xor.py
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
#  	Location: 	https://github.com/metfar/logicOnPython/blob/main/xor.py
#	Project:	Logic On Python
#	URL:		https://github.com/metfar/logicOnPython

import sys;
from lop import *;


def main(args):
	html=0;
	var=[1,0];
	VARS={
			"_P"	:	var,
			"_Q"	:	var
			};
	RES=[	
			{
			"name"	:	"(P ∧ Q)",
			"value"	:	"AND(_P,_Q)"
			},
			{
			"name"	:	"(P ⊽ Q)",
			"value"	:	"NOR(_P,_Q)"
			},
	
			{
			"name"	:	"_OUT_MINE=(P ∧ Q) ⊽ ( P ⊽ Q )",
			"value"	:	"NOR(AND(_P,_Q),NOR(_P,_Q))"
			},
			{
			"name"	:	"(P⊼P)",
			"value"	:	"NAND(_P,_P)"
			},
			{
			"name"	:	"((P⊼P)⊼Q)",
			"value"	:	"NAND(NAND(_P,_P),_Q)"
			},
			{
			"name"	:	"(Q⊼Q)",
			"value"	:	"NAND(_Q,_Q)"
			},
			{
			"name"	:	"((Q⊼Q)⊼P)",
			"value"	:	"NAND(NAND(_Q,_Q),_P)"
			},
			{
			"name"	:	"_OUT_OPT=((P⊼P)⊼Q)⊼((Q⊼Q)⊼P)",
			"value"	:	"NAND(NAND(NAND(_P,_P),_Q),NAND(NAND(_Q,_Q),_P))"
			},
			{
			"name"	:	"_XOR=(P⊻Q)",
			"value"	:	"XOR(_P,_Q)"
			}
		];
	
	Evaluation=chipEvaluator(VARS,RES);
	
	if(not html):
		try:
			from tomd import Tomd;
			print(Tomd(Evaluation).markdown.replace(cSpace," "));
		except:
			print("MarkDown format requires Tomd library installed.\nPlease install it doing * pip install tomd *\n");
			exit(1);
	else:
		print(Evaluation);
	return(0);


if __name__ == '__main__':
    exit(main(sys.argv));
