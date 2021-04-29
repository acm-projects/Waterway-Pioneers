import json
import math
from collections import defaultdict

from flask_restful import Api, Resource
import firebase_admin
from flask import Flask, request, jsonify, redirect, render_template, make_response
from firebase_admin import credentials, firestore, initialize_app
from firebase import firebase

app = Flask(__name__)
api = Api(app)
firebase = firebase.FirebaseApplication("https://login-auth-42458-default-rtdb.firebaseio.com/", None)

# Ignore the config dict its useless
config = {
    "apiKey": "AIzaSyCOyYtjVoddu_v0wuE90AlUO5ZYvIwe1iI",
    "authDomain": "login-auth-42458.firebaseapp.com",
    "projectId": "login-auth-42458",
    "storageBucket": "login-auth-42458.appspot.com",
    "messagingSenderId": "642686191238",
    "appId": "1:642686191238:web:74ba8c7a94671f0d447307",
    "measurementId": "G-9L1VJ04JS7"}
# ------------------------------

#Initialize trails DB

cred1 = credentials.Certificate('firebase-sdk.json')
app2 = firebase_admin.initialize_app(cred1)
db1 = firestore.client(app=app2)


# Initialize Login Auth firestore DB
cred = credentials.Certificate(
    'login-auth-42458-firebase-adminsdk-fl3g5-db0164d6e9.json')
app1 = firebase_admin.initialize_app(cred, name="login")
db = firestore.client(app=app1)

# Statement below adds a data to the realtime database

'''
data = {
    'username': 'yashp',
    'password': 'ypathi234'
}
result1 = firebase.post('/login-auth-42458-default-rtdb/Credentials', data)
'''


# Uses firestore
# Creating new accounts - REQUIRED INFO (USERNAME AND PASS)
@app.route('/signup/<string:fname>/<string:lname>/<string:username>/<string:password>/<string:email>',
           methods=['POST', 'GET'])
def signup(fname: str, lname: str, username: str, password: str, email: str):
    if request.method == 'POST':
        data = {
            'firstname': fname,
            'lastname': lname,
            'username': username,
            'password': password,
            'email': email,
            'userrating': 0,
            'comments': 'none',
            'trailsvisited': -1,
            'trailsreviewed': 0

        }
        signup_ref = db.collection('Credentials').document(username)
        if signup_ref.get().exists:
            return 'Please use another username as this one is taken.', 400
        else:
            result = signup_ref.set(data)
            return 'success', 200

    else:
        # return render_template('login.html')
        return 'Method only posts data to DB'

    # result = firebase.post('/login-auth-42458-default-rtdb/Credentials', data)
    '''
    usern = request.form['uname']
    passwo = request.form['passw']
    print(usern)
    "\n"
    print(passwo)

    # login_ref = db.collection('Credentials').document('firstEntry')
    login_ref = db.collection('Credentials')
    login_ref.add({
        'username': usern,
        'password': passwo
    })
    #return redirect('/')
    '''


@app.route('/login/<string:username>/<string:password>', methods=['GET'])
def login(username: str, password: str):
    if request.method == 'GET':
        doc_ref = db.collection('Credentials').document(username).get()
        if doc_ref.exists:
            contents = doc_ref.to_dict()
            if password == contents['password']:
                print(f'Document data: {doc_ref.to_dict()}')
                return contents, 200
            else:
                return "Incorrect password", 404
        else:
            print('No such document!')
            data = {
                "error": "Incorrect username"
            }
            return "Incorrect username", 404
    else:
        return 'Use GET method'

        # result = firebase.get("/login-auth-42458-default-rtdb/Credentials", '')
        # return contents, 200
        # return contents['password']
    # else:
    # return 'wrong call', 404


@app.route('/changepassword/<string:username>/<string:password>', methods=['PATCH'])
def changePassword(username: str, password: str):
    if request.method == 'PATCH':
        doc_ref = db.collection('Credentials').document(username)
        if doc_ref.get().exists:
            data = {
                "password": password
            }
            doc_ref.update(data)
            return 'success', 200
        else:
            return 'User not found', 404
    else:
        return 'Use PATCH method', 404


@app.route('/increaseuserrating/<string:username>', methods=['PATCH'])
def updateUserRating(username: str):
    if request.method == 'PATCH':
        '''
        doc_ref = db.collection('Credentials').document(username)
        if doc_ref.get().exists:
            data = {
                "userrating": userrating
            }
            doc_ref.update(data)
            return 'success'
        else:
            return 'User not found'

    else:
        return 'Use PATCH method'
        '''
        doc_ref = db.collection('Credentials').document(username).get()
        doc_ref1 = db.collection('Credentials').document(username)
        if doc_ref.exists:
            contents = doc_ref.to_dict()
            data = {
                "userrating": contents["userrating"] + 1
            }
            doc_ref1.update(data)
            return 'success'
        else:
            return 'User not found'

@app.route('/decreaseuserrating/<string:username>', methods=['PATCH'])
def decreaseUserRating(username: str):
    if request.method == 'PATCH':
        doc_ref = db.collection('Credentials').document(username).get()
        doc_ref1 = db.collection('Credentials').document(username)
        if doc_ref.exists:
            contents = doc_ref.to_dict()
            data = {
                "userrating": contents["userrating"] - 1
            }
            if contents["userrating"] > 0:
                doc_ref1.update(data)
            return 'success'
        else:
            return 'User not found'


@app.route('/getuserrating/<string:username>', methods=['GET'])
def getUserRating(username: str):
    if request.method == 'GET':
        doc_ref = db.collection('Credentials').document(username).get()
        if doc_ref.exists:
            contents = doc_ref.to_dict()
            print(f'Document data: {doc_ref.to_dict()}')
            userr = contents['userrating']
            return str(userr), 200
        else:
            print('No such document!')
            return 'Incorrect username', 404
    else:
        return 'Use GET method'


@app.route('/addcomment/<string:username>/<string:comment>', methods=['PATCH'])
def addComment(username: str, comment: str):
    if request.method == 'PATCH':
        doc_ref = db.collection('Credentials').document(username)
        # UNSURE
        if doc_ref.get().exists:
            data = {
                "comments": comment
            }
            snapshot = doc_ref.get('comments')
            doc_ref.update(data, snapshot)
            return 'success'
        else:
            return 'User not found'

    else:
        return 'Use PATCH method'


@app.route('/getusercomment/<string:username>', methods=['GET'])
def getUserComment(username: str):
    if request.method == 'GET':
        doc_ref = db.collection('Credentials').document(username).get()
        if doc_ref.exists:
            contents = doc_ref.to_dict()
            print(f'Document data: {doc_ref.to_dict()}')
            userr = contents['comments']
            return str(userr), 200
        else:
            print('No such document!')
            return 'Incorrect username', 404
    else:
        return 'Use GET method'


@app.route('/settrailsreviewed/<string:username>/<int:trailsrev>', methods=['PATCH'])
def setTrailsReviewed(username: str, trailsrev: int):
    if request.method == 'PATCH':
        doc_ref = db.collection('Credentials').document(username)
        if doc_ref.get().exists:
            data = {
                "trailsreviewed": trailsrev
            }
            doc_ref.update(data)
            return 'success'
        else:
            return 'User not found'

    else:
        return 'Use PATCH method'


# Fix later
@app.route('/updatetrailsreviewed/<string:username>', methods=['GET'])
def updateTrailsReviewed(username: str):
    if request.method == 'GET':
        doc_ref = db.collection('Credentials').document(username).get()
        if doc_ref.exists:
            contents = doc_ref.to_dict()
            print(f'Document data: {doc_ref.to_dict()}')
            userr = contents['comments']
            return str(userr), 200
        else:
            print('No such document!')
            return 'Incorrect username', 404
    else:
        return 'Use GET method'


# Make an update method
@app.route('/settrailsvisited/<string:username>/<int:trailvisit>', methods=['PATCH'])
def setTrailsVisited(username: str, trailvisit: int):
    if request.method == 'PATCH':
        doc_ref = db.collection('Credentials').document(username)
        if doc_ref.get().exists:
            data = {
                "trailsvisited": trailvisit
            }
            doc_ref.update(data)
            return 'success'
        else:
            return 'User not found'

    else:
        return 'Use PATCH method'


@app.route('/deleteaccount/<string:username>', methods=['DELETE'])
def deleteAccount(username: str):
    if request.method == 'DELETE':
        doc_ref = db.collection('Credentials').document(username)
        if doc_ref.get().exists:
            doc_ref.delete()
            return 'success', 200
        else:
            return 'User not found', 404
    else:
        return 'Use DELETE method', 404
    '''
# RESTful API - uses the realtime database
class Get(Resource):
    def get(self):
        # args = post_put_args.parse_args()
        result = firebase.get('/login-auth-42458-default-rtdb/Credentials', '')
        print(result)


api.add_resource(Get, "/getUserInfo")
'''


@app.route('/allValues', methods=['GET'])
def allValues():
    trails_ref = db1.collection('trails_v')

    new_dict = defaultdict(list)

    count = 0

    # assign all trail names and lat/long in database to dictionary
    # nested dictionary- within value of first dictionary, theres key-value pairs for each attribute
    for doc in trails_ref.stream():
        dict = doc.to_dict()
        new_dict[count] = (dict)
        count += 1

    return new_dict


@app.route('/nearRank/<string:lat>/<string:long>', methods=['GET'])
def nearRank(lat: str, long: str):
    trails_ref = db1.collection('trails_v')

    new_dict = defaultdict(list)

    # assign all trail names and lat/long in database to dictionary
    # (lat/long is a list within a list as a value of the dictionary)
    for doc in trails_ref.stream():
        temp_list = []
        dict = doc.to_dict()
        temp_list.append(dict['X'])
        temp_list.append(dict['Y'])
        new_dict[dict['TrailheadName']].append(temp_list)

    # find the distance between two lat-long coordinates

    radius = 6373.0  # radius of the earth

    lat1 = math.radians(float(lat))  # convert coordinates from degrees to radians
    long1 = math.radians(float(long))

    lat2 = 0
    long2 = 0

    dist_dict = defaultdict(list)

    for key in new_dict:  # {"John Trail" : "123123,123123"
        lat2 = math.radians(float(new_dict[key][0][0]))
        long2 = math.radians(float(new_dict[key][0][1]))
        dlong = long2 - long1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2) ** 2  # Haversine formula
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c
        dist_dict[key] = distance

    sorted_values = sorted(dist_dict.values())
    sorted_dict = {}

    for i in sorted_values:
        for k in dist_dict.keys():
            if dist_dict[k] == i:
                sorted_dict[k] = dist_dict[k]
                break

    # NEW
    # print(sorted_dict)

    count = 0

    big_dict = defaultdict(list)

    for doc in trails_ref.stream():
        temp_list = []
        dict = doc.to_dict()
        big_dict[count] = (dict)
        count += 1

    mega_dict = {}

    count2 = 0

    for key in sorted_dict:
        # print(key)
        for key2 in big_dict:
            if big_dict[key2]['TrailheadName'] == key:
                mega_dict[count2] = (big_dict[key2])
                # NEW CODE
                data = {
                    "distance": sorted_dict[key]
                }
                # (mega_dict.update(data))
                mega_dict[count2]['distance'] = sorted_dict[key]
                # ---
                count2 += 1
                break

    json_object = json.dumps(mega_dict, indent=4)
    # print(json_object)
    print(mega_dict)
    # return json_object
    return mega_dict

    '''
    top_eight= []
    count=0
    while count<8:
        top_eight.append(sorted_dict[count])
        count+=1


    return str(top_eight)


        with open('models/customer.json', 'r') as j:
        schema = json.loads(j.read())

    errors = validator.validate(schema, mega_dict)
    for err in errors:
        print(err['msg'])

    sort_dict = defaultdict(list)

    sort_dict= sorted(dist_dict.items(), key=lambda x: x[1])


       for doc in trails_ref.stream():
           dict= doc.to_dict()
           new_dict[dict['TrailheadName']].append(str(dict['X'])+','+str(dict['Y']))
           count+=1
    '''

    # return new_dict
    # return str(new_dict['Bay Lake Trailhead'][0][0])
    # return new_dict['Waterfront Park'][0]


@app.route('/closeBy/<int:lat>/<int:long>', methods=['GET'])
def closeBy(lat: int, long: int):
    number = str(lat + long)
    return number


@app.route('/restrooms/<string:yaboobae>', methods=['GET'])
def Restrooms(yaboobae: str):
    trails_ref = db1.collection('trails_v')
    docs = trails_ref.where('Restrooms', '==', 'Yes').stream()

    name = []
    x = []
    y = []

    for doc in docs:
        dict = doc.to_dict()
        name.append(dict['TrailName'])
        x.append(round(dict['X'], 4))
        y.append(round(dict['Y'], 4))

    new_dict = defaultdict(list)

    for i in range(len(name)):
        new_dict[i].append("{} @ location: {}, {}".format(name[i], x[i], y[i]))
    return new_dict;


if __name__ == '__main__':
    app.run(Debug=True)
