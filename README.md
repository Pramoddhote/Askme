
# Askme Q&A: Question and Answer System Based on Google Palm LLM and Langchain for E-learning  

This is an basic LLM project based on Google Palm and Langchain. We are building a Q&A system just like a chatGPT.


## Project Highlights

- Students should be able to use this system to ask questions directly and get answers within seconds

## You will learn following,
  - Langchain + Google Palm: LLM based Q&A
  - Streamlit: UI

## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/Pramoddhote/Askme.git
```
2.Navigate to the project directory:

```bash
  cd Askme
```
3. Install the required dependencies using pip. Before installation of dependencies make sure you already have install latest python and pip in your local system .

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through makersuite.google.com and paste it in API variable in main.py file

```bash
  GOOGLE_API_KEY="your_api_key_here"
```
## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser.

- Now you are ready to ask questions. Type your question in Question box and hit Enter

- You can Ask any kind of question here . it will provide the answer based on Google PaLm llm 

## Sample Questions
  - calorie's in apple 
  - capital of India  

## Project Structure

- main.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
