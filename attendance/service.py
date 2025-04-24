from attendance import firebase
firebase = firebase.FirebaseApplication('https://qrattendance-4e21a-default-rtdb.firebaseio.com/', None)

class FireBaseObject:
    pass

def postObject(data,type):
    result = firebase.post('/'+type+'/',data)
    print(result)
    return result