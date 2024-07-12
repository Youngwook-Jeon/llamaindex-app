from llama_index.core import Document
from llama_index.core.schema import TextNode
doc = Document(text="This is a sample document text")
n1 = TextNode(text=doc.text[0:16], id_=doc.doc_id)
n2 = TextNode(text=doc.text[17:30], id_=doc.doc_id)
print(n1)
print(n2)