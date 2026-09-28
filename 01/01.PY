from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota para cálculo de combustível e estimativa de trajeto
@app.route('/api/calcular-rota', methods=['POST'])
def calcular_rota():
    data = request.get_json()
    
    origem = data.get('origem')
    destino = data.get('destino')
    distancia_km = float(data.get('distancia_km', 0))  # Ex: 2100 km (Recife a SP ~2.700km)
    autonomia = float(data.get('autonomia_kml', 3.5))   # Ex: Caminhão faz 3.5 km/l
    preco_combustivel = float(data.get('preco_litro', 5.89))

    litros_necessarios = distancia_km / autonomia
    custo_total = litros_necessarios * preco_combustivel

    return jsonify({
        "origem": origem,
        "destino": destino,
        "distancia_km": distancia_km,
        "litros_estimados": round(litros_necessarios, 2),
        "custo_estimado_reais": round(custo_total, 2),
        "link_waze": f"https://waze.com/ul?q={destino}&navigate=yes",
        "link_google_maps": f"https://www.google.com/maps/dir/?api=1&origin={origem}&destination={destino}"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)