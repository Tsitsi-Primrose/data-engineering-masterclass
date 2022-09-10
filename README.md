# Data Engineering masterclass

```bash
pip3 install virtualenv
```

```bash
virtualenv streamlit_app
```

```bash
source streamlit_app/bin/activate
```

(to deactivate virtual env)

```bash
source streamlit_app/bin/deactivate
```

Install dependendencies

```bash
pip3 install -r requirements.txt
```

streamlit run app.py

## Building using docker

docker build -t de_masterclass .
docker run -p 8501:8501 de_masterclass

Visit
http://localhost:8501/ to view your app
