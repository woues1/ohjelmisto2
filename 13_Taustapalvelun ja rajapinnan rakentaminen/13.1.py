from flask import Flask

# http://127.0.0.1:3000/is_prime/31

app = Flask(__name__)

@app.route("/is_prime/<num>")
def is_prime(num):
    n = int(num)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime number"
    return f"{n} is a prime number"

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
