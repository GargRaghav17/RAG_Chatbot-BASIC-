# Q/A RAG Pipeline based Chatbot

This repository contains code for a Question-Answering (Q/A) chatbot implemented using Gemini Pro, Google's Generative AI, Typesense as the vector store database, and Streamlit for the user interface.

## Dependencies

Make sure you have the following dependencies installed:

- `langchain_google_genai`
- `langchain`
- `dotenv`
- `streamlit`

You can install these dependencies using pip:

```bash
pip install langchain_google_genai langchain python-dotenv streamlit
```

## Usage

### Setup

1. Clone the repository:

   ```bash
   git clone <https://github.com/GargRaghav17/RAG_Chatbot-BASIC-/>
   ```

2. Install the required dependencies as mentioned above.

3. Obtain a Google API key and replace `'AIzaSyAKqlN3y5HwwjIjLKq9adJ6yor2Q1ciogU'` with your actual API key in the code.

4. Adjust the file path for the PDF in the code according to your file system.

### Running the Chatbot

Run the following command:

```bash
streamlit run init.py
```

This will launch a Streamlit app where you can interact with the Q/A chatbot.

## Description

The chatbot operates in the following manner:

1. It loads a PDF document specified in the code.
2. Text from the PDF is split into chunks for processing.
3. The text chunks are indexed in Typesense as vectors using Google's Generative AI embeddings.
4. Users interact with the chatbot through a Streamlit UI.
5. The chatbot responds to user queries by retrieving relevant information from the indexed text chunks.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
