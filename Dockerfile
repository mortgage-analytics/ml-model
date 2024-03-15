FROM continuumio/miniconda3
WORKDIR /usr/src
COPY . .
RUN conda env create --file environment.yaml && conda clean -afy
WORKDIR /usr/src/models
EXPOSE 8000
ENTRYPOINT [ "conda", "run", "-n", "model" ]
CMD ["uvicorn", "main:app", "--reload"]



