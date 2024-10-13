import configuration
import data
import requests

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.POST_CREATE_ORDER_PATH,
                         json=order_body)

def get_new_order_track():
    return post_new_order(data.order_body).json()["track"]

def get_order_by_track(str_track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + '?t=' + str_track_number)