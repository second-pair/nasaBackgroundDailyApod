make:
	pyinstaller.exe --onefile --specpath build --distpath bin backgroundDailyApod.py
	cp apiKey bin/apiKey
	
clean:
	rm -rf bin build __pycache__
