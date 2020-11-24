#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lop.py
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
#  	Location: 	https://github.com/metfar/logicOnPython/blob/main/lop.py
#	Project:	Logic On Python
#	URL:		https://github.com/metfar/logicOnPython

import sys;

#constants for human errors 
true=TRUE=True;
false=FALSE=False;
null=NULL=nil=NIL=None;


def TF(a):
	out=True;
	for f in ["false","0","f","none"]:
		if(f in str(a).lower()):
			out=false;
	return(out==true);
	
def Not(a):
	return((not TF(a))==true);
def Nor(a,b):
	return(Not(a) & Not(b));
def Xor(a,b):
	return(TF(a) != TF(b));
def Imp(a,b):
	return(Not(TF(a) & Not(b)));

def Nand(*args):
	out=0;
	for f in args:
		out=out | Not(f);
	return(out==true);


def Or(*args):
	out=0;
	for f in args:
		out=out | TF(f);
	return(out ==true);
	

def And(*args):
	out=1;
	for f in list(args):
		out=out & TF(f);
	return(out ==true);

	
def Iff(*args):
	out=1;
	vargs=list(args);
	while(len(vargs)>0):
		first=vargs.pop(0);
		out=(first==out);
	return(out ==true);


	
	
NOT=Not;
NAND=Nand;
AND=And;
OR=Or;
NOR=Nor;
XOR=Xor;
IFF=IFANDONLYIF=IfAndOnlyIf=Iff;
IMP=Implies=Imp;

LF="\n";
sTable="<table border=0 align=center>"+LF;	eTable="</table>"+LF;
sHead="<thead>"+LF;	eHead="</thead>"+LF;
sBody="<tbody>"+LF;	eBody="</tbody>"+LF;
sRow="<tr>"+LF;		eRow="</tr>"+LF;
sCell="<td> ";		eCell=" </td>"+LF;
cSpace="&nbsp;";	cEnter="<br />"+LF;
def chipEvaluator(VARS,RES):
	out=sTable+sHead;
	td=eCell+sCell;
	rows=1;
	cols={};
	lVars=len(VARS);
	mods=[0]*lVars;
	n=1;
	for f in VARS:
		length=len(VARS[f]);
		rows=rows*length;
		cols[f]=length;
		mods[lVars-n]=rows;
		n+=1;
	
	row=0;
	names,values=list(VARS.keys()),list(VARS.values());
	out+=sRow+sCell;
	for f in names:
		out+=f.replace("_",cSpace)+td;
		#print(f.replace("_"," "),end="\t");
	
	for f in RES:
		out+=f["name"].replace("_",cSpace)+td;
		#print(f["name"].replace("_"," "),end="\t");
	
	out+=eCell+eRow+eHead;#	print();
	out+=sBody;
	LVARS={};
	
	while(row<rows):
		out+=sRow+sCell;
		t=row;
		leRow=[0]*lVars;
		
		for f in range(len(values)-1,-1,-1):
			leRow[f] = t %  len(values[f]) ;
			t=(t-leRow[f]) // len(values[f]);
		n=0;
		val=[0]*lVars;
		for f in leRow:
			val[n]=str(values[n][f]);
			out+=val[n].center(len(names[n])).replace(" ",cSpace)+td;
			#print(val[n].center(len(names[n])),end="\t");
			cad="LVARS['"+names[n]+"']="+val[n]+";";
			n+=1;
			exec(cad);
		
		rowRes=[0]*len(RES);
		n=0;
		for f in RES:
			expression=f["value"];
			for g in names:
				if(g in expression):
					expression=expression.replace(g,"LVARS['"+g+"']");
			rowRes[n]=eval(expression);
			vale=str(1 if rowRes[n] else 0);
			out+=vale.center(len(f["name"])).replace(" ",cSpace)+td;
			#print(vale.center(len(f["name"])),"\t",end="");
			n+=1;
			
		out+=eCell+eRow;#print();
		row+=1;
	out+=eBody+eTable;
	return(out);


def main(args):
	html=0;
	var=[1,0];
	VARS={
			"_Armed"	:	var,
			"_Door"	:	var,
			"_Glass"	:	var,
			"_Motion":	var
			};
	RES=[	{
			"name"	:	"_Alarm",
			"title"	:	"Armed ∧ ( Door ∨ Glass ∨ Motion )",
			"value"	:	"AND(_Armed, OR(_Door,_Glass,_Motion ))"
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
