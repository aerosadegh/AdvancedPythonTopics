# %%%%%%%%%%%%%%%%%%%%%%%%%%
import cProfile
from time import sleep


def api_call():
    sleep(2)


def load_data():
    for i in range(10**5):
        i


def sort_data():
    load_data()

    for i in range(10**6):
        i
    sleep(2)


def process_data():
    for i in range(10**3):
        i


def get_page():
    api_call()
    load_data()
    sort_data()
    process_data()


print("Get Profiling ...")

cProfile.run("get_page()", sort="cumtime")
