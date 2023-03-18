from OOP.static_andclass_methods.documentmanagment.project.category import Category
from OOP.static_andclass_methods.documentmanagment.project.document import Document
from OOP.static_andclass_methods.documentmanagment.project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        category = [category for category in self.categories if category_id == category.id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [topic for topic in self.topics if topic_id == topic.id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        doc = [doc for doc in self.documents if doc.id == document_id][0]
        doc.edit(new_file_name)

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        self.topics.remove([topic for topic in self.topics if topic_id == topic.id][0])

    def delete_document(self, document_id: int):
        self.documents.remove([document for document in self.documents if document_id == document.id][0])

    def get_document(self, document_id: int):
        doc = [doc for doc in self.documents if doc.id == document_id][0]
        return doc

    def __repr__(self):
        return '\n'.join([str(doc) for doc in self.documents])


from OOP.static_andclass_methods.documentmanagment.project.category import Category
from OOP.static_andclass_methods.documentmanagment.project.document import Document

from OOP.static_andclass_methods.documentmanagment.project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
