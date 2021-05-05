# Solution exercise 2


docker run --rm -it --name fastqc_albot -w="/data/" -v ~/containers/data/:/data quay.io/biocontainers/fastqc:0.11.9--0 /bin/bash 
docker run --rm --name fastqc_albot -u="$(id -u):$(id -g)" -w="/data/" -v ~/containers/data/:/data quay.io/biocontainers/fastqc:0.11.9--0 /bin/bash -c "fastqc WT*.fq.gz"
