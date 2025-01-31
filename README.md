# Retrieval-Augmented-Generation
# Reflection on Wikipedia Query Program

## Document Queried
**Name:** Wikipedia Page for Laufey  
**Explanation:**  
I decided to query the Wikipedia page for a musician I love to listen to—Laufey. Her Wiki page contains information about her background and how she has influenced music today.  
This is the website I used: [Laufey Wikipedia Page](https://en.wikipedia.org/wiki/Laufey_(singer))

---

## How the Program Works

### 1. Reads and Splits the File  
- The program reads the file **Selected_Document.txt**, which contains the Wikipedia article text.  
- It splits the text into **chunks**, using **double newlines (`"\n\n"`)** as separators.

### 2. Generates Embeddings  
- It uses the `"all-MiniLM-L6-v2"` model from **SentenceTransformers** to convert each text chunk into an **embedding** (a vector representation of the text).  
- These embeddings **capture the meaning** of the text in a numerical format.

### 3. Finds Similar Text Chunks (Example Query: *"What is cosine similarity?"*)  
- The program **embeds the query** in the same way as the text chunks.  
- It compares the query embedding to all stored text embeddings using **cosine similarity** (a measure of how similar two vectors are).  
- It retrieves the **top 3 most relevant text chunks**.

### 4. Generates a Response  
- The program uses `"google/flan-t5-small"`, a **pre-trained AI model**, to generate a response.  
- It **feeds the retrieved text chunks and the query** into the model.  
- The AI **generates a coherent answer** based on the best-matching text chunks.

---

## Five Important Questions About the Model

### 1. **What is the role of embeddings in this program, and why are they necessary?**  
**Explanation:** Embeddings convert text into **numerical vectors** that capture **semantic meaning**. This allows the program to **compare different text chunks efficiently** using mathematical operations.

### 2. **How does cosine similarity help in finding relevant text chunks for a given query?**  
**Explanation:** Cosine similarity **measures the angle** between two vectors in a multi-dimensional space. The program uses it to **rank text chunks** based on how closely their meaning matches the query.

### 3. **What is the purpose of the SentenceTransformer model (`all-MiniLM-L6-v2`) in this program?**  
**Explanation:** The **SentenceTransformer** model **generates embeddings** for both text chunks and queries. This enables meaningful comparisons between them, allowing the program to **find the most relevant chunks** based on their similarity.

### 4. **How does the Hugging Face T5 model (`google/flan-t5-small`) generate responses using retrieved text chunks?**  
**Explanation:** After retrieving **relevant text chunks**, the T5 model **takes the query and the combined context as input** and generates a **coherent response** using its **pre-trained language generation** capabilities.

### 5. **How well does the system retrieve relevant content and generate responses?**  
- **Retrieval Performance:** The system retrieved the **correct answer 4 out of 5 times** and correctly identified text with relevant information.  
- **Response Quality:** All generated responses were **accurate** based on the retrieved chunks.

---

## **Analysis of System Performance**
### **How well did the system retrieve relevant content?**  
The retrieval was **accurate** in most cases, correctly identifying the **most relevant chunks** for 4/5 questions. The top similar chunks **contained the key information** needed for response generation.

### **Quality of the Generated Responses**  
The **generated responses were correct** for all the test questions. The program was able to extract relevant information and answer **clearly and concisely**.

### **Possible Improvements or Extensions**  
- Allowing users to **continuously type questions** without having to rerun the program every time.  
- Expanding the dataset to **include more details** (e.g., Laufey's **albums, tour dates, and collaborations**).  

---

## **Program Output: Queries, Retrieved Content, and Generated Responses**

### **Query: "Where is Laufey from?"**  
**Generated Response:** *Iceland*  
**Top Similar Chunks:**  
1. **Similarity: 0.6172**  
   > Laufey Lín Bīng Jónsdóttir was born on 23 April 1999 in Reykjavík, Iceland's capital. Her father is Icelandic and her mother is Chinese, hailing from Guangzhou...  
2. **Similarity: 0.5989**  
   > Laufey Lín Bing Jónsdóttir (Icelandic: ...), is an Icelandic singer-songwriter and musician...  
3. **Similarity: 0.5804**  
   > After high school, Laufey attended Berklee College of Music in the United States...  

### **Query: "What was her debut song?"**  
**Generated Response:** *Street by Street*  
**Top Similar Chunks:**  
1. **Similarity: 0.4677**  
   > On 6 April 2020, Laufey released her debut single, "Street by Street", which charted at number one...  
2. **Similarity: 0.4470**  
   > Laufey's United States network television debut was in 2022 when she appeared on Jimmy Kimmel Live!...  
3. **Similarity: 0.4021**  
   > Laufey released her debut EP, *Typical of Me* (2021), and graduated from the Berklee College of Music...  

### **Query: "What genre is her music?"**  
**Generated Response:** *Jazz*  
**Top Similar Chunks:**  
1. **Similarity: 0.6390**  
   > Laufey describes her genre as jazz or jazz pop...  
2. **Similarity: 0.4519**  
   > Laufey rose to prominence in the early 2020s for her success as a jazz-inspired pop artist...  
3. **Similarity: 0.4482**  
   > Laufey was influenced by classical music but turned to jazz musicians such as Ella Fitzgerald...  

### **Query: "Does she have any siblings?"**  
**Generated Response:** *Júnía Lín Jónsdóttir*  
**Top Similar Chunks:**  
1. **Similarity: 0.4540**  
   > Laufey has an identical twin sister named Júnía Lín Jónsdóttir, who is a violinist and serves as her creative director...  
2. **Similarity: 0.4353**  
   > Laufey and her twin sister were accepted to the University of St Andrews...  
3. **Similarity: 0.2875**  
   > At age 15, Laufey performed as a cello soloist with the Iceland Symphony Orchestra...  

### **Query: "What is her latest album?"**  
**Generated Response:** *Bewitched*  
**Top Similar Chunks:**  
1. **Similarity: 0.5558**  
   > Studio albums...  
2. **Similarity: 0.3963**  
   > Her second album, *Bewitched*, was released on 8 September 2023 and won a Grammy Award...  
3. **Similarity: 0.3557**  
   > Laufey rose to prominence as a jazz-inspired pop artist in the early 2020s...  

---

## **Conclusion**
This program successfully retrieved relevant text from Laufey's Wikipedia page and generated **accurate** responses using **AI-powered retrieval and text generation**. While effective, improvements such as **continuous querying** and **expanded dataset coverage** could further enhance the experience.
