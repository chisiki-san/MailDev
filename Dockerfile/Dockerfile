FROM rockylinux:9.2
EXPOSE 1080
EXPOSE 1025
RUN dnf install -y npm
RUN npm i -g maildev
CMD ["maildev"]