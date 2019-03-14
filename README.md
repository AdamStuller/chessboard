Chessboard, Euler's horse problem
=========================================

This repository contains that solves euler's horse problem by implementing search algorithm. 
Specifically `depth first search`. It uses `Warnsdorff’s heuristic` for making the search more
efficient. Check the documentation for closer look at the algorithm implemented.

#Usage

Requirements.txt file is empty since no external libraries were used. Python interpreter 
used was **python3.7**. Before running programme check config.py and change it to modify 
behavior of programme. 

To run it go to desired file and run:
```
git clone git@github.com:AdamStuller/chessboard.git
cd ./chessboard
```

Now you have repository cloned. You can create virtual enviroment by running:
```
python3.7 -m venv ./venv
./venv/bin/pip3.7 install -r ./requirements.txt
```

And then, after modifying config run:
```
./venv/bin/python3.7 ./chessboard.py
```