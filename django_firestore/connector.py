from django.http import JsonResponse

from .firebase import FirestoreClass

__all__ = ['send_message', 'make_as_read']

FirestoreClass().initialise()


def send_message(request):
    message = request.GET.get('message', "")
    raw_notification = {
        "message": message,
        "is_read": False
    }
    spend_time = FirestoreClass.send_to_firebase(raw_notification)
    return JsonResponse(
        {"message": 'Notification created',
         "spend_time": spend_time}, status=201)


def make_as_read(request):
    snapshot_id = request.GET.get('snapshot_id')
    if not snapshot_id:
        return JsonResponse(
            {'message': 'You have to send a snapshot id'},
            status=400)

    spend_time = FirestoreClass.update_firebase_snapshot(snapshot_id)
    return JsonResponse(
        data={'message': 'OK', 'spend_time': spend_time},
        status=200)
