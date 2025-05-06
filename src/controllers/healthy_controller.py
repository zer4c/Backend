from src.services.healthy_service import check_healthy

def healthy_response():
    return check_healthy()