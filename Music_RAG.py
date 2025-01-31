import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import T5Tokenizer, T5ForConditionalGeneration

def read_and_split_file(filename):
    """
    Reads the content of a file and splits it into chunks separated by double newline characters ("\n\n").
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Split content into chunks
        chunks = content.split("\n\n")
        
        return chunks
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return [] 

def generate_embeddings(chunks):
    """
    Generates embeddings for a list of text chunks using SentenceTransformers.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks, convert_to_tensor=True)
    
    # Move embeddings to CPU before converting to NumPy array
    embeddings = embeddings.cpu().numpy()
    
    # Store embeddings in a dictionary
    embeddings_dict = {chunks[i]: embeddings[i] for i in range(len(chunks))}
    
    return embeddings_dict

def find_most_similar_chunks(query, embeddings_dict, top_n=3):
    """
    Finds the top N most similar text chunks to the query using cosine similarity.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode([query], convert_to_tensor=True).cpu().numpy()
    
    texts = list(embeddings_dict.keys())
    embeddings = np.array(list(embeddings_dict.values()), dtype=np.float32)
    
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    
    return [(texts[i], similarities[i]) for i in top_indices]

def generate_response(query, top_chunks):
    """
    Generates a response based on the retrieved text chunks and query using the google/flan-t5-small model.
    """
    model_name = "google/flan-t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    # Combine the retrieved chunks into a single prompt
    context = "\n".join([chunk for chunk, _ in top_chunks])
    prompt = f"Query: {query}\nContext: {context}\nAnswer:"
    
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, max_length=200)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return response

if __name__ == "__main__":
    filename = "Selected_Document.txt"
    chunks = read_and_split_file(filename)
    
    print("Generating new embeddings...")
    embeddings_dict = generate_embeddings(chunks)
        
    query = input("Enter your search query: ")
    top_chunks = find_most_similar_chunks(query, embeddings_dict)
    
    print("\nTop similar chunks:")
    for text, similarity in top_chunks:
        print(f"Similarity: {similarity:.4f}\n{text}\n")
    
    response = generate_response(query, top_chunks)
    print("\nGenerated Response:")
    print(response)
