import json, requests
# Create your tests here.

def test_new_tracka():
    data = {
    'project_id':1,
    'zone_id':  1,
    'content_text' : 'TEST',
    'content_img' : '',
    'content_audio' : '',
    'content_video' : '',
    }
    url = 'http://127.0.0.1/endpoints/v1/tracka/new/'
    header = {'Content-Type' : 'application/json'}
    rsp =  requests.post(url, data=json.dumps(data),headers=header)
    


#Test new tracka
test_new_tracka()
