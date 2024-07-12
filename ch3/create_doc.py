from llama_index.core import Document
text = "The quick brown fox jumps over the lazy dog."
doc = Document(
    text=text,
    extra_info={"author": "John Doe", "caregory": "others"},
    doc_id="1"
)
print(doc)