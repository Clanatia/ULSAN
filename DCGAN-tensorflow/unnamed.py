import os
import scipy.misc
import numpy as np
import math
from time import gmtime, strftime
from model import DCGAN
from utils import pp, visualize, to_json, show_all_variables

from ops import *


import tensorflow as tf

batch_size = 1
run_config = tf.ConfigProto()
run_config.gpu_options.allow_growth=True
with tf.Session(config=run_config) as sess:
    dcgan = DCGAN(
        sess,
        input_width=64,
        input_height=64,
        output_width=64,
        output_height=64,
        batch_size=batch_size,
        sample_num=1,
        c_dim=3,
        dataset_name="celebA",
        input_fname_pattern="*.jpg",
        is_crop=False,
        checkpoint_dir="checkpoint",
        sample_dir="samples")
        
    #show_all_variables()
    if not dcgan.load("checkpoint"):
        raise Exception("[!] Train a model first, then run test mode")
        
    image_frame_dim = int(math.ceil(batch_size**.5))
    z_sample = np.random.uniform(-0.5, 0.5, size=(batch_size, dcgan.z_dim))
    print(z_sample.shape)
    #print(z_sample)
    samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})
    print(samples.shape)
    save_images(samples, [image_frame_dim, image_frame_dim], 'test_%s.png' % strftime("%Y%m%d%H%M%S", gmtime()))
