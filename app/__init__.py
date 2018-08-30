"""Module that contains the route for the obtaining the shortest path."""

from flask import request, jsonify
from flask_api import FlaskAPI
from collections import deque 

def create_app():
    app = FlaskAPI(__name__, instance_relative_config=True)
    @app.route('/apiv1/shortestpath', methods=['GET'])
    def shortestpath():
        start = request.args.get('start')
        end = request.args.get('end')
        startX = convertToNum(start[0])
        startY = int(start[1])
        endX = convertToNum(end[0])
        endY = int(end[1])
        N = 8
        board_p = [[(-1,-1) for f in range(0,N)] for i in range(0,N)]
        s = (startX,startY)
        t = (endX, endY)
        q = deque()
        q.append(s)
        print(s)
        board_p[s[0]][s[1]] = s # "root" of BFS-traversal points to it self 
        while q:
            u = q.popleft()
            if u == t: break
            for v in Adjacents(u):
                if board_p[v[0]][v[1]] == (-1,-1):
                    board_p[v[0]][v[1]] = u
                    q.append(v)

        # walk the path back (using parent "pointers")
        path = [(t)]    
        while t != s:
            t = board_p[t[0]][t[1]]
            path.append(t)

        path.reverse()
        count = 0
        data = {}
        for place in path:
            data[count] = convertToLetter(place[0]) + '' + str(place[1])
            count = count + 1

        response = jsonify({
            'path': data,
            'status': 'success'
        })
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentialsn'] = True
        response.status_code = 200
        return response
    return app

def Adjacents(u): 
    N = 8   
    adj = []
    for e in [(-2,-1),(-2,1),(2,1),(2,-1),(-1,-2),(1,-2),(-1,2),(1,2)]:        
        v = (u[0] + e[0], u[1] + e[1])
        if v[0] >= 0 and v[0] < N and v[1] >= 0 and v[1] < N: adj.append(v)
    return adj

def convertToNum(letter):
    assignment = {
        'a':0,
        'b':1,
        'c':2,
        'd':3,
        'e':4,
        'f':5,
        'g':6,
        'h':7
    }
    return assignment[letter]

def convertToLetter(num):
    assignment = {
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8
    }
    num = num + 1
    for key, value in assignment.items():
        if num == value:
            return key


   
