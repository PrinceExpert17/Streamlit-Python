import streamlit as st
from textblob import TextBlob
import spacy

#from gensim.summarization.summarizer import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#This project is an NLP Sentiment Analysis:
#- Streamlit, Spacy
#- NER | Sentiment | Summarization

def text_analyze(texts):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(texts)
    all_data = [f'Tokens: {token.text},\nLemma: {token.lemma_}' for token in docx]
    return all_data

def entity_analyze(texts):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(texts)
    tokens = [token.text for token in docx]
    ent = [(entity.text, entity.label_) for entity in docx.ents]
    all_data = all_data = [f'Tokens: {tokens},\nEntities: {ent}']
    return all_data

def sumy_sum(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer('english'))
    lex_sum = LexRankSummarizer()
    sums = lex_sum(parser.document, 3)
    sum_list = [str(sentence) for sentence in sums]
    result = ''.join(sum_list)
    return result

def main():
    st.title('NLP Classifier with Streamlit')
    st.subheader('NLP made easier')
    
    # Tokenizing
    if st.checkbox('Tokenization & Lemma'):
        st.subheader('Tokenizing')
        message = st.text_area('Enter a sentence below', 'Type Here')
        if st.button('Analyze'):
            nlp_result = text_analyze(message)
            st.json(nlp_result)
    
    # Named Entity
    if st.checkbox('Name Entity Recognition'):
        st.subheader('Extract Entity From Your Text')
        message = st.text_area('Enter Your Text', 'Type Here')
        if st.button('Extract'):
            nlp_result = entity_analyze(message)
            st.json(nlp_result)
    
    # Sentiment Analysis
    if st.checkbox('Sentiment Analysis'):
        st.subheader('Extract Sentiment From Your Text')
        message = st.text_area('Enter Sentiment below', 'Type Here')
        if st.button('Extract'):
            blob = TextBlob(message)
            result_sent = blob.sentiment
            st.success(result_sent)
            
    # Text Summarization
    if st.checkbox('Text Summarize'):
        st.subheader('Get a Summarization of your Text')
        message = st.text_area('Enter Text', 'Type Here')
        if st.button('Summary'):
            st.text('Sumy...')
            sum_result = sumy_sum(message)
            st.success(sum_result)
            
    st.sidebar.subheader('About App')
    st.sidebar.text('This is an NLP App Classifier with Streamlit')
    st.sidebar.info('About App')
    

if __name__ == '__main__':
    main()
