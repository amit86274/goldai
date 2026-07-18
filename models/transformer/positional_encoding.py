
import tensorflow as tf

def positional_encoding(length, depth):
    positions=tf.range(length,dtype=tf.float32)[:,None]
    dims=tf.range(depth,dtype=tf.float32)[None,:]
    angle=positions/tf.pow(10000.0,(2*(dims//2))/depth)
    pe=tf.where(tf.cast(dims%2,tf.bool), tf.cos(angle), tf.sin(angle))
    return pe
