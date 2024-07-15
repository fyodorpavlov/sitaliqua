def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
