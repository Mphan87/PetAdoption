from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)
db.create_all()

@app.route('/')
def index():
    listing = Pet.query.all()
    return render_template("home.html", listing = listing)

@app.route('/add' ,methods=["GET"])
def show_form():
    form = AddPetForm()
    return render_template("form.html", form = form)

@app.route('/add' ,methods=["POST"])
def post_data():
    form = AddPetForm()
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age =  form.age.data
    notes = form.notes.data
    new_pet = Pet(name = name, species = species , photo_url = photo_url, age =  age, notes= notes)
    db.session.add(new_pet)
    db.session.commit()
    return redirect("/add")

@app.route('/<int:pet_id>',methods=["GET"])
def detail_data(pet_id):
    details = Pet.query.get_or_404(pet_id)
    return render_template("details.html", details = details)

@app.route('/<int:pet_id>/edit',methods=["GET"])
def show_edit_data(pet_id):
    form = EditPetForm()
    return render_template("editform.html", form = form)

@app.route('/<int:pet_id>/edit',methods=["POST"])
def edit_data(pet_id):
    form = EditPetForm()
    details = Pet.query.get_or_404(pet_id)
    details.photo_url = form.photo_url.data
    details.notes = form.notes.data
    details.available = form.available.data
    db.session.commit()
    return redirect("/")

@app.route('/<int:pet_id>/delete',methods=["POST"])
def delete_data(pet_id):
    details = Pet.query.get_or_404(pet_id)
    db.session.delete(details)
    db.session.commit()
    return redirect("/")








    
    
    
    


