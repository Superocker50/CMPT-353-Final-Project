# EDA on Mobile Apps on Google Play Store and Apple App Store

### SFU CMPT 353 Fall 2021 - Final Project


## Setup with Docker 🐳
- `download [git lfs](https://git-lfs.github.com/)`
- `git lfs install`
- clone the repository
- `cd CMPT-353-Final-Project`
- `docker run -d --rm --name project-353 -v "$PWD":/code -w /code -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes --user root jupyter/datascience-notebook`
- run `docker logs project-353` to get app url 
- copy and paste above url to your browser. It looks something like `http://127.0.0.1:8888/lab?token=SOME-RANDOM-TOKEN`


## Setup with virtualenv
- `download [git lfs](https://git-lfs.github.com/)`
- `git lfs install`
- clone the repository
- `cd CMPT-353-Final-Project`
- `pip install virtualenv`
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- `jupyter notebook`

___

### Libraries Used: 

Python Libraries: sys, re

Other: Pandas, Numpy, Matplotlib, Seaborn, Scipy, ipywidgets, pymannkendall, TextBlob, plotly

Please run Jupyter notebook cells sequentially. 

References 

Google Play Store Data set: https://www.kaggle.com/gauthamp10/apple-appstore-apps
Apple App Store Data set: https://www.kaggle.com/gauthamp10/google-playstore-apps
Google Play Scraper Module: https://github.com/JoMingyu/google-play-scraper
Apple App Store Scraper Library: https://github.com/facundoolano/app-store-scraper
