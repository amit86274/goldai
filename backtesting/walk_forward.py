
def walk_forward(data,train_size,test_size):
    for i in range(0,len(data)-train_size-test_size+1,test_size):
        yield data[i:i+train_size],data[i+train_size:i+train_size+test_size]
