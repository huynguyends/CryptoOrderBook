import json

import pandas as pd
import websocket

# df = pd.DataFrame(columns=['foreignNotional', 'grossValue', 'homeNotional', 'price', 'side',
#                            'size', 'symbol', 'tickDirection', 'timestamp', 'trdMatchID'])

try:
    import thread
except ImportError:
    import _thread as thread
import time
def on_message(ws, message):
    msg = json.loads(message)
    print(msg)
    # global df
    # # `ignore_index=True` has to be provided, otherwise you'll get
    # # "Can only append a Series if ignore_index=True or if the Series has a name" errors
    # df = df.append(msg, ignore_index=True)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send('{"op": "subscribe", "args": ["orderBook_200.100ms.BTCUSD"]}')
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())
    return


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://stream-testnet.bybit.com/realtime",
                                on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    
    
    ws.run_forever()