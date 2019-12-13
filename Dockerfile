#
#
#
FROM python:3.7-alpine
#RUN apk --no-cache add python-pip && \
#    pip install jsonify flask
RUN pip install jsonify flask line-bot-sdk
COPY line_svc.py /

EXPOSE 8080

ENTRYPOINT ["python", "/line_svc.py"]
