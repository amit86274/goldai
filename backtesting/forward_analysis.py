
def forward_performance(train_profit,test_profit):
    return {"train":train_profit,"test":test_profit,"ratio":test_profit/train_profit if train_profit else 0}
