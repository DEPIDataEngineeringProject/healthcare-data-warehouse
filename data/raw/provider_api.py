from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

providers_df = pd.read_csv(r'D:\DEPI\DEPI final project\data sources\providers.csv')

@app.route("/providers", methods=["GET"])
def get_providers():

    specialty = request.args.get("SPECIALITY")

    if specialty:
        filtered = providers_df[
            providers_df["SPECIALITY"].str.lower() == specialty.lower()
        ]
        return jsonify(filtered.to_dict(orient="records"))

    return jsonify(providers_df.to_dict(orient="records"))


@app.route("/providers/<provider_id>", methods=["GET"])
def get_provider_by_id(provider_id):

    provider = providers_df[providers_df["Id"] == provider_id]

    if provider.empty:
        return jsonify({"message": "Provider not found"}), 404

    return jsonify(provider.to_dict(orient="records")[0])


if __name__ == "__main__":
    app.run(debug=True)