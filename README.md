# Timetabler


## Installation

* **Clone the repository**

```
git clone https://github.com/gabeha/timetabler-flask-vue.git
```

## Install the dependencies for the Frontend
```bash
cd timetabler-flask-vue/client
npm install                         #install the required npm packages
```
## Install the dependencies for the Backend
```bash
cd timetabler-flask-vue
python3 -m venv env                 #create a virtual environment
.\env\Scripts\activate              #activate the virtual environment
pip install -r requirements.txt     #install the required python packages
```

---

### In two seperate consoles, run the Frontend and the Backend
#### To run the Frontend in development mode
```bash
cd timetabler-flask-vue/client
npm run dev
```
#### To run the Backend in development mode
```bash
cd timetabler-flask-vue
flask run
```

The app will now be hosted on port http://localhost:5173/




