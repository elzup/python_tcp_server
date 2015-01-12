# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from models import log_model
    lm = log_model.LogModel()
#    lm.InsertLog('fuga!')
#    res = lm.get_active_user_wrap()
    res = lm.get_active_user_wrap()
    print (res)
