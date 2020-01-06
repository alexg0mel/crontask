run:
	./.venv/bin/python ./app/app.py

asyncrun:
	cd app && ../.venv/bin/uvicorn asyncapp:app --reload

install:
	pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \
    wxPython
	pip install -r app/requirements.txt


up:
	docker-compose up --build -d
		./.venv/bin/python ./app/app.py

down:
	docker-compose down

test:
	./.venv/bin/pytest

test-cov:
	./.venv/bin/pytest --cov ./app/