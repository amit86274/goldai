
def get_device_config(use_gpu=True):
    return {"device":"gpu"} if use_gpu else {"device":"cpu"}
