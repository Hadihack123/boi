12345FROM python:latest 
COPY bot.py . 
RUN pip3 install  rubika --upgrade
ENTRYPOINT [ "python3" ] 
CMD ["bot.py"] 