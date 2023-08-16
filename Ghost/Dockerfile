FROM tensorflow/tensorflow:nightly-gpu-jupyter

WORKDIR /Ghost

COPY requirements.txt requirements.txt

# install build dependencies 
RUN apt-get update && apt-get install -y g++ rsync zip openssh-server make 

# configure SSH for communication with Visual Studio 
RUN mkdir -p /var/run/sshd

RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \ 
   ssh-keygen -A

# 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

# LD_LIBRARY_PATH 환경 변수 설정
ENV LD_LIBRARY_PATH /path/to/libraries:$LD_LIBRARY_PATH

RUN pip install -r requirements.txt

# Set environment variables for CUDA
# ENV PATH="/usr/local/cuda-11.8/bin:$PATH"
# ENV LD_LIBRARY_PATH="/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH"

EXPOSE 8888

ENTRYPOINT [ "jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]