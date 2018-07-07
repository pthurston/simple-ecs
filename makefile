report:
	coverage report -m

test:
	coverage run --source ecs -m unittest -v
	make report

run:
	python py-ecs.py

shell:
	python -i shell.py