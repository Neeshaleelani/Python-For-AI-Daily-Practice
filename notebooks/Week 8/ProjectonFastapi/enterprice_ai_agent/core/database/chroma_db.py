import chroma_db

COLLECTION_NAME ="resturnet"

chroma_client = chromadb.PersistentClient(path="./")

collection = chroma_client.get_or_create_collection(name="restaurant_vector_db")