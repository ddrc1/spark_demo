{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1de1e888-c06e-463d-bd9b-76528f20f161",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tweepy\n",
    "from tweepy import OAuthHandler, Stream\n",
    "import socket\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ee7daac2-2707-4a0f-accf-dfc12be57a1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "consumer_secret = 'bYOLrnkvJdCJeF3iYBAamLQY5HXwla5hz5mzWJiyAP9K0i9jul'\n",
    "consumer_key = 'v3SoyRIi7d5xzjDiPUMgU5qS3'\n",
    "access_token = '1497787515088035840-glE4iazjAbFDsVp7MiGyvJVHbR9wZp'\n",
    "token_secret = 'ge0ntMRn9yZ95xmeaDHCeSbKRJ9Nbtqjj3zuPOwr8BFsf'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3533f57f-6e84-43a7-962c-a0b3433f39a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "class TweetListener(Stream):\n",
    "    def __init__(self, csocket):\n",
    "        self.client_socket = csocket\n",
    "        \n",
    "    def on_data(self, data):\n",
    "        try:\n",
    "            msg = json.loads(data)\n",
    "            print(msg['text'].encode('utf-8'))\n",
    "            self.client_socket.send(msg['text'].encode('utf-8'))\n",
    "            return True\n",
    "        except BaseException as e:\n",
    "            print('ERROR', e)\n",
    "        return True\n",
    "    \n",
    "    def on_error(self, status):\n",
    "        print(status)\n",
    "        return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "da3759b2-4734-45d6-a9fb-d4b72f18efec",
   "metadata": {},
   "outputs": [],
   "source": [
    "def send_data(csocket):\n",
    "    auth = OAuthHandler(consumer_key, consumer_secret)\n",
    "    auth.set_access_token(access_token, access_secret)\n",
    "    \n",
    "    twitter_stream = Stream(auth, TweetListener(csocket))\n",
    "    twitter_stream.filter(track=['guitar'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e9ddecc-7868-45c5-800e-d8f3c1f2358c",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == '__main__':\n",
    "    s = socket.socket()\n",
    "    host = '127.0.0.1'\n",
    "    port = 5555\n",
    "    s.bind((host, port))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
