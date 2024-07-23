# audio can be stored as uncompressed wave files
# https://docs.python.org/3/library/wave.html

# There are 3 main parameters 
# Sampling frequency e.g. 48 kHz
# Bitrate (Bits per sample) e.g. 32 bits
# Number of channels e.g. 2 Channels of Audio

# 'wave' is a built-in module in python

# ======================================================================================================================
# Wave_write Objects
# ======================================================================================================================
# close()	        Close the file if it was opened by wave.
# setnchannels()	Set the number of channels. 1 for Mono 2 for stereo channels
# setsampwidth()	Set the sample width to n bytes.
# setframerate()	Set the frame rate to n.
# setnframes()	    Set the number of frames to n.
# setcomptype()	    Set the compression type and description. At the moment, only compression type NONE is supported, meaning no compression.
# setparams()	    accepts parameter tuple (nchannels, sampwidth, framerate, nframes, comptype, compname)
# tell()	        Retrieves current position in the file
# writeframesraw()	Write audio frames, without correcting.
# writeframes()	    Write audio frames and make sure they are correct.


# ======================================================================================================================
# Wave_read Objects
# ======================================================================================================================
# close()	        Close the stream if it was opened by wave module.
# getnchannels()	Returns number of audio channels (1 for mono, 2 for stereo).
# getsampwidth()	Returns sample width in bytes.
# getframerate()	Returns sampling frequency.
# getnframes()	    Returns number of audio frames.
# getcomptype()	    Returns compression type ('NONE' is the only supported type).
# getparams()	    Returns a namedtuple() (nchannels, sampwidth, framerate, nframes, comptype, compname), equivalent to output of the get*() methods.
# readframes(n)	    Reads and returns at most n frames of audio, as a bytes object.
# rewind()	        Rewind the file pointer to the beginning of the audio stream.


import wave, struct, random

# CREATE WAVE FILE
sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz
obj = wave.open('./myfiles/sound.wav','wb')
obj.setnchannels(1)    # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(99999):
   value = random.randint(-32767, 32767)
   data = struct.pack('<h', value)
   obj.writeframesraw( data )
obj.close()


# READ WAVE FILE
obj = wave.open('./myfiles/sound.wav','rb')
print( "Number of channels",obj.getnchannels())
print ( "Sample width",obj.getsampwidth())
print ( "Frame rate.",obj.getframerate())
print ("Number of frames",obj.getnframes())
print ( "parameters:",obj.getparams())
obj.close()

# Number of channels 1
# Sample width 2
# Frame rate. 44100
# Number of frames 99999
# parameters: _wave_params(nchannels=1, sampwidth=2, framerate=44100, nframes=99999, comptype='NONE', compname='not compressed')