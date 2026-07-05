from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate




load_dotenv()

def ask_product(question, webpage):
    document = Document(page_content=webpage)

    

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )  
    chunks = splitter.split_documents([document])

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs= {"k": 4})

    llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

    retrieved_docs = retriever.invoke(question)
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    prompt = PromptTemplate(
    template="""
You are ProDoubt, an AI assistant that answers questions about products.

Use ONLY the information provided in the context.

If the answer cannot be found in the context, say:
"I couldn't find that information on this product page."

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)

    final_prompt = prompt.invoke({"question": question, "context": context_text})

    answer = llm.invoke(final_prompt)

    return answer.content







   



   
    
  








    
    

  

    


    
