#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect(":memory:");

def run_in_db(txt):
    # print "running: " + txt
    conn.execute(txt)

def create_table( tbl_name, *rest):
    qry = "CREATE TABLE " + tbl_name + " (" + tbl_name + " text, "
    for r in rest:
        qry = qry  + r + " text, "

    p_val = "p_" + tbl_name
    qry = qry + p_val + " reat)"
    run_in_db( qry)
    return p_val
    
def fill_data( tbl_name, y_val, *rest):
    qry = "INSERT INTO " + tbl_name + " VALUES ('{}', "
    for r in rest:
        qry = qry + "'{}', ".format( r)

    qry = qry + "{})"
    run_in_db( qry.format('y', y_val))
    run_in_db( qry.format('n', (1-y_val)))

# rc = sqlite3_open(":memory:", &db);

# cur=conn.cursor

sum_str = create_table( "a")
fill_data( "a", 0.01)

# conn.execute('''CREATE TABLE t (t text, a text, p_t real)''')
sum_str  += " * " + create_table( "t", "a")
fill_data("t", 0.05, 'y')
fill_data("t", 0.01, 'n')

sum_str  += " * " + create_table("s")
fill_data("s", 0.5)

sum_str  += " * " + create_table("l", "s")
fill_data("l", 0.1, "y")
fill_data("l", 0.01, "n")

sum_str  += " * " + create_table("b", "s")
fill_data("b", 0.6, "y")
fill_data("b", 0.3, "n")

sum_str  += " * " + create_table("e", "l", "t")
fill_data("e", 1, "y", "y")
fill_data("e", 1, "y", "n")
fill_data("e", 1, "n", "y")
fill_data("e", 0, "n", "n")

sum_str  += " * " + create_table("x", "e")
fill_data("x", 0.98, "y")
fill_data("x", 0.05, "n")

sum_str  += " * " + create_table("d", "e", "b")
fill_data("d", 0.9, "y", "y")
fill_data("d", 0.7, "y", "n")
fill_data("d", 0.8, "n", "y")
fill_data("d", 0.1, "n", "n")

conn.commit()

print sum_str

for row in conn.execute('''SELECT b, sum({})
FROM a INNER JOIN t using(a)
INNER JOIN e USING(t) 
INNER JOIN l using(l)
INNER JOIN s using(s)
INNER JOIN b using(s)
INNER JOIN x using(e)
INNER JOIN d using(e, b)
WHERE a='n' and x='y'
GROUP BY b
order by 1
'''.format(sum_str)):
    print row

conn.close()


