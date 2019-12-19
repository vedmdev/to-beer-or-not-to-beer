create_env:
	virtualenv venv
	echo "now call: source ./venv/bin/activate"

activate_env:
	source ./venv/bin/activate

install_training_requirements:
	pip3 install -r ./training-requirements.txt

train:
	echo "training"
	python3 ./src/training/train.py

test:
	echo "testing"

run_prediction_on_file:
	python3 ./src/prediction/run_prediction_on_file.py

serve:
	python3 ./src/serving/server.py

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

ready_k8s:
	kubectl create namespace beer

deploy_k8s:
	kubectl -n beer apply -f k8s.yml


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
	python3 ./scripts/scrapers/google/image_downloader.py
