import string

import numpy as np
import tensorflow as tf

allowed_text = ["loha", "alha", "aloa", "aloh", "aoha", "aloha"]
id_to_char = np.array([x for x in string.ascii_lowercase + "\" -|"])


def ce_loss(x, y, weight=1):
    '''Cross entropy loss function for training keyword spotter'''
    loss = tf.nn.softmax_cross_entropy_with_logits_v2(logits=x, labels=y)
    return weight * tf.reduce_sum(loss)


def weight_init(shape):
    '''Convenience function for randomly initializing weights'''
    weights = np.random.uniform(-0.05, 0.05, size=shape)
    return weights


def merge(chars):
    '''Merge repeated characters and strip blank CTC symbol'''
    acc = ["-"]
    for c in chars:
        if c != acc[-1]:
            acc.append(c)

    acc = [c for c in acc if c != "-"]
    return "".join(acc)


def predict_text(sim, probe, n_steps, p_time=10):
    '''Predict a text transcription from the current simulation state'''
    n_frames = int(n_steps / p_time)
    char_data = sim.data[probe]
    n_chars = char_data.shape[1]

    # reshape to seperate out each window frame that was presented
    char_out = np.reshape(char_data, (n_frames, p_time, n_chars))

    # take most ofter predicted char over each frame presentation interval
    char_ids = np.argmax(char_out, axis=2)
    char_ids = [np.argmax(np.bincount(i)) for i in char_ids]

    text = merge(''.join([id_to_char[i] for i in char_ids]))
    text = merge(text)  # merge repeats to help autocorrect

    return text


def create_stream(stream, dt=0.001):
    '''Create a streaming function for sending data into Nengo network'''
    def play_stream(t, stream=stream):

        ti = int(t / dt)
        return stream[ti % len(stream)]

    return play_stream

