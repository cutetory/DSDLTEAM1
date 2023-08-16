FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:1.15.5-gpu-py3-jupyter

WORKDIR /tf-test

COPY requirements.txt requirements.txt

# Update and upgrade the package repository
RUN apt-get update && apt-get upgrade -y

# Install Python 3.9 and update alternatives
RUN apt-get install -y python3.9 python3.9-distutils
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Update pip for Python 3.9
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.9 get-pip.py

# Clean up
RUN rm get-pip.py
RUN apt-get clean

# Set Python 3.9 as the default Python version
RUN update-alternatives --set python3 /usr/bin/python3.9

RUN pip install -r requirements.txt

# Set environment variables for CUDA
ENV PATH="/usr/local/cuda-11.8/bin:$PATH"
ENV LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"
# ENV PATH="/usr/local/cuda-12.2/bin:$PATH"
# ENV LD_LIBRARY_PATH="/usr/local/cuda-12.2/lib64:$LD_LIBRARY_PATH"


EXPOSE 8888

ENTRYPOINT [ "jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]