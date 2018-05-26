from app import app
from app.controllers.mahasiswa import MahasiswaController

@app.route('/')
@app.route('/index')
def index():
    return 'lagi testing saja'

@app.route('/mahasiswa', methods=['GET', 'POST'])
def mahasiswa():
    return MahasiswaController().mahasiswaSave()

@app.route('/mahasiswa/all')
def mahasiswaall():
    return MahasiswaController().mahasiswaShow()
