import sender_stand_request

def test_get_order_by_track():
    new_order_track = sender_stand_request.get_new_order_track()
    get_order_by_track_response = sender_stand_request.get_order_by_track(str(new_order_track))
    assert get_order_by_track_response.status_code == 200

# Артём Иванов, 22A когорта — Финальный проект. Инженер по тестированию плюс