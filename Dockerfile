FROM python:3.6

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./src .


CMD python3 __init__.py 50 15 20 2 1 && ls results
#&& echo "result.txt\n\n" && cat results/results.txt && echo "\n\ngraph.txt\n\n" && cat results/graph.txt
#CMD python3 se.py 
#&& echo "result.txt\n\n" && cat results/results.txt && echo "\n\ngraph.txt\n\n" && cat results/graph.txt