# Crawler

- This is a python script used to crawl through a target directory, find all TIFF files, 
convert them to JPEG and copy them to a new target directory.


### Getting started

The project structure should look like this
```
crawler_root 
      |--- venv
      |--- crawler 
                |--- .git
```

1. Create the project root: `mkdir crawler_root`
2. Create the virtual environment: 
```
cd crawler_root
python -m venv venv
``` 
3. Clone the repo: `git clone https://github.com/dfo-gulf-science/crawler.git`
4. Activate the virtual environment: `..\venv\Scripts\activate`
5. Install requirements: `pip install -r requirements.txt`
