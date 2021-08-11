#QA BugsManager AutoTests Yana Shurpik Project


#####To install requirements for Windows
```pip install -r requirements.txt```

#####Examples of running marked tests:
    pytest -m api -s
    pytest -m ui -s
    
#####Examples of running parametrized tests:
    pytest --browser_name=chrome --language=en -s -m ui