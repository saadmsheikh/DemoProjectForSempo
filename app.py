from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        word = request.form.get('word')
        status = isPalindrome(word)
        if status == True:
            return render_template('ptrue.html')
        else:
            return render_template('pfalse.html')

    return render_template('index.html')

def isPalindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    app.run()

