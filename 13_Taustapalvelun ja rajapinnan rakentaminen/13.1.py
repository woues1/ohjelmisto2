from flask import Flask, request

app = Flask(__name__)

@app.route("/is_prime")
def is_prime():
    n = int(request.args.get("n"))
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{i} is not a prime number"
    return f"{n} is a prime number"

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
