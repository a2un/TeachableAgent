from pb_py import main as API
import sys

# Global parameters
HOST = 'aiaas.pandorabots.com'
USER_KEY = "7d387c332ebfa536b90b7820426ed63b"
APP_ID = "1409611535153"
BOT = "nico"

   
def response(topic):
    response = API.talk(USER_KEY, APP_ID, HOST, BOT, topic)
    bot_response = response['response']
    print bot_response


def main():
    problem = sys.argv[1]
    step = sys.argv[2]
    topic = problem + " " + step
    response(topic)

if __name__ == '__main__': main()