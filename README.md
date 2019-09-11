#  Nasa Background Daily APOD
This is a simple programme to download NASA's Astrological Picture Of the Day and set it as the user's desktop background.
Setting the background currently only works on Windows (and running on another OS would probably cause it to error out after downloading the image), though I intend to widen operability in due course.

##  Usage (CLI)
backgroundDailyApod.exe [date]

##  API Key
The programme will run quite happily with the demo API key, but if you already have your own, feel free to slot it into the `apiKey` file in the same directory as the programme.
You'll need your own API key to be able to specify a date, since the demo key only supports getting information on today's image.

##  Compiling
The python script can be run in-place no problem, but I have included a `makefile` for simple compiling for distribution to computers not running Python (you're welcome, Grandma :).
Simply run `make` to compile and `make clean` to clean up.
The resulting files in `bin` are all you need to run the programme on a clean install!

##  Dependencies
For running:
- requests

For compiling:
- pyinstaller

##  Running
You need to have the `apiKey` file in the same directory as `backgroundDailyApod.exe`.
You can simply double-click the `backgroundDailyApod.exe` executable to run it.
Likewise, you can set up an entry in "Task Scheduler" to run it as a normal executable.
If running on the command-line, you can also specify a custom date in the "yyyy-mm-dd" format and the programme will try to fetch the APOD on that date, but this requires that `apiKEy` contains a valid API key issued by NASA [(apply here!)](https://api.nasa.gov/index.html#apply-for-an-api-key).
