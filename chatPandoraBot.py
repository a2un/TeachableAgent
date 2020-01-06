from pb_py import main as API
import sys
import json

# Global parameters
HOST = 'api.pandorabots.com'
USER_KEY = "0f1473bc84221a5524b0c3c6ad138e8c"
APP_ID =  "un5f098976"
#BOT_NAME = 'cobi'
#COBI_BOTKEY = 'ydFwh9aChnKyEJ6LRrdDRdi4t8vfXSPHOMy84nRx-c7Q34HeiygUE8WcpgLuvU8rYpoe-KPxn3Y~'
nico_BOTKEY = 'ydFwh9aChnLIV1klwtqOwmj9YVoyW0StuuW1kw2rpVaOVokZNl5PZIVvneNUHKU8O_1CeaLOOCxalByRKUY_JA~~'



def response(transcriptFile, pathForResponse, BOT, userid):
    # currently the sdk needs to create an instance of bot to do the talking thing
    bot = API.Pandorabots(USER_KEY, APP_ID, HOST, BOT, nico_BOTKEY)
    fileWrite = open(pathForResponse, 'w')
    with open(transcriptFile) as f:
        for line in f:
            # response = API.talk(USER_KEY, APP_ID, HOST, BOT, line, clientID=userid)
            input = {'message': line}
            # I didn't modify the broken talk method in the sdk, instead, I am using atalk just for now
            # will look into the sdk and original version of API of pandora to make sure the bug fixing of SDK is correct
            response = bot.atalk(input)
            bot_response = json.loads(response.text)
            # this is just a test output, ignore the possibility that there are more than one response from the server
            output_str = bot_response['responses'][0]
            fileWrite.write(output_str)
    fileWrite.close()

def main():
    fileOfTranscript = sys.argv[1]
    pathForResponse = sys.argv[2]
    BOT = sys.argv[3]
    userid = sys.argv[4]

    response(fileOfTranscript, pathForResponse, BOT, userid)

if __name__ == '__main__': main()
