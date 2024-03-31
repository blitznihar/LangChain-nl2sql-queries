# LangChain Agent to query Database based on the questions

##### Langchain is a framework that enables querying a pre-defined database using natural language. It processes your question and generates the corresponding SQL query to retrieve the data.

##### You can ask questions in plain English to get information from a pre-built database with Langchain.

#### _Step to run the project_

Add Environment file. Create a .env file and add below configurations
```sh
OPENAI_API_KEY=""
```
Fill the OPENAI_API_KEY values

In the Terminal 
```sh
pipenv install
pipenv shell
```

Once the app is running type below command in the Terminal
```sh
python .
```

Ask your question. for e.g.
```sh
how many users name starts with anthony in the database?
```

Or
```sh
how many users firstname anthony in the database?
```

Or
```sh
what are some 5 products in the database?
```

Or
```sh
how many users who have provided their shipping addresses?
```


##### References:

[OpenAI](https://platform.openai.com/docs/introduction)

[OpenAI API Keys](https://platform.openai.com/api-keys)

[LangChain](https://python.langchain.com/docs/get_started/introduction)