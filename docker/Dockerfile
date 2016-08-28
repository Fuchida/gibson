FROM python:3.5

ENV POSTS_GIT_REPO "REPO with your posts"
ENV POSTS_GIT_REPO_SECRET "THIS IS A SECRET"

RUN mkdir -p /www && \
	cd www && \
	git clone https://github.com/Fuchida/gibson && \
	cd blog && \
	pip install -r Requirements.in && \
	cd app && \
	git clone $POSTS_GIT_REPO

ADD https://raw.githubusercontent.com/fuchida/gibson/master/docker/start_server.sh /www
CMD ["chmod","+x","/www/start_server.sh"]

EXPOSE 5000

CMD ["sh","/www/start_server.sh"]

