# sample-s3-input

npm install -g serverless
serverless create \
  --template aws-python3 \
  --name sample-s3-input \
  --path sample-s3-input
cd sample-s3-input
npm init -f
npm install --save serverless-python-requirements
virtualenv venv --python=python3
source venv/bin/activate (Linux)
venv\Scripts\activate (Windows)
pip install {requirements}
pip freeze > requirements.txt
