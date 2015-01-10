if __name__ == '__main__':
    from models import log_model
    lm = log_model.LogModel()
    stmt = lm.SelectLog()
    for r in stmt:
        print(r[2], r[1])
