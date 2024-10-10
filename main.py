from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_annual_data():
    well_api = request.args.get('well')
    conn = sqlite3.connect('production_data.db')
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute('''SELECT OIL, GAS, BRINE FROM production WHERE "API WELL  NUMBER" = ?''', (well_api,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({
            "oil": row[0],
            "gas": row[1],
            "brine": row[2]
        })
    else:
        return jsonify({"error": "Well API number not found"}), 404

if __name__ == '__main__':
    app.run(port=8080)
