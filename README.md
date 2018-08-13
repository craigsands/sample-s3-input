# sample-s3-input

## Scratch installation

##### Install NodeJS

Download and install from [here](https://nodejs.org/en/).

##### Install Serverless
```bash
npm install -g serverless
```

##### Create the project folder (with sample Python module)
```bash
serverless create \
  --template aws-python3 \
  --name sample-s3-input \
  --path sample-s3-input
```

##### Initialize NPM (and dependencies) within the project folder
```bash
cd sample-s3-input
npm init -f
npm install --save serverless-python-requirements
```

##### Create a Python 3 virtual environment for local testing (optional)
```bash
virtualenv venv --python=python3
source venv/bin/activate  # Linux
venv\Scripts\activate  # Windows
```

##### Install any required Python modules (optional)
```bash
pip install numpy
```

##### Create a requirements.txt file of Python dependencies
```bash
pip freeze > requirements.txt
```

## Deploy the project to AWS
```bash
serverless deploy
```
