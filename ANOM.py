# Denis Atwell
# 30.05.2022
# JS.proto.anom

import requests
import json
import sqlite3
import asyncio
import datetime
import colorama

# token: 
# api: https://api.telegram.org/bot
# res: 

# "iMa":   295, - current
# "iWa":   64,  - active
# "iVA":   65,  - full
# "iVar": -10,  - reactive

async def req():
    api = "http://10.210.1.183:8888/api/cachedStatus"
    res = json.loads(requests.get(api).content)
    await asyncio.sleep()

def main(inp = None):

    requests.get("https://api.telegram.org/ /sendMessage?chat_id=1023337472&text=")

    testVal = {"iMa": list(range(293, 296)), "iWa": list(range(60, 65)), "iVA": list(range(62, 66)), "iVar": list(range(-11, -8))}

    # Colorama
    colorama.init()

    # DB
    db = sqlite3.connect("./cases.db").cursor()
    db.execute("DROP TABLE cases")
    db.execute("CREATE TABLE cases('iMaMIN' INT, 'iMaMAX' INT, 'iWaMIN' INT, 'iWaMAX' INT, 'iVAMIN' INT, 'iVAMAX' INT, 'iVarMIN' INT, 'iVarMAX INT')")
    db.execute(f"INSERT INTO cases VALUES({min(testVal['iMa'])}, {max(testVal['iMa'])}, {min(testVal['iWa'])}, {max(testVal['iWa'])}, {min(testVal['iVA'])}, {max(testVal['iVA'])}, {min(testVal['iVar'])}, {max(testVal['iVar'])})") 
    db.execute("SELECT * FROM cases")
    fetch = db.fetchall()[0]

    if (fetch[0] > inp['iMa'] or fetch[1] < inp['iMa']) or (fetch[2] > inp['iWa'] or fetch[3] < inp['iWa']) or (fetch[4] > inp['iVA'] or fetch[5] < inp['iVA']) or (fetch[6] > inp['iVar'] or fetch[7] < inp['iVar']):
        txt = f"Warning!\nSName: KrepkiyLob\niMa: {inp['iMa']}\niWa: {inp['iWa']}\niVA1: {inp['iVA']}\niVar: {inp['iVar']}"
        requests.get(f"https://api.telegram.org/ /sendMessage?chat_id=5011225208&text={txt}")
        print(colorama.Fore.LIGHTRED_EX, txt)
    else:
        print(f'{colorama.Fore.LIGHTCYAN_EX}All is okay')
        requests.get("https://api.telegram.org/ /sendMessage?chat_id=5011225208&text=All is okay!")

# Main
if __name__ == "__main__":
    choice = int(input('1: custom\n2: from RPCM\n'))
    if choice == 1:
        iMa, iWa, iVA, iVar = map(int, input("iMa iWa iVA1  iVar\n").split())
        main({"iMa": iMa, "iWa": iWa, "iVA": iVA, "iVar": iVar})
    elif 2:
        res = json.loads(requests.get("http://10.210.1.183:8888/api/cachedStatus").content.decode('utf-8'))['ats']['channels']['1']
        main({"iMa": res['iMa'], "iWa": res['iWa'], "iVA": res['iVA'], "iVar": res['iVar']})

    
