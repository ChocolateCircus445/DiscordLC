import os
from packages import discord

token, path = "null", "null"

print(os.path.dirname(os.path.realpath(__file__)))

def extract_info():
    global token, path
    f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.txt"), "r").read().split("\n")
    for i in f:
        if i.startswith("token="):
            token = i.split("=")[1]
        elif i.startswith("directory="):
            path = i.split("=")[1]


def send_to_file(c):
    open(path, "w").write(c)
    return "Success!"

def get_msg_args(c):
    a = c.split('"')[0].strip()
    return a.split(" ")

def has_quotes(c):
    if '"' in c:
        return True
    return False

extract_info()

client = discord.Client()

@client.event
async def on_message(msg):
    charnames = ("sayori", "natsuki", "yuri", "monika")
    c = msg.content
    if True: #too lazy to indent, tried "with as", did NOT end well
        if c.startswith("!d "):

            valid_type = False
            is_hide = False

            if ('"' in c and get_msg_args(c)[1] != "hide") or (not '"' in c and get_msg_args(c)[1] == "hide"):
                valid_type = True

            if valid_type and get_msg_args(c)[1] == "hide":
                is_hide = True

            accept_criteria = [
                1 < len(get_msg_args(c)) < 4,
                valid_type,
                get_msg_args(c)[1] in charnames or is_hide
            ]
            error_outs = [
                "Invalid number of arguments",
                "Invalid format",
                "Unknown character"
            ]
            if all(accept_criteria):
                await msg.channel.send(send_to_file(c))
            else:
                count = 0
                for i in accept_criteria:
                    if not i:
                        await msg.channel.send(":x:" + error_outs[count])
                        break
                    count += 1

client.run(token)
