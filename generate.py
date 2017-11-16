import sys

import numpy as np
import librosa
import chainer

import models
from utils import mu_law
from utils import Preprocess
import opt

model = models.VAE()
chainer.serializers.load_npz(sys.argv[1], model)

n = 1
x = np.expand_dims(Preprocess(
    opt.data_format, opt.sr, opt.mu, opt.sr * 3, False)(sys.argv[2])[0], 0)
output = model.generate(x)
wave = mu_law(opt.mu).itransform(output)
np.save('result.npy', wave)
librosa.output.write_wav('result.wav', wave, opt.sr)
