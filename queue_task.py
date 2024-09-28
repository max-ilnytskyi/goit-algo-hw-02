from queue import Queue
import random

queue = Queue()

last_request_id = 0


def generate_request():
    global last_request_id
    last_request_id += 1
    request_id = last_request_id
    queue.put(request_id)
    print(f"+ Generated request {request_id}")


def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"- Processing request {request_id}")
        return "not_empty"
    else:
        print("No incoming requests")
        return "empty"


start_requests_num = 3

for _ in range(start_requests_num):
    generate_request()

while True:
    if random.choice([True, False]):
        generate_request()
    process_result = process_request()

    if process_result == "empty":
        break
