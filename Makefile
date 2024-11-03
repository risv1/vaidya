rs:
	cd services/hadoop && docker compose up -d
	cd .. && cd spark && docker compose up -d
	cd .. && cd ..
	python3 src/main.py

rc:
	cd client && bun dev