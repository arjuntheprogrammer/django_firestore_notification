import time
from datetime import timedelta
from uuid import uuid4
from firebase_admin import firestore, credentials, initialize_app


class FirestoreClass:
    def __init__(self) -> None:
        self.db = firestore.Client()

    def initialise(self, ):
        # Use the application default credentials
        cred = credentials.Certificate(
            'django_firestore/firebase_config/joshskills-1dd9b-firebase-adminsdk-fp44k-9d3fcf0bbc.json')
        initialize_app(cred)

        db = firestore.client()
        return db

    def add_data_one(self, ):
        doc_ref = self.db.collection(u'users').document(u'alovelace')
        doc_ref.set({
            u'first': u'Ada',
            u'last': u'Lovelace',
            u'born': 1815
        })

    def add_data_two(self, ):
        doc_ref = self.db.collection(u'users').document(u'aturing')
        doc_ref.set({
            u'first': u'Alan',
            u'middle': u'Mathison',
            u'last': u'Turing',
            u'born': 1912
        })

    def get_collection(self, ):
        users_ref = self.db.collection(u'users')
        docs = users_ref.stream()

        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

    @staticmethod
    def send_to_firebase(raw_notification):
        db = firestore.client()
        start = time.time()
        db.collection('notifications').document(
            str(uuid4())).create(raw_notification)
        end = time.time()
        spend_time = timedelta(seconds=end - start)
        return spend_time

    @staticmethod
    def update_firebase_snapshot(snapshot_id):
        start = time.time()
        db = firestore.client()
        db.collection('notifications').document(snapshot_id).update(
            {'is_read': True}
        )
        end = time.time()
        spend_time = timedelta(seconds=end - start)
        return spend_time
