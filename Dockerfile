FROM centos:latest
RUN yum group install "Development Tools" -y
RUN yum install llvm-toolset -y


# docker built -t mygcc:v1