import requests

def test_recommend_by_description_endpoint():
    response = requests.get("http://0.0.0.0:80/recommend_by_description?description=Mother")
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    for element in data:
        assert 'title' in element and isinstance(element['title'], str)
        assert 'thumbnail' in element and isinstance(element['thumbnail'], str)
        assert 'description' in element and isinstance(element['description'], str)
        assert 'average_rating' in element and isinstance(element['average_rating'], (float, int))


def test_recommend_by_title_endpoint():
    response = requests.get("http://0.0.0.0:80/recommend_by_title?title=In a Sunburned Country")
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    for element in data:
        assert 'title' in element and isinstance(element['title'], str)
        assert 'thumbnail' in element and isinstance(element['thumbnail'], str)
        assert 'description' in element and isinstance(element['description'], str)
        assert 'average_rating' in element and isinstance(element['average_rating'], (float, int))


