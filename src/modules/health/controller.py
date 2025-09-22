from src.modules.health.service import check_healthy


def healthy_response():
    return check_healthy()
