import requests

def check_site_availability(url, timeout=5):
    """
    Проверяет доступность сайта.
    Возвращает словарь с результатом проверки.
    """
    try:
        response = requests.get(url, timeout=timeout)
        return {
            "url": url,
            "is_available": response.status_code == 200,
            "status_code": response.status_code,
        }
    except requests.exceptions.RequestException as error:
        return {
            "url": url,
            "is_available": False,
            "status_code": None,
            "error": str(error),
        }