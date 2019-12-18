create_env:
	virtualenv venv
	echo "now call: source ./venv/bin/activate"

activate_env:
	source ./venv/bin/activate

install:
	pip3 install -r ./requirements.txt

train:
	echo "training"
	python3 ./src/training/train.py

test:
	echo "testing"

run_prediction_on_file:
	python3 ./src/prediction/run_prediction_on_file.py

package:
	echo "to create a docker build/ python package/code artefacts"
	docker-compose -f ./docker-compose.yml build

publish:
	echo "to publish a created docker image / code artefacts to a cental repository"
	docker-compose -f ./docker-compose.yml push

run_package:
	docker-compose -f docker-compose.yml up

deploy:
	echo "deploying"



#######
train_exp_1:
	python3 ./src/training/train_exp_1.py

train_exp_2:
	python3 ./src/training/train_exp_2.py

run_prediction_on_file_exp_2:
	python3 ./src/prediction/run_prediction_on_file_exp_2.py

train_exp_3:
	python3 ./src/training/train_exp_3.py

run_prediction_on_file_exp_3:
	python3 ./src/prediction/run_prediction_on_file_exp_3.py

download_images_from_google:
	python3 ./scripts/scrapers/google/image_download.py
