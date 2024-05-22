# Tiff Crawler

This is a python script used to crawl through a source directory, find all TIF files, 
convert them to JPEG and copy them to some target directory.


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
4. Activate the virtual environment: **Windows**: `..\venv\Scripts\activate` **Linux**: `source ..\venv\bin\activate`
5. Install requirements: `pip install -r requirements.txt`

### Run the script!

**Windows**
`python crawl.py --source_dir="M:\foo_dir\tif_src" --target_dir="N:\bar_dir\jpg_dst"`

**Linux**
src="/foo_dir/src"
dst="/bar_dir/dst"
`python crawl.py --source_dir=$src --target_dir=$dst`
