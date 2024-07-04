from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.chains import LLMChain
from langchain.chains import SequentialChain, SimpleSequentialChain
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()




import langchain
langchain.debug=True

_ = load_dotenv(find_dotenv())

llm = ChatOpenAI(temperature=0.0)

chatPromptTemplate= ChatPromptTemplate