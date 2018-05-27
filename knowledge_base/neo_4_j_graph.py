from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client


class KnowledgeGraph:
    def __init__(self):
        self.db = GraphDatabase("http://localhost:7474", username="neo4j", password="Qwertz1#")
        self._add_user()

    def _add_user(self):
        """
        Adds the central user, i.e. the conversation partner
        """
        q = "MATCH (u:User) RETURN u;"
        user1 = self.db.query(q, returns=client.Node)

        if user1:
            self.central_user = self.db.nodes.get(name="CentralUser", key="0")
            return
        else:
            user = self.db.labels.create("User") # Type
            self.central_user = self.db.nodes.create(name="CentralUser", key="0")
            user.add(self.central_user)

    def add_contact(self, contact_name, relationship):
        contact = self.db.labels.create("contact") #type
        c1 = self.db.nodes.create(name=contact_name)
        contact.add(c1)
        self.central_user.relationships.create(relationship, c1)

        if relationship == "sister":
            c1.relationships.create("brother", self.central_user)
        if relationship == "brother":
            c1.relationships.create("sister", self.central_user)
        if relationship == "friend":
            c1.relationships.create("friend", self.central_user)

    def search_contactname_by_relationship(self, relationship):
        if relationship == 'freund':
            q = 'MATCH (u:User)-[r:friend]->(c:contact) RETURN c.name;'
        elif relationship == 'schwester':
            q = 'MATCH (u:User)-[r:sister]->(c:contact) RETURN c.name;'
        elif relationship == 'bruder':
            q = 'MATCH (u:User)-[r:sister]->(c:contact) RETURN c.name;'
        else:
            return None
        result = self.db.query(q, returns=str)
        if len(result) == 0:
            return None

        return result[0][0]

    def search_relationship_by_contactname(self, contact_name):
        name = contact_name.replace(" ", "")
        q = 'MATCH (:User)-[r]->(c:contact) WHERE c.name="'+name+'" RETURN type(r);'
        result = self.db.query(q, returns=str)
        if len(result) == 0:
            return None

        return result[0][0]

    def search_all_contacts(self):
        q = 'MATCH (:User)-[r]->(c:contact) RETURN c;'
        results = self.db.query(q, returns=client.Node)
        contacts = []
        for r in results:
            contacts.append(r[0]["name"])

        """
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
        """


if __name__ == "__main__":
    kg = KnowledgeGraph()
    #kg.add_contact("Lara", "sister")
    #print(kg.search_contact_by_relation("sister"))
    print(kg.search_relationship_by_contactname("blub"))

    #kg.search_all_contacts()

