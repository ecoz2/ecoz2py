all: test

_ecoz2_extension.so: ecoz2_extension_build.py ecoz2_extension.h
	C_INCLUDE_PATH=../ecoz2/src/include python ecoz2_extension_build.py
	mv _ecoz2_extension.cpython-*.so _ecoz2_extension.so

# the generated .so looks like:
#  on mac: _ecoz2_extension.cpython-38-darwin.so
#  on lin: _ecoz2_extension.cpython-36m-x86_64-linux-gnu.so

test: _ecoz2_extension.so
	python ecoz2_extension_test.py

clean:
	rm -f *.so *.o _ecoz2_extension.c

copyStuff:
	mkdir -p data/predictors/TRAIN/B
	cp ../../ecoz2-whale/exerc01/data/predictors/TRAIN/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.prd data/predictors/TRAIN/B/
	mkdir -p data/sequences/TRAIN/M1024/B
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10079.092_10080.35.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__10540.822_10543.197.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1068.8552_1069.205.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__1089.723_1090.6355.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__12907.783_12909.293.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__15415.037_15417.307.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__2926.575_2929.6223.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__5067.5444_5070.2764.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__588.77454_591.3191.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__680.14154_680.8046.seq data/sequences/TRAIN/M1024/B/
	cp ../../ecoz2-whale/exerc01/data/sequences/TRAIN/M1024/B/from_MARS_20161221_000046_SongSession_16kHz_HPF5Hz.wav__7145.495_7147.0107.seq data/sequences/TRAIN/M1024/B/
