from celery import shared_task


@shared_task(bind=True)

def test_func(self):
    for i in range(10):
        print(i)
    for _ in range(1,10):
        print(_)
    return "Done"