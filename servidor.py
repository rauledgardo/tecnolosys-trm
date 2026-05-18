from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/datos')
def datos():
    try:
        url = "https://www.datos.gov.co/resource/32sa-8pi3.json?$limit=1&$order=vigenciadesde DESC"
        r = requests.get(url, timeout=10)
        trm = float(r.json()[0]['valor'])
    except:
        trm = 0
    
    return jsonify({
        "TRM": f"${trm:,.2f}",
        "fecha": datetime.now().strftime("%d/%m/%Y"),
        "hora": datetime.now().strftime("%H:%M"),
        "mensaje": f"TECNOLOSYS | TRM: ${trm:,.2f} | {datetime.now().strftime('%d/%m/%Y')}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
