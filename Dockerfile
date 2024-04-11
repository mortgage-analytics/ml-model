FROM continuumio/miniconda3:latest
WORKDIR /usr/src

COPY container-env.yaml container-env.yaml
ENV PYTHONDONTWRITEBYTECODE=true
RUN conda env create --file container-env.yaml \
	&& conda clean -afy \
	&& find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

COPY models ./models
COPY Scripts ./Scripts
WORKDIR /usr/src/models

EXPOSE 8000
ENTRYPOINT [ "conda", "run", "-n", "model" ]
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]



