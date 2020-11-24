#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  combinations.py
#  
#  Copyright 2020 William Martinez Bas <wmartinez@metfar>
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
#  

from lop  import  *;

def listToSet(x):
	return(str(x).replace('[','{').replace(']','}').replace("'",""));


def Combinations(n=1,k=1,tablePrinted=False):
	var=[1,0];
	VARS={};
	numOfVars=n;
	numOfPlaces=k;
	
	
	condition=str(numOfPlaces)+"==(0";
	for f in range(numOfVars):
		VARS["_V"+str(f+1)]=var;
		condition+="+"+"_V"+str(f+1);
	condition+=")";
	print(	"""
Number of symbols to allocate:\t\t"""+		str(numOfVars)+"""

Number of locations to be place in:\t"""+	str(numOfPlaces)+"""

ValidationCondition:\t"""+condition+"""
			""");
	
	RES=[	{
			"name"	:	"_ValidCombination",
			"value"	:	condition
			}
		];
	
	Evaluation=chipEvaluator(VARS,RES);
	
	from tomd import Tomd;
	Table=Tomd(Evaluation).markdown.replace(cSpace," ");
	ResTable=Table.split("\n");
	num=len(ResTable[3].split())-2;
	tot=0;
	elements=ResTable[1].replace("|","").split()[:-1];
	elements=[elem[1:] for elem in elements];
	print("Elements:\t",listToSet(elements));
	print("\nCombinations:\n{");
	for f in ResTable:
		row=[n for n in f.split()];
		if(len(row)>num and str(row[num])=="1"):
			#print(f);
			o=f.replace("|","").split();
			print("\t{",end=" ");
			for g in range(len(o)-1):
				if(TF(o[g])==1):
					print(elements[g],end=" ");
			print("}");
			tot+=1;
	
	print(("\t"*numOfPlaces)+"}\nTotal of valid results: ",tot);
	
	if(tablePrinted):
		print("\n",Table);
	return(0);
	
def main(args):
	Combinations(5,2,True);
	return(0);

if __name__ == '__main__':
    exit(main(sys.argv));
