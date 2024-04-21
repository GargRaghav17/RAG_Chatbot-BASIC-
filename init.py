# Importing Dependencies

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Typesense
from dotenv import load_dotenv
import streamlit as st
import warnings

# Creating a chatbot using Gemini Pro, with Typesense as the vector store db, Google API for embeddings, and StreamLit for UI



# Initializing
if "history" not in st.session_state:
    st.session_state.history = []
load_dotenv()

GOOGLE_API_KEY = 'AIzaSyAKqlN3y5HwwjIjLKq9adJ6yor2Q1ciogU'

model = ChatGoogleGenerativeAI(model = 'gemini-pro', google_api_key = GOOGLE_API_KEY, temperature = 0.2, convert_system_message_to_human=True)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=GOOGLE_API_KEY)

warnings.filterwarnings("ignore")



# Load PDF
pdf_loader = PyPDFLoader("E:/python310/Vscode/Microsoft VS Code/ragllmbasic/engbookmerged.pdf")
pages = pdf_loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
texts = text_splitter.split_documents(pages)



# Vector Database
vector_index = Typesense.from_documents(
    texts,
    embeddings,
    typesense_client_params={
        "host": "fmqs2b5rd6elvcwip-1.a1.typesense.net",  
        "port": "443",
        "protocol": "https",
        "typesense_api_key": "cEawC7Usaz1Sea2OEYytJ3DO6d0Mps6W",
        "typesense_collection_name": "lang-chain",
    },
)

retriever = vector_index.as_retriever()



# Prompt Template
template = """Use the following pieces of context to answer the question at the end. If there is a question asked related to the context , but the answer isn't present in the context and you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
{context}
Question: {question}
Helpful Answer:"""



# QA Chain
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)# Run chain
qa_chain = RetrievalQA.from_chain_type(
    model,
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)


# Streamlit UI
st.title('Q/A RAG Pipeline based Chatbot')

for msg in st.session_state.history:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])


prompt = st.chat_input("Say something")
if prompt:
    st.session_state.history.append({
        'role':'user',
        'content':prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner('💡Thinking'):
        response = qa_chain({"query": prompt})

        st.session_state.history.append({
            'role' : 'Assistant',
            'content' : response['result']
        })

        with st.chat_message("Assistant"):
            st.markdown(response['result'])