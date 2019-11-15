from hello_app.views import func


def test_answer():
    assert func(3) == 4
