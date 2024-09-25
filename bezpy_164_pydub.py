
# Manipulate audio with a simple and easy high level interface
# https://pypi.org/project/pydub/
# Requires `pip install pydub`
from pydub import AudioSegment

# Pull in your audio file
sound = AudioSegment.from_file("example.mp3")

# Slice and dice—grab the first 10 seconds
first_ten_seconds = sound[:10000]

# Export your creation
first_ten_seconds.export("output.mp3", format="mp3")