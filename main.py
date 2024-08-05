from src.app import app
# def before_request():
#   if not request.is_secure:
#     url = request.url.replace('http://', 'https://', 1)
#     code = 301
#     return redirect(url, code=code)

# export LC_ALL=C
# sudo python3 -m venv venv
# . venv/bin/activate

if __name__ == '__main__':
  app.run(debug=True)
