from flask import render_template, redirect, url_for
from app.forms.mahasiswa import MahasiswaSave
from app.models.models import Mahasiswa

class MahasiswaController():
    
    def mahasiswaSave(self):
        form = MahasiswaSave()
        if form.validate_on_submit():
            mahasiswa = Mahasiswa(nim=form.nim.data, nama=form.nama.data)
            mahasiswa.save()
            return redirect(url_for('mahasiswaall'))
        return render_template('mahasiswa.html', form=form)
    
    def mahasiswaShow(self):
        mahasiswaAll = Mahasiswa().getAll()
        return render_template('show.html', mahasiswaAll=mahasiswaAll)
    
