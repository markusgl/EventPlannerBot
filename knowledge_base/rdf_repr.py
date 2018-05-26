from rdflib import Graph, BNode, RDF, Literal, URIRef
from rdflib.namespace import FOAF

graph = Graph()
user = BNode()

graph.add((user, RDF.type, FOAF.Person))
graph.add((user, FOAF.nick, Literal("user", lang="de")))
graph.add((user, FOAF.name, Literal("Max Mustermann")))
graph.add((user, FOAF.mbox, URIRef("mailto:max@example.org")))

# For each foaf:Person in the store print out its mbox property.
print("--- printing mboxes ---")
for person in graph.subjects(RDF.type, FOAF.Person):
    for name in graph.objects(person, FOAF.name):
        print(name)

graph.serialize("test_foaf.rdf", format="pretty-xml")
print(graph.serialize(format='n3'))