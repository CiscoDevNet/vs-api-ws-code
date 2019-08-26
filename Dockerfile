FROM ciscodevnet/vs-cicd-ws-code:latest

RUN mkdir /home/coder/project/api_samples

COPY meraki_devices_gathering.py /home/coder/project/api_samples/meraki_devices_gathering.py
