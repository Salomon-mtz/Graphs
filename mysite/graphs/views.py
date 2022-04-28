from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from json import dumps


def index(request):
    mydb = sqlite3.connect("db.sqlite3")
    curr = mydb.cursor()
    
    #Map Query
    h_var = 'Country'
    v_var = 'Players'
    query_countries ='''SELECT country, COUNT(country)
		FROM graphs_player
		GROUP BY country
	'''
    rows3 = curr.execute(query_countries)
    data = [[h_var, v_var]]
    
    for x in rows3:
        data.append([x[0], x[1]])

    modified_data = dumps(data)
    
    return render(request, 'index.html', {'values3': modified_data, })
