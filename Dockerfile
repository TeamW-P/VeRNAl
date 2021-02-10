FROM continuumio/anaconda3

WORKDIR /vernal

COPY . .

RUN chmod +x boot.sh
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "vernal", "/bin/bash", "-c"]

EXPOSE 5003

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "vernal", "./boot.sh"]
