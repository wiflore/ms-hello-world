import logging
import settings
import routes
from bottle import run, get

@get(routes.HEALTH_CHECK)
def health_check():
    return {
        'app_name': settings.APP_NAME,
        'version': settings.APP_VERSION,
        'message': f'{settings.APP_NAME} up and running!'
    }

def run_server():
    logging.info("Starting Server")
    run(host="0.0.0.0", port=8080, server="paste")

if __name__ == '__main__':
    run_server()