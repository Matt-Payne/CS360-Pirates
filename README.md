# CS360-Pirates
repo for my python project
CHRISTOPHER	NEWPORT	UNIVERSITY
DEPARTMENT	OF	PHYSICS, COMPUTER	SCIENCE	& ENGINEERING
CPSC 360 - CONCEPTS	IN	PROGRAMMING	LANGUAGES
*	Assignment	4:	Python:	Jack	Sparrow *
Instructor:	Dr.	Roberto	A.	Flores
Goal
Use	Python for	problem	solving.
Description
Jack	Sparrow and	his	crew	gazed	happily	upon	the	chest	brimming	with	gemstones.	Diamonds,	rubies,
sapphires,	opals,	and	many	other	kinds	of	gems	added	to	the	sparkling	collection.
“We’re	rich,	my	lads!”	he	said,	“Now,	here’s	what	we’re	going	to	do.	Each	of	us	will	take	two	stones
now,	then	we’ll	bury	the	rest	because...because	that’s	what	pirates	do!”
“Who	chooses	first?”	asked	the	kitchen boy,	fearing	that	he	already	knew	the	answer.
“I’ll	choose	one	first,”	said	Sparrow,	“and	then	each	man	from	there	in	order	of	rank,	starting	with	the
first	mate	down	to	the	kitchen boy”.	The	lower-ranked	crew	members	began	to	grumble.	“Then,” said
Sparrow,	“the	kitchen boy	immediately	chooses	his	second	gem,	and	we	proceed	in	reversed	order	until
we	get	to	me,	and	I	will	be	the	last	to	choose	my	second	stone.”
The	crew	quickly	agreed	and,	almost	as	quickly,	began	trying	to	figure	how	to	claim	the	best	stones.
Implementation
Write	a	python	file	“pirates.py”	that	has	the	function	“process(	after,	input	)”,	which receives	an	integer
(“after”)	indicating	the	number	of	pirates	who choose	a	gem after	you, and	a	list	of	tuples	(“input”)
holding	the	type	and	value	of	each	jewel.	For	example,	the	tuple	('ruby', 6000, 5000) indicates	that	there
are	two	rubies,	one	worth	6000	and	the	other	5000	doubloons.	The	function	returns	a	string	indicating
the	best	two	jewels	you	could	choose.
All	gems	in	the	input will	be	taken once each pirate has	picked two	gems. In	cases	where there are
several	gems	with the	same	value,	pirates choose	the	type	of	gem	that	is	earliest	alphabetically.
Example 1: given	1	and	[ ('ruby', 6000, 5000), ('diamond', 5000, 4000)	] as	input,	the	method	returns
"ruby:6000 diamond:4000".
Example	2:	given	3	and	[ ('Sapphire', 500, 500, 50, 50), ('Ruby', 5000, 500, 50, 5),	('Zircon', 1, 0, 0, 0),
('Diamond',	10000,	9000,	8000,	6000)	] the	method	returns	"Ruby:5000	Ruby:5".
You	can	implement	additional	functions	and	classes	if	needed.
Unit	Test
Use the	unit	test	file “piratesTest.py”	to	validate your	implementation.	This	file	must	not	be	changed	nor
its	answers	hard-coded.
Groups
This	assignment	is	done	individually.
No	code	(partially	or	totally)	should	be	taken	or	disclosed	to/from	other	people,	including	online
resources.	If	in	doubt,	read	the	“Honor	Code”	section	in	the	syllabus	or contact	your	instructor.
Submission
Your	program	must	be	written	for	Python	3.0 or	newer. Submit	your	“pirates.py”	file	to	Scholar.
l
