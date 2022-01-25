

import py_code.chat_casual as cas
import py_code.chat_class as clf

chat_history_ids = None


def get_response(text, chat_history_ids = None):
    initial = text.split(' ', 1)[0]
    
    if initial in ('menu', 'courses', 'grades', 'sports', 'directions'):
        response = None
        chat_history_ids = None
        page = initial
    else:
       #send to classification
        tag, prob = clf.get_clf(text)
        tag = str(tag[0])
        print(tag)
        #print(prob, tag)
        if prob > 0.90 and tag in ('food', 'directions','grades', 'courses','sports'):
            page = tag
            response = None
            chat_history_ids = None
        
        else:
            page = None
            response, chat_history_ids = cas.casual_chat(text, chat_history_ids)
            #print(response)
    return (page, response, chat_history_ids) 

# p,r,c = get_response('HJow is life..', None)# tensor([[15496,    11,  6855,   282, 22618, 50256, 15496,   837,  5891,  9379, 50256]])))
# print(r)
# p,r,c = get_response('and the kids.', c)
# print(r)
# print(c)