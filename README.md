### Setup with virtualenv
- clone the repository
- `cd CMPT-353-Final-Project`
- `download and install [git lfs](https://git-lfs.github.com/)`
- `pip install virtualenv`
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- `jupyter notebook`

### Setup with Docker
- clone the repository
- download and install [git lfs](https://git-lfs.github.com/)
- `cd CMPT-353-Final-Project`
- `docker run -d --rm --name project -v "$PWD":/code -w /code -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes --user root jupyter/datascience-notebook`
- run `docker logs project` to get app url 
- copy and paste above url to your browser. It looks something like `http://127.0.0.1:8888/lab?token=SOME-RANDOM-TOKEN`

### Libraries Used: 

Python Libraries: sys, re

Other: Pandas, Numpy, Matplotlib, Seaborn, Scipy, ipywidgets, pymannkendall, TextBlob, plotly

Please run Jupyter notebook cells sequentially. 
