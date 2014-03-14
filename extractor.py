''' Answer Extractor Module'''

import api
import pygraphviz as pgv


#transforms sentence into dependency graph
def getGraph(s):
    G = {}
    orig = api.toString(s)
    dep = api.corenlp.raw_parse(orig)['sentences'][0]['indexeddependencies']
    for d in dep:
        #rel(x,y) gives the relation of y to x
        #interpret it as y is a rel(x,y) of x
        rel = d[0] #relationship between words
        x = d[1] # the word that y is in relation to
        y = d[2] # the word that we want to find the relation of

        if not y in G:
           G[y] = []
        if x in G:
            if (y, rel) in G[x]:
                continue
            else:
                G[x].append((y,rel))
        else:
            G[x] = [(y,rel)]
    return G
#s is the string you want to turn into a graph
def visualizeGraph(s):
    p = api.parseS(s)
    G = getGraph(p[0])
    vis = pgv.AGraph(directed=True)
    vis.graph_attr['label'] = api.toString(p[0])
    for v in G:
        vis.add_node(v)
    for v in G:
        for tpl in G[v]:
            vis.add_edge(v, tpl[0], label=tpl[1])
    vis.draw('graph.png', prog='circo')


#returns the index of the string node
def idx(node):
    itms = node.split('-')
    return itms[1]-1

#returns the word of a string node
def word(node):
    itms = node.split('-')
    return itms[0]

#The function finds the node which has a t typed edge
#G is the graph
#curr is the current node
#t is a string representing the relation your looking for
#visited is a dict of visited nodes
def gSearch(G, curr, t, visited):
    visited[curr] = True
    for nb in G[curr]:
        word = nb[0]
        tp = nb[1]
        if word in visited:
            continue
        if tp == t:
            return (visited, curr)
        else:
            (visited, result) = gSearch(G, word, t, visited)
            if result:
                return (visited,result)
    return (visited, None)
            

#extracts subj/verb/obj of a question
#s is the question, t is question type
def get(t,s):
    G = getGraph(s)
    pnode = gSearch(G, 'ROOT-0', 'aux', {},
    if t == 0:
        
    else:
'''    
def getNP():
def getT():
def getPer():
def getPlc():
def getYN():
'''
