# simple smart file organiser
A background tool that watches my Downloads folders and sorts text files and PDFs into folders based on their content.

### Pipeline
1. Monitor a folder and detect when a file arrives
2. Open PDFs/Docs and extract raw string text in Python
3. Train a model to classify the text into categories
