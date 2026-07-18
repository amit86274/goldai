
def get_training_params(use_gpu=True):
    return {"task_type":"GPU"} if use_gpu else {"task_type":"CPU"}
