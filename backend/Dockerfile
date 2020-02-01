# base stage
FROM python:3.7 AS base
ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT

# builder stage -- installs pipenv and python packages
FROM base AS builder
RUN pip install pipenv
COPY Pipfile* ./
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy --ignore-pipfile

# production stage -- add app files to a secure user
FROM base
ENV PATH $PYROOT/bin:$PATH
COPY --from=builder $PYROOT/lib/ $PYROOT/lib/
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser

WORKDIR /app/
COPY manage.py ./
COPY entrypoint.sh ./
COPY find_closing_bracket/ ./find_closing_bracket
COPY api/ ./api
COPY libs/ ./libs

RUN chown -R appuser:appuser /app/

USER appuser
EXPOSE 8000
CMD ["sh", "entrypoint.sh"]