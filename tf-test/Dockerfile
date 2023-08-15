FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:1.15.5-gpu-py3-jupyter

WORKDIR /tf-test

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Set environment variables for CUDA
# ENV PATH /usr/local/cuda-11.8/bin:$PATH

# Set environment variables for CUDA
# ENV PATH="/usr/local/cuda-11.8/bin:$PATH"
# ENV LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"
ENV PATH="/usr/local/cuda-12.2/bin:$PATH"
ENV LD_LIBRARY_PATH="/usr/local/cuda-12.2/lib64:$LD_LIBRARY_PATH"


EXPOSE 8888

ENTRYPOINT [ "jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]