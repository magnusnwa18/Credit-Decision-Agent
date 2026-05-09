from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import pandas as pd

# Placeholder for credit decision agent
print('Credit Decision Agent initialized')

# Example usage
def process_document(text):
    llm = ChatOpenAI(model='gpt-4o')
    prompt = PromptTemplate.from_template('Extract credit risk info from: {text}')
    chain = prompt | llm
    return chain.invoke({'text': text})

if __name__ == '__main__':
    sample = 'Sample bank statement data...'
    result = process_document(sample)
    print(result)